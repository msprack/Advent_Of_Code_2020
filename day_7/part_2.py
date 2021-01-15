#!/usr/bin/env python3
class Bags:
    found = []
    colors = {}
    def __init__(self):
        # Open the file herefor to be called f
        with open("input.txt") as f:
            # Look at every line in the file
            for line in f:
                line = line.strip()
                line = line.strip(".")
                # Split the line into the bag and the bags it can contain
                container, contained = line.split(" contain ")
                # Grab the container modifier and color
                container_shade = container.split(" bags")[0]
                if container_shade not in self.colors:
                    self.colors[container_shade] = []
                # Split the contained bags into the contained segments     
                # Look at each contained segment
                for segment in contained.split(", "):
                    # Grab the color and modifier
                    segment_shade = segment.split()[1] + ' ' + segment.split()[2]
                    # Grab the number of segment_shade bags contained
                    if segment.split()[0] == "no":
                        number_contained = 0
                    else:
                        number_contained = int(segment.split()[0])
                    # Append the modified color and number to the value list
                    if segment_shade not in self.colors[container_shade]:
                        self.colors[container_shade]
                        self.colors[container_shade].append((segment_shade, number_contained))

    # Take in a bag and the number of them that exist. If this is the original query, don't count the containing bag
    def get_color(self, color, number, first=True)->int:
        # If number is 0, return 0
        if number == 0:
            return 0
        # Set the count to one for the current bag
        count = number
        # If this is the first, don't count it
        if first:
            count = 0
        # Look at each contained_color and contained_number in the associated list
        for contained_color, contained_number in self.colors[color]:
            # Add contained_color times the result of contained_color to the number
            count += number * self.get_color(contained_color, contained_number, first=False)
        return count

if __name__ == "__main__":
    bags = Bags()
    print(bags.get_color("shiny gold", 1))