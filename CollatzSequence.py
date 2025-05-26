print("Prajwal BR\nUSN:1AY24AI083\nSec:O")
def collatz_sequence(n):
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:  
            n = n // 2
        else:           
            n = 3 * n + 1
    sequence.append(1)   
    return sequence

try:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        print("Please enter a positive integer.")
    else:
        seq = collatz_sequence(num)
        print(f"Collatz sequence for {num}:")
        print(seq)
        print(f"Length: {len(seq)} steps")
except ValueError:
    print("Invalid input. Please enter a positive integer.")
