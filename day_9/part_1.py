#!/usr/bin/env python3

def main():
    # Open the input file and store contents in a single list
    with open("input.txt") as f:
        xmas = f.readlines()
    # Look at every index starting at 25
    for i in range(25, len(xmas)):
        # Escape the loop through a raised exception when the addends are found
        try:
            # Look at the 25 previous entries
            for j in range(i-25, i):
                    # Look the entries between this one and i
                    for k in range(j, i):
                        # If one adds up, raise StopIteration
                        if int(xmas[j].strip()) + int(xmas[k].strip()) == int(xmas[i].strip()):
                            raise StopIteration
            # If the for loop ends without raising an exception, print i and return
            print(xmas[i].strip())
            return
        except StopIteration:
            pass

if __name__ == "__main__":
    main()