#!/usr/bin/env python3

def main():
    # Open the input file as f
    with open("input.txt") as f:
        # Cast all input lines to integers and sort them
        adapters = sorted([int(i) for i in f.readlines()])
    # Establish a list of paths from each element
    possibility_list = [0] * (len(adapters) + 1)
    # Add an element 0 to the beginning
    adapters.insert(0, 0)
    # Set the value of the rear to 1
    possibility_list[len(possibility_list) - 1] = 1
    # Starting from the rear, add the value of the current element to every element within 3 of it
    for i in range(len(possibility_list) - 1, 0, -1):
        for j in range(i-1, -1, -1):
            print(i, j)
            if adapters[i] - adapters[j] > 3:
                break
            else:
                possibility_list[j] += possibility_list[i]
    # print the value of possibilities at 0
    print(possibility_list[0])
if __name__ == "__main__":
    main()