#!/usr/bin/env python3

def generate_dict():
    return_dict = {}
    for i in range(ord("a"), ord("z") + 1):
        return_dict[chr(i)] = True
    return return_dict
def main():
    # Start the count at 0
    count = 0
    # Create an empty dictionary named questions
    questions = generate_dict()
    # Open the file, herefor to be referred to as f
    with open("input.txt") as f:
        # Look at every line in the file
        for line in f:
            line = line.strip()
            # If it is a newline, add the total of keys to count, clear the dictionary and continue.
            if line == "":
                count += len(questions.keys())
                questions = generate_dict()
                continue
            # Remove questions that aren't in the line
            temp = []
            delete_questions = [question for question in questions if question not in line]
            for question in delete_questions: del questions[question]
        # Add the total of keys to count, clear the dictionary and continue
        count += len(questions.keys())
        print(count)
if __name__ == "__main__":
    main()