print("Prajwal BR\nUSN1AY24AI083\nSec:O")
import random
from abc import ABC, abstractmethod
from collections import defaultdict

class Die:
    COLORS = {
        'green': ['brain']*3 + ['shotgun']*1 + ['footprint']*2,
        'yellow': ['brain']*2 + ['shotgun']*2 + ['footprint']*2,
        'red': ['brain']*1 + ['shotgun']*3 + ['footprint']*2
    }
    
    def __init__(self, color):
        self.color = color
        self.face = None
    
    def roll(self):
        self.face = random.choice(self.COLORS[self.color])
        return self.face

class Player(ABC):
    def __init__(self, name):
        self.name = name
        self.brains = 0
        self.shotguns = 0
        self.turn_brains = 0
        self.turn_shotguns = 0
    
    def reset_turn(self):
        self.turn_brains = 0
        self.turn_shotguns = 0
    
    def record_roll(self, results):
        for result in results:
            if result == 'brain':
                self.turn_brains += 1
            elif result == 'shotgun':
                self.turn_shotguns += 1
    
    def end_turn(self, success):
        if success:
            self.brains += self.turn_brains
        self.reset_turn()
    
    @abstractmethod
    def decide_continue(self, game_state):
        pass

class GameState:
    def __init__(self, player, dice_in_hand, remaining_dice):
        self.player = player
        self.dice_in_hand = dice_in_hand
        self.remaining_dice = remaining_dice
        self.turn_stats = {
            'rolls': 0,
            'brains': player.turn_brains,
            'shotguns': player.turn_shotguns
        }

class CowardlyBot(Player):
    """Always stops after first roll"""
    def decide_continue(self, game_state):
        return False

class CautiousBot(Player):
    """Stops after 1 shotgun or 2+ brains"""
    def decide_continue(self, game_state):
        return not (self.turn_shotguns >= 1 or self.turn_brains >= 2)

class BalancedBot(Player):
    """Balanced risk-taking"""
    def decide_continue(self, game_state):
        if self.turn_shotguns >= 2:
            return False
        if self.turn_brains >= 4:
            return False
        return True

class RecklessBot(Player):
    """Only stops at 3 shotguns"""
    def decide_continue(self, game_state):
        return self.turn_shotguns < 3

class StatisticalBot(Player):
    """Makes decisions based on probability"""
    def decide_continue(self, game_state):
        if self.turn_shotguns >= 3:
            return False
        
        dice_colors = [die.color for die in game_state.dice_in_hand]
        color_counts = defaultdict(int)
        for color in dice_colors:
            color_counts[color] += 1
        
        expected_brains = 0
        expected_shotguns = 0
        
        for color, count in color_counts.items():
            faces = Die.COLORS[color]
            brain_prob = faces.count('brain') / len(faces)
            shotgun_prob = faces.count('shotgun') / len(faces)
            
            expected_brains += brain_prob * count
            expected_shotguns += shotgun_prob * count
        
        risk_factor = (self.turn_shotguns + expected_shotguns) / 3
        reward_factor = (self.turn_brains + expected_brains) / 13
        
        return risk_factor < 0.7 and reward_factor < 0.8

class ZombieDiceGame:
    def __init__(self, players):
        self.players = players
        self.current_player_idx = 0
        self.reset_dice_cup()
    
    def reset_dice_cup(self):
        self.dice_cup = (
            [Die('green') for _ in range(6)] +
            [Die('yellow') for _ in range(4)] +
            [Die('red') for _ in range(3)]
        )
        random.shuffle(self.dice_cup)
    
    def current_player(self):
        return self.players[self.current_player_idx]
    
    def draw_dice(self, n):
        if len(self.dice_cup) < n:
            self.reset_dice_cup()
        return [self.dice_cup.pop() for _ in range(n)]
    
    def play_round(self):
        player = self.current_player()
        player.reset_turn()
        footprints = []
        dice_in_hand = self.draw_dice(3)
        
        while True:
            results = [die.roll() for die in dice_in_hand]
            player.record_roll(results)
            
            new_footprints = [die for die, res in zip(dice_in_hand, results) if res == 'footprint']
            footprints.extend(new_footprints)
            
            if player.turn_shotguns >= 3:
                player.end_turn(False)
                return False
            
            game_state = GameState(
                player,
                dice_in_hand,
                len(self.dice_cup) + len(footprints)
            )
            
            if not player.decide_continue(game_state):
                success = player.turn_shotguns < 3
                player.end_turn(success)
                return success
            
            dice_in_hand = footprints + self.draw_dice(3 - len(footprints))
            footprints = []
    
    def play_game(self, max_rounds=100):
        for _ in range(max_rounds):
            for i in range(len(self.players)):
                self.current_player_idx = i
                self.play_round()
                
                if any(p.brains >= 13 for p in self.players):
                    return self.get_winner()
        
        return self.get_winner()
    
    def get_winner(self):
        return max(self.players, key=lambda p: p.brains)

def simulate_tournament():
    bot_classes = [CowardlyBot, CautiousBot, BalancedBot, RecklessBot, StatisticalBot]
    bots = [cls(f"{cls.__name__} {i+1}") for i, cls in enumerate(bot_classes)]
    
    results = {bot.name: 0 for bot in bots}
    
    for game_num in range(100):
        random.shuffle(bots)
        game = ZombieDiceGame(bots.copy())
        winner = game.play_game()
        results[winner.name] += 1
        print(f"Game {game_num+1}: {winner.name} wins!")
    
    print("\nTournament Results:")
    for name, wins in sorted(results.items(), key=lambda x: -x[1]):
        print(f"{name}: {wins} wins")

if __name__ == "__main__":
    print("Zombie Dice Bot Tournament Simulation")
    simulate_tournament()
