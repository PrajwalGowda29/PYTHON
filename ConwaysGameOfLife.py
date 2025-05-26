##Conways Game Of Life
print("Prajwal BR,USN:1AY24AI083,SEC:O")
import numpy as np
import time
import os
print("Prajwal BR\nUSN:1AY24AI083\nSec:O")

def console_game(size=20, generations=50, delay=0.5):
    grid = initialize_grid(size)
    
    for _ in range(generations):
        os.system('cls' if os.name == 'nt' else 'clear')
        print_grid(grid)
        grid = update_grid(grid)
        time.sleep(delay)

def print_grid(grid):
    for row in grid:
        print(' '.join(['■' if cell else ' ' for cell in row]))

if __name__ == "__main__":
    console_game()
