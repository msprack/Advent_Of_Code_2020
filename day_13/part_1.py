#!/usr/bin/env python3
from math import log
def main():
    # Open the file
    with open("input.txt") as f:
        # Grab the timestamp
        timestamp = int(f.readline().strip())
        # Grab the line, stripped
        line = f.readline().strip()
        # Declare a smallest valid time
        smallest_time = None
        # Declare a currently selected bus
        selected_bus = None
        # Loop through the entries
        for entry in line.split(","):
            # If entry is an x, skip
            if entry == 'x':
                continue
            entry = int(entry)
            # Integer divide the timestamp by entry and multiply by entry
            rough_product = timestamp // entry * entry
            # If the product matches the timestamp print and return
            if rough_product == timestamp:
                print(entry)
            # Add element to the product and subtract timestamp.
            first_valid = rough_product + entry
            # if smallest valid is none, or is larger than this one, set it to this one
            if smallest_time == None or smallest_time > first_valid:
                smallest_time = first_valid
                selected_bus = entry
        print(selected_bus * (smallest_time - timestamp))
if __name__ == "__main__":
    main()