#!/usr/bin/env python3

def calculate(partitioning:str)->int:
    result = 0
    # Iterate through the range of indices for the partitioning string
    for i in range(len(partitioning)):
        # With every element of the list, the minimum possible row has the potential to increase.
        # The potential increase starts at half of the number of items,
        # this can be represented as 2 to the power of one less than the length of the string.
        # Now, possible increase decrease by half each time the index increases
        # Until we are eventually left with two possible rows and a potential row increase of 1 decreases it
        # So, the powers we will raise 2 to will start at len(partitioning) - 1 and decrease by 1 with every iteration.
        # The final iteration will have an index of 6 and raise to a power of 0. Hence 2 ** (len(partitioning)-i).
        if partitioning[i] == 'B' or partitioning[i] == 'R':
            result += 2**((len(partitioning)-1) - i)
    return result

def main():
    # Start the max is None so we can tell if the loop is on its first iteration
    maximum = 0
    # Open the file to be accessed as f
    with open("input.txt") as f:
        # Look at every line in the file
        for line in f:
            line = line.strip()
            # Store the row number as row
            row = calculate(line[:7])
            # Store the column number as column
            column = calculate(line[7:])
            # Seat id is the row times the column plus the column
            seat_id = row * 8 + column
            maximum = max(maximum, seat_id)
    print(maximum)

if __name__ == "__main__":
    main()