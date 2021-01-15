#!/usr/bin/env python3

def evaluate(iterator):
    times_stack = []
    number_stack = []
    try:
        add = None
        operand_string = ''
        last_character = ' '
        character = next(iterator)
        # Go until failure or return
        while True:
            # If we hit a parenthetical, evaluate it
            if character == '(':
                # Set it to the operand_string
                operand_string = evaluate(iterator)
            # If we hit the end of the current parenthetical, handle remaining operations and return result
            elif character == ')':
                if add:
                    number_stack.append(number_stack.pop() + int(operand_string))
                    add = False
                else:
                    number_stack.append(int(operand_string))
                # Clear out the multiplication stack
                while len(times_stack) > 0:
                    times_stack.pop()
                    number_stack.append(number_stack.pop() * number_stack.pop())
                # Return the final result
                return number_stack.pop()
            # If the character is a number, process it as part of an operand
            elif character.isdigit():
                if last_character == ' ':
                    operand_string = character
                else:
                    operand_string += character
            # If we hit an addition operation, set add flag true and append to add stack
            elif character == '+':
                add = True
            # If we hit a multiplication operation set add flag false and append to times stack
            elif character == '*':
                add = False
                times_stack.append('*')
            # If we hit a space and the last character was not an operator
            elif character == ' ' and last_character != '+' and last_character != '*':
                # If we are right of an add, add and push new value, pop an add, add becomes false
                if add:
                    number_stack.append(number_stack.pop() + int(operand_string))
                    add = False
                # If we are not on the right of an add, append operand to number stack
                else:
                    number_stack.append(int(operand_string))
                operand_string = ''
            # Track the previous character
            last_character = character
            # Move on to the current character
            character = next(iterator)

    except StopIteration:
        # Handle any last minute additions and operands
        if add:
            number_stack.append(number_stack.pop() + int(operand_string))
            add = False
        else:
            number_stack.append(int(operand_string))
    # Clean up multiplication
    while len(times_stack) > 0:
        times_stack.pop()
        number_stack.append(number_stack.pop() * number_stack.pop())
    # Return the final result
    return number_stack.pop()

def main():
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            total += evaluate(iter(line))
    print(total)

if __name__ == "__main__":
    main()