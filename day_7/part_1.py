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
                if "no other" in line:
                    continue
                # Split the line into the bag and the bags it can contain
                container, contained = line.split(" contain ")
                # Grab the container modifier and color
                container_shade = container.split(" bags")[0]
                # Split the contained bags into the contained segments     
                # Look at each contained segment
                for segment in contained.split(", "):
                    # Grab the color and modifier
                    segment_shade = segment.split()[1] + ' ' + segment.split()[2]
                    # Append the modified color to the value list
                    if segment_shade not in self.colors:
                        self.colors[segment_shade] = []
                    self.colors[segment_shade].append(container_shade)

    def get_color(self, color, first=True):
        # Set the count to 0
        count = 0
        # if the color is in found, return
        if color in self.found:
            return
        # Add the color to the found list
        if not first:
            self.found.append(color)
        # Look at every item in the color's list
        for shade in self.colors.get(color, []):
            self.get_color(shade, first=False)
        return count
    def get_gold(self)->int:
        return len(self.found)
if __name__ == "__main__":
    bags = Bags()
    bags.get_color("shiny gold")
    print(bags.get_gold())