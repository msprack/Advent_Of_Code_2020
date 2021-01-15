#!/usr/bin/env python3

def greater_than(one, two):
    f = [int(i) for i in one.split(',')]
    l = [int(i) for i in two.split(',')]
    for i in [2, 1, 0]:
        if f[i] > l[i]:
            return True
    return False

def sort_cubes(cubes):
    if len(cubes) == 1:
        return cubes
    # print("Called one")
    l1 = sort_cubes(cubes[:len(cubes)//2])
    # print("Called two")
    l2 = sort_cubes(cubes[len(cubes)//2:])
    return_val = []
    low_index = 0
    high_index = 0
    while not (low_index == len(l1) and high_index == len(l2)):
        if high_index < len(l2) and (low_index == len(l1) or greater_than(l1[low_index], l2[high_index])):
            return_val.append(l2[high_index])
            high_index += 1
        else:
            return_val.append(l1[low_index])
            low_index += 1
            return l1 + l2
def draw_picture(cubes:dict)->None:
    # Sort the dict by row, then column then shelf
    sorted_list = sort_cubes(list(cubes))
    first_x, first_y, first_z = sorted_list[0]
    low_x = high_x = first_x
    low_y = high_y = first_y
    low_z = high_z = first_z
    for cube in sorted_list:
        x, y, z = cube
        low_x = min(low_x, x)
        high_x = max(high_x, x)
        low_y = min(low_y, y)
        high_y = max(high_y, y)
        low_z = min(low_z, z)
        high_z = max(high_z, z)
    for z in range(low_z, high_z + 1):
        print(f"\n Z = {z}\n")
        for y in range(low_y, high_y + 1):
            for x in range(low_x, high_x + 1):
                if f'{x},{y},{z}' in cubes:
                    print('#', end='')
                else:
                    print('.', end='')
            print()



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
                    active[(x, y, z)] = '#'
                x+=1
            y += 1
            x=0
        #print(active)
        # Simulate the necessary rounds
        for round_number in range(6):
            # Coordinates are still keys, but values are the number of active neighbors
            # Seed the dictionary with the active cubes to prevent zero-neighbor active cube blindspots
            tabulation = active.copy()
            # Mark the number of active neighbors for every neighbor of an active cube
            for active_cube in active:
                x, y, z = active_cube
                # All possible neighbors relative to current cube
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        for k in range(-1, 2):
                            # Skip self, so you aren't your own neighbor
                            if not (i == 0 and j == 0 and k == 0):
                                # Add 1 to the neighbor, if it hasn't been set yet set to one
                                temp = tabulation.get((x+i, y+j, z+k), 0)
                                temp = 0 if temp == '#' else temp
                                tabulation[(x+i, y+j, z+k)] = temp + 1
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
            if False and (round_number == 2 or round_number == 3):
                draw_picture(active)
                print(len(active))
        print(len(active))


                
if __name__ == "__main__":
    main()