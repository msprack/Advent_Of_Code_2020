#!/usr/bin/env python3
from math import sin, cos, radians
def main():
    # Start coordinates at the origin, facing east
    ships_x = ships_y = orientation = 0
    # Open the file to be accessed as f
    with open("input.txt") as f:
        # Look at every line in f
        for line in f:
            # Grab the action
            action = line[0]
            # Grab the input value
            value = int(line[1:-1])
            if action == 'N':
                ships_y += value
            elif action == 'S':
                ships_y -= value
            elif action == 'E':
                ships_x += value
            elif action == 'W':
                ships_x -= value
            elif action == 'L':
                orientation = (orientation + value) % 360
            elif action == 'R':
                orientation = (orientation - value) % 360
            elif action == 'F':
                ships_x += int(value * cos(radians(orientation)))
                ships_y += int(value * sin(radians(orientation)))
    print(abs(ships_x) + abs(ships_y))
if __name__ == "__main__":
    main()