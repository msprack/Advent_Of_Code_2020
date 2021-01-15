#!/usr/bin/env python3
from math import sin, cos, radians, atan, hypot, pi
def main():
    # Start ship's coordinates at the origin
    ships_x = ships_y = 0
    # Set the waypoint's units to 10 east, 1 north
    way_x = 10
    way_y = 1
    instruction = 0
    # Open the file to be accessed as f
    with open("input.txt") as f:
        # Look at every line in f
        for line in f:
            line = line.strip()
            # Grab the action
            action = line[0]
            # Grab the input value
            value = int(line[1:])
            if action == 'N':
                way_y += value
            elif action == 'S':
                way_y -= value
            elif action == 'E':
                way_x += value
            elif action == 'W':
                way_x -= value
            elif action == 'L':
                # x is set to -y
                # y is set to x
                if value == 90:
                    temp = way_x
                    way_x = -1 * way_y
                    way_y = temp
                # x is set to -x
                # y is set to -y
                elif value == 180:
                    temp = way_x
                    way_x = -1 * way_x
                    way_y = -1 * way_y
                # x is set to y
                # y is set to -x
                elif value == 270:
                    temp = way_x
                    way_x = way_y
                    way_y = -1 * temp
            elif action == 'R':
                # x is set to y
                # y is set to -x
                if value == 90:
                    temp = way_x
                    way_x = way_y
                    way_y = -1 * temp
                # x is set to -x
                # y is set to -y
                elif value == 180:
                    way_x = -1 * way_x
                    way_y = -1 * way_y
                # x is set to -y
                # y is set to x
                elif value == 270:
                    temp = way_x
                    way_x = -1 * way_y
                    way_y = temp
            elif action == 'F':
                ships_x += way_x * value
                ships_y += way_y * value
    print(abs(ships_x) + abs(ships_y))
if __name__ == "__main__":
    main()