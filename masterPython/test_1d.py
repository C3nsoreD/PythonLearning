from ds import Array2D
from ds import Array

import random


if __name__ == "__main__":
    ##  Testing Array functionaliry
    with open("tests/input00.txt", 'r') as f:
        lines = f.read().strip()
        # Use my array to count the number of occurances.
        my_counts = Array(len(lines) + 5)
        my_counts.clear(0)  # initializes with 0s

        for line in lines:
            num = ord(line)
            my_counts[num] += 1 
    
    for i in range(26):
        print(
            f"{chr(97 + i)}, {my_counts[97 + i]} "
        )
        