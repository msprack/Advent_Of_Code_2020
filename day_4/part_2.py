#!/usr/bin/env python3

# Passport class to represent the current state
class Passport:
    # List of valid eye color strings
    eyes = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    # All fields start as False
    def __init__(self):
        self.byr = False
        self.iyr = False
        self.eyr = False
        self.hgt = False
        self.hcl = False
        self.ecl = False
        self.pid = False
        self.cid = False
    # Reset all fields to initial state
    def clear(self):
        self.byr = False
        self.iyr = False
        self.eyr = False
        self.hgt = False
        self.hcl = False
        self.ecl = False
        self.pid = False
        self.cid = False
    # Set a field to a value
    def set_field(self, field:str, value:str)->None:
        if field == "byr":
            self.byr = value
        elif field == "iyr":
            self.iyr = value
        elif field == "eyr":
            self.eyr = value
        elif field == "hgt":
            self.hgt = value
        elif field == "hcl":
            self.hcl = value
        elif field == "ecl":
            self.ecl = value
        elif field == "pid":
            self.pid = value
        elif field == "cid":
            self.cid = value
    
    def validate_birth(self)->bool:
        return self.byr and (len(self.byr) == 4 and self.byr.isdigit() and 1920 <= int(self.byr) <= 2002)

    def validate_issue(self)->bool:
        return self.iyr and (len(self.iyr) == 4 and self.iyr.isdigit() and 2010 <= int(self.iyr) <= 2020)

    def validate_expiration(self)->bool:
        return self.eyr and (len(self.eyr) == 4 and self.eyr.isdigit() and 2020 <= int(self.eyr) <= 2030)

    def validate_height(self)->bool:
        if self.hgt and len(self.hgt) >= 4:
            units = self.hgt[-2:]
            number = int(self.hgt[:-2])
        return self.hgt and len(self.hgt) >= 4 and ((units == "cm" and 150 <= number <= 193) or (units == "in" and 59 <= number <= 76))

    def validate_hair(self)->bool:
        if self.hcl:
            try:
                int(self.hcl[1:], 16)
                is_hex = True
            except:
                is_hex = False
        return self.hcl and is_hex and self.hcl[0] == "#"

    def validate_eyes(self):
        return self.ecl and self.ecl in self.eyes

    def validate_passportID(self):
        return self.pid and self.pid.isdigit() and len(self.pid) == 9

    def validate(self)->bool:
        return (self.validate_birth() and self.validate_issue() and self.validate_expiration() and 
        self.validate_height() and self.validate_hair() and self.validate_eyes() and self.validate_passportID())



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
                field, value = item.split(":")
                print(field, value)
                # Set the value of the field
                passport.set_field(field, value)
    # Check the last passport
    if (passport.validate()):
        valid_passports += 1
    # Print out the number of valid passports
    print(valid_passports)

if __name__ == "__main__":
    main()