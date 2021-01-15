#!/usr/bin/env python3

def find_noncomply(xmas: list)->int:
    # Look at every index starting at 25
    for i in range(25, len(xmas)):
        # Escape the loop through a raised exception when the addends are found
        try:
            # Look at the 25 previous entries
            for j in range(i-25, i):
                    # Look the entries between this one and i
                    for k in range(j, i):
                        # If one adds up, raise StopIteration
                        if xmas[j] + xmas[k] == xmas[i]:
                            raise StopIteration
            # If the for loop ends without raising an exception, print i and return
            return xmas[i]
            break
        except StopIteration:
            pass

def main():
    # Open the input file and store contents in a single list
    with open("input.txt") as f:
        xmas = [ int(number.strip()) for number in f ]
    noncomply = find_noncomply(xmas)
    # Start with the first index at 0 and the last at 1
    first = 0
    last = 1
    while True:
        # Add the elements from first through last
        total = sum(xmas[first:last + 1])
        # Make the range larger if the total is smaller than noncomply
        if total < noncomply:
            last += 1
        # Increase the first index and reset the last to be one farther than the new first
        elif total > noncomply:
            first += 1
            last = first + 1
        # If the answer has been found, add the largest and smallest elements in the range
        else:
            big = max(xmas[first:last + 1])
            small = min(xmas[first:last + 1])
            print(big + small)
            break
        
    

if __name__ == "__main__":
    main()