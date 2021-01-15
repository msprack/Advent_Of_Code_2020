#!/usr/bin/env python3
from math import log, gcd, ceil, floor
def main():
    # Open the file
    with open("input.txt") as f:
        # Grab the timestamp
        timestamp = int(f.readline().strip())
        # Grab the values of the list
        entries = f.readline().strip().split(',')
        # Find valid numbers starting with the second one
        i = 1
        smaller_val = int(entries[0])
        cycle_length = smaller_val
        max_cycle = cycle_length
        while i < len(entries):
            # Mind the gap
            gap = 1
            while i < len(entries) and entries[i] == 'x':
                i += 1
                gap += 1
            # Later val is found
            later_val = int(entries[i])
            # Until we find a good value:
            smaller_multiplier = 0
            while True:
                small_test = int(smaller_val + cycle_length * smaller_multiplier)
                # Set the later multiplier to that which is required to exceed the smaller_val + gap
                later_multiplier = ceil((small_test + gap) / later_val)
                # Candidate is itself times the later multiplier
                candidate = later_val * later_multiplier
                # If candidate - gap equals smaller_val plus (cycle_length times smaller_multiplier):
                if candidate - gap == small_test:
                    print("here")
                    # Set the cycle length
                    print(cycle_length)
                    # Cycle length is the least common multiple of the current cycle length and the later multiplicand
                    cycle_length = int((cycle_length * later_val) / gcd(cycle_length, later_val))
                    # Set the smaller value to the candidate value
                    smaller_val = candidate
                    # Escape the loop
                    break
                smaller_multiplier += 1
            # Increase the value of i
            i += 1
        print(smaller_val - len(entries) + 1)
        
if __name__ == "__main__":
    main()