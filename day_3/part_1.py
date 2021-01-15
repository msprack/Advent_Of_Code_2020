#!/usr/bin/env python3

def main():
    # Open the input file, refer to it as f
    with open("input.txt") as f:
        # Intialize the tree count at 0
        trees = 0
        # Create a line number starting at 0, this will be used to
        # determine the x coordinate in every line
        line_number = 0
        # Look at every line in the file
        for line in f:
            # Remove trailing newlines
            line = line.strip()
            # Generate the x coordinate according to the given slope
            x_coordinate = line_number * 3
            # since the pattern is repeating we can use a modulus to find 
            # the index of the x_coordinate in the line
            x_index = x_coordinate % len(line)
            if line[x_index] == '#':
                trees += 1
            line_number += 1
        print(trees)

if __name__ == "__main__":
    main()