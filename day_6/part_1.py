#!/usr/bin/env python3

def main():
    # Start the count at 0
    count = 0
    # Create an empty dictionary named questions
    questions = {}
    # Open the file, herefor to be referred to as f
    with open("input.txt") as f:
        # Look at every line in the file
        for line in f:
            line = line.strip()
            # If it is a newline, add the total of keys to count, clear the dictionary and continue.
            if line == "":
                count += len(questions.keys())
                questions = {}
                continue
            # Set each question in line to true
            for question in line:
                questions[question] = True
        # Add the total of keys to count, clear the dictionary and continue
        count += len(questions.keys())
        print(count)
if __name__ == "__main__":
    main()