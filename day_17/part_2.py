#!/usr/bin/env python3

def main():
    # Dictionary with keys as x,y,z. Presence indicates active
    active = {}
    with open("input.txt") as f:
        # Baseline position
        x=0
        y=0
        z=0
        w=0
        for line in f:
            line = line.strip()
            if line == '':
                continue
            for cube in line:
                if cube == '#':
                    active[(x, y, z, w)] = '#'
                x+=1
            y += 1
            x=0
        #print(active)
        # Simulate the necessary rounds
        for round_number in range(6):
            # Coordinates are still keys, but values are the number of active neighbors
            tabulation = active.copy()
            # Mark the number of active neighbors for every neighbor of an active cube
            for active_cube in active:
                x, y, z, w = active_cube
                # All possible neighbors relative to current cube
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        for k in range(-1, 2):
                            for l in range(-1, 2):
                                # Skip self, so you aren't your own neighbor
                                if not (i == 0 and j == 0 and k == 0 and l == 0):
                                    # Add 1 to the neighbor, if it hasn't been set yet set to one
                                    temp = tabulation.get((x+i, y+j, z+k, w+l), 0)
                                    temp = 0 if temp == '#' else temp
                                    tabulation[(x+i, y+j, z+k, w+l)] = temp + 1
            #print(tabulation)
            #return
            for cube, number in tabulation.items():
                # If cube is inactive and does not have 2 to 3 active neighbors, deactivate
                if cube in active and not (number == 2 or number == 3):
                    # Deactivate by removing from the active dictionary
                    active.pop(cube)
                # If cube is inactive has three active neighbors, make cube active
                if (cube not in active) and number == 3:
                    # Cube is made active by adding to the active dictionary
                    active[cube] = '#'
        print(len(active))


                
if __name__ == "__main__":
    main()