print("Prajwal BR\nUSN:1AY24AI083\nSec:O")
def simple_zigzag(rows, length):
    for i in range(rows):
        line = []
        for j in range(length):
            if j % (rows * 2 - 2) == i or j % (rows * 2 - 2) == (rows * 2 - 2 - i):
                line.append("*")
            else:
                line.append(" ")
        print("".join(line))

# Example usage:
simple_zigzag(5, 30)
