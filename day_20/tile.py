class Tile:
    def __init__(self, id:str, lines:list):
        self.assigned = False
        self.lines = lines
        self.id = id
        self.top = lines[0]
        self.bottom = lines[-1]
        self.left = ""
        self.right = ""
        for line in lines:
            self.left += line[0]
            self.right += line[-1]
    def rotate(self, degrees:int):
        degrees = degrees % 360
        if degrees == 0:
            return
        if degrees % 90 != 0:
            raise ValueError
        self.left = ""
        self.right = ""
        for _ in range(0, degrees, 90):
            new_lines = [['' for _ in range(len(self.lines))] for _ in range(len(self.lines[0])) ]
            # i represents the row number of the character
            for i, line in enumerate(self.lines):
                # j represents the column number of the character
                for j, character in enumerate(line):
                    # Set the slot at 
                    new_lines[j][len(line) - i - 1] = character
        self.lines = []
        for line in new_lines:
            new_line = ''.join(line)
            self.lines.append(new_line)
            self.left += new_line[0]
            self.right += new_line[-1]
        self.top = self.lines[0]
        self.bottom = self.lines[-1]
    def flip_vertical(self):
        # Switch lines along the vertical axis
        self.lines = list(reversed(self.lines))
        self.left = ""
        self.right = ""
        for line in self.lines:
            self.left += line[0]
            self.right += line[-1]
        self.top = self.lines[0]
        self.bottom = self.lines[-1]

    def flip_horizontal(self):
        for i, line in enumerate(self.lines):
            self.lines[i] = ''.join(reversed(line))
        self.left = ""
        self.right = ""
        for line in self.lines:
            self.left += line[0]
            self.right += line[-1]
        self.top = self.lines[0]
        self.bottom = self.lines[-1]
    def get_edges(self)->dict:
        return {"top": self.top, "right": self.right, "bottom": self.bottom, "left": self.left}
    def __str__(self):
        return ''.join([l + '\n' for l in self.lines])