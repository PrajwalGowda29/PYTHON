#coinflip
import random
print("Prajwal BR\nUSN:1AY24AI083\nSec:O")
def simulate_coin_flips(num_flips=100):
    """Simulate a series of coin flips and return the results"""
    return [random.choice(['H', 'T']) for _ in range(num_flips)]

def count_streaks(flips):
    """Count streaks of heads or tails in the flip sequence"""
    streaks = []
    current_streak = 1
    
    for i in range(1, len(flips)):
        if flips[i] == flips[i-1]:
            current_streak += 1
        else:
            streaks.append(current_streak)
            current_streak = 1
    streaks.append(current_streak) 
    
    return streaks

def analyze_streaks(streaks):
    """Analyze and display streak statistics"""
    max_streak = max(streaks)
    avg_streak = sum(streaks) / len(streaks)
    long_streaks = sum(1 for s in streaks if s >= 6)  
    
    print(f"\nStreak Analysis:")
    print(f"Total flips: {sum(streaks)}")
    print(f"Number of streaks: {len(streaks)}")
    print(f"Longest streak: {max_streak}")
    print(f"Average streak length: {avg_streak:.2f}")
    print(f"Number of streaks ≥6: {long_streaks}")

def display_flips(flips, per_line=20):
    """Display the flips in a readable format"""
    print("\nCoin Flip Sequence:")
    for i in range(0, len(flips), per_line):
        print(' '.join(flips[i:i+per_line]))

def main():
    print("Coin Flip Streak Analyzer")
    try:
        num_flips = int(input("How many flips to simulate? (default 100): ") or 100)
        if num_flips <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input. Using default 100 flips.")
        num_flips = 100
    
    flips = simulate_coin_flips(num_flips)
    streaks = count_streaks(flips)
    
    display_flips(flips)
    analyze_streaks(streaks)

if __name__ == "__main__":
    main()
