#!/usr/bin/env python3

def main():
    # Holds all of the turn numbers for each number, keyed with strings, values are integers
    last_spoken = {}
    with open("small.txt") as f:
        # i tracks the turns, starting at one
        turn = 1
        # Read all of the starting numbers
        for item in f.readline().split(','):
            # They are spoken on this turn number
            last_spoken[item] = turn
            # Set the last number to this number since it was just spoken
            last_number = item
            # Increase the turn number
            turn += 1
        #TODO: find a formula to solve this sequence
        # Go up to 30000000, this takes a few seconds
        for turn in range(turn, 30000001):
            # Difference between the last turn and the previous time that number was spoken
            new_number = (turn - 1) - last_spoken.get(last_number, turn - 1)
            # Set the previous time of the last number to the last turn
            last_spoken[last_number] = turn - 1
            # The new number becomes spoken and is now the last number
            last_number = str(new_number)
    print(new_number)
main()