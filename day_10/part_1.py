#!/usr/bin/env python3

def main():
    # Open the input file as f
    with open("input.txt") as f:
        # Cast all input lines to integers and sort them
        adapters = sorted([int(i) for i in f.readlines()])
    # The outlet has a 0 value, initialize the ones count as 0
    ones = last_adapter = 0
    # Since the phone is always three above the highest, initialize the threes count as 1
    threes = 1
    # Look at every adapter, starting at the second
    for adapter in adapters:
        # Check if the gap is a one or a three. Increment the appropriate count.
        if adapter - last_adapter == 1:
            ones += 1
        elif adapter - last_adapter == 3:
            threes += 1
        # Set the last_adapter to the current adapter
        last_adapter = adapter
    print(ones * threes)
if __name__ == "__main__":
    main()