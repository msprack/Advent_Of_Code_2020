#!/usr/bin/env python3

def main():
    # initialize the result as 1 to avoid zero multiplication
    result = 1
    # Open the input file, refer to it as f
    with open("input.txt") as f:
            # Grab all the lines for later use
            lines = f.readlines()
    for change_x, change_y in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2)):
        # Intialize the tree count at 0
        trees = 0
        # Create a line number starting at 0, this will be used to
        # determine the x coordinate in every line
        line_number = 0
        # Look at every line in the file
        for line_number in range(0, len(lines), change_y):
            # Remove trailing newlines
            line = lines[line_number].strip()
            # Generate the x coordinate according to the given slope
            x_coordinate = line_number * change_x
            # since the pattern is repeating we can use a modulus to find 
            # the index of the x_coordinate in the line
            x_index = x_coordinate % len(line)
            # 
            if line[x_index] == '#':
                trees += 1
            line_number += change_y
        result *= trees
    print(result)

if __name__ == "__main__":
    main()