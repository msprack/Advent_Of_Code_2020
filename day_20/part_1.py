#!/usr/bin/env python3
import math

def main():
    tiles = {}
    edges = {}
    corners = []
    id = None
    with open("input.txt") as f:
        # Assemble a dictionary with tile IDs as keys and tiles as values
        # Look at every line in the file:
        for line in f:
            line = line.strip()
            # If the line is blank, set the previous line to the bottom edge
            # And populate the dictionary entry
            if line == "":
                bottom_edge = previous_line
                tiles[id] = [top_edge, bottom_edge, left_edge, right_edge]
                # Log each edge in the dictionary
                for edge in tiles[id]:
                    rev = ''.join(reversed(edge))
                    # If the edge exists unreversed, append id
                    if edge in edges:
                        edges[edge].append(id)
                    elif ''.join(reversed(edge)) in edges:
                        edges[rev].append(id)
                    else:
                        edges[edge] = [id]
            # If the line starts with a tile, strip the : and split on space
            elif line.startswith("Tile"):
                id = line.strip(':').split()[1]
                left_edge = ""
                right_edge = ""
            else:
                # If this is the first line in the tile, set it as the top edge
                if previous_line.startswith("Tile"):
                    top_edge = line
                # Add the left-hand character to the left-hand edge string
                left_edge += line[0]
                # Add the right-hand character to the right-hand edge string
                right_edge += line[-1]
                # Store the current line as the last line
            previous_line = line
        # Go through every tile and assess whether it was a corner.
        for tile, tile_edges in tiles.items():
            shared = 0
            for edge in tile_edges:
                rev = ''.join(reversed(edge))
                if edge in edges:
                    neighbors = edges[edge]
                else:
                    neighbors = edges[rev]
                if len(neighbors) == 2:
                    shared += 1
            if shared == 2:
                corners.append(tile)
        print(math.prod([int(corner) for corner in corners]))
if __name__ == "__main__":
    main()