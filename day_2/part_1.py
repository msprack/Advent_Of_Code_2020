#!/usr/bin/env python3

def main():
    # Open input file
    with open("input.txt") as f:
        correct_count = 0
        # Look at every line in the file
        for line in f:
            # Ignore trailing newlines
            line = line.strip()
            # Split the line into policy, letter(with a trailing ':') and the password
            policy, letter, password = line.split()
            letter = letter.strip(":")
            low = int(policy.split("-")[0])
            high = int(policy.split("-")[1])
            if low <= password.count(letter) <= high:
                correct_count += 1
        print(correct_count)


if __name__ == "__main__":
    main()