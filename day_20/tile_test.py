#!/usr/bin/env python3
from tile import Tile

def main():
    tiles = {}
    edges = {}
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if line.startswith("Tile"):
                id = line.strip(':').split()[1]
                lines = []
            elif line == '':
                tiles[id] = Tile(id, lines)
                # Populate the edges
                for edge in tiles[id].get_edges():
                    rev = ''.join(reversed(edge))
                    if edge in edges:
                        edges[edge].append(id)
                    elif rev in edges:
                        edges[rev].append(id)
                    else:
                        edges[edge] = [id]
            else:
                lines.append(line)
    # Now to arrange the picture.
    # First, assemble the corners
    corners = []
    for id, tile in tiles:
        total = 0
        for edge in tile.get_edges():
            if len(edges[edge]) == 2:
                total += 2
if __name__ == "__main__":
    main()