#!/usr/bin/env python3

def copy_seats(seats:list)->list:
    copy = []
    for i in range(len(seats)):
        copy.append([])
        for seat in seats[i]:
            copy[i].append(seat)
    return copy

def occupied(seats:list, row:int, column:int, x_direction:int, y_direction:int)->bool:
    row = row + y_direction
    column = column + x_direction
    if 0 <= row < len(seats) and 0 <= column < len(seats[row]):
        return seats[row][column] == '#'
    else:
        return False

def main():
    # Grab the input from the file
    with open("input.txt") as f:
        # Create a two dimensional list of all the seats
        seats = [list(line.strip()) for line in f]
    # Declare a variable to hold the previous arrangement of seats
    last_seats = None
    # directions is used to decrease, maintain or increase position along an axis
    directions = [-1, 0, 1]
    # Do until the seats are the same as they were before the last iteration
    while seats != last_seats:
        # Make a copy of the last seat arrangement
        last_seats = copy_seats(seats)
        # Look at every row in the seating space
        for i in range(len(seats)):
            # Look at every seat in the row
            for j in range(len(seats[i])):
                if last_seats[i][j] == '.':
                    continue
                occupied_count = 0
                free = last_seats[i][j] == "L"
                # Decrease, maintain and increase row number
                for y_direction in directions:
                    # Decrease, maintain and increase column number
                    for x_direction in directions:
                        # Don't check self
                        if x_direction == 0 and y_direction == 0:
                            continue
                        # Increase occupied count if the seat adjacent is occupied
                        occupied_count += 1 if occupied(last_seats, i, j, x_direction, y_direction) else 0

                # If the seat is free and all adjacent spots empty, it becomes occupied
                if free and occupied_count == 0:
                    seats[i][j] = '#'
                # If a seat is occupied and 4 or more seats are occupied it becomes empty
                elif (not free) and occupied_count >= 4:
                    seats[i][j] = 'L'
    occupied_count = 0
    for row in seats:
        for seat in row:
            occupied_count += 1 if seat == '#' else 0
    print(occupied_count)

if __name__ == "__main__":
    main()