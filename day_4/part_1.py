#!/usr/bin/env python3


class Passport:
    def __init__(self):
        self.fields = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False, "cid": False}
    def clear(self):
        self.fields = {"byr": False, "iyr": False, "eyr": False, "hgt": False, "hcl": False, "ecl": False, "pid": False, "cid": False}
    def validate(self):
        for field, present in self.fields.items():
            if field != "cid" and not present:
                return False
        return True
    def mark_field(self, field):
        self.fields[field] = True


def main():
    # Start the count of valid passports at 0
    valid_passports = 0
    # Create an passport object to represent the current passport
    passport = Passport()
    # Open the input file and provide aaccess to it as f
    with open("input.txt") as f:
        # Look at every line in f, representing the current line as f
        for line in f:
            # Strip the newline from the current line
            line = line.strip()
            # If the line is empty, check passport validity, clear the passport and continue to the next line
            if not line:
                if passport.validate():
                    valid_passports += 1
                passport.clear()
                continue
            # Check every entry on the current line
            for item in line.split():
                # Mark the field name as present
                passport.mark_field(item.split(":")[0])
    if (passport.validate()):
        valid_passports += 1
    # Print out the number of valdi passports
    print(valid_passports)

if __name__ == "__main__":
    main()