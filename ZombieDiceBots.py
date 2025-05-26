print("Prajwal BR\nUSN:1AY24AI083\nSec:O")
import random
DICE = {
    'green': ['brain', 'brain', 'brain', 'shotgun', 'feet', 'feet'],
    'yellow': ['brain', 'brain', 'shotgun', 'shotgun', 'feet', 'feet'],
    'red': ['brain', 'shotgun', 'shotgun', 'shotgun', 'feet', 'feet']
}

DICE_COLORS = ['green', 'yellow', 'red']

class ZombieDiceBot:
    def __init__(self):
        self.brains = 0
        self.shotgun_blasts = 0
        self.feet = 0
        self.roll_count = 0

    def roll_dice(self, num_dice=3):
        """Roll dice and return the results"""
        dice = random.choices(DICE_COLORS, k=num_dice)
        results = []
        for die in dice:
            result = random.choice(DICE[die])
            results.append(result)
        return results

    def play_turn(self):
        """Simulate a bot turn"""
        while True:
            self.roll_count += 1
            print(f"\nTurn {self.roll_count}: Rolling dice...")
            results = self.roll_dice(3)
            print("Rolled results:", results)

            brains = results.count('brain')
            shotguns = results.count('shotgun')
            feet = results.count('feet')

            self.brains += brains
            self.shotgun_blasts += shotguns
            self.feet += feet

            print(f"Brains: {self.brains}, Shotguns: {self.shotgun_blasts}, Feet: {self.feet}")

            if self.shotgun_blasts >= 3:
                print("Bot got 3 shotgun blasts! Turn ends.")
                return False

            if self.brains >= 13:
                print("Bot has collected enough brains! Turn ends.")
                return True 
            
            if self.shotgun_blasts >= 2 or self.brains >= 4:
                print("Bot decides to stop rolling.")
                return True 

            print("Bot continues rolling...")

def simulate_game():
    bot = ZombieDiceBot()
    while True:
        if bot.play_turn():
            print(f"\nBot ends the turn. Final score: {bot.brains} brains, {bot.shotgun_blasts} shotguns.\n")
            break

simulate_game()
