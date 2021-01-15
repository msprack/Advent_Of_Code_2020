#!/usr/bin/env python3
import queue
def evaluate(expression:str) -> int:
    # Create queues, 1 for working numerical values and 1 queue for stored operations.
    number_queue = queue.LifoQueue()
    operation_queue = queue.LifoQueue()
    # Split the expression into it's individual tokens which are separated by spaces
    tokens = expression.split()
    # Look at every token in our list of tokens:
    for token in tokens:
        beginning_parenthese = False
        ending_parenthese = False
        # If the token begins with a parenthese, We need to process the parenthetical expression as it's own expression
        if token.startswith('('):
            for _ in range(token.count("(") - 1):
                number_queue.put(0)
                operation_queue.put('+')
            token = token.lstrip('(')
            beginning_parenthese = True
        # If the token ends with a parenthese, we can perform the action listed before the beginning of the parenthetical expression
        if token.endswith(')'):
            end_parens = token.count(')')
            token = token.rstrip(')')
            ending_parenthese = True
        # If the token is a number, we can perform the previously listed operation with the last current working value
        if token.isdigit():
            # Check to see if there are no numbers in the queue. In which case, place this number directly in the queue
            if number_queue.empty() or beginning_parenthese:
                number_queue.put(int(token))
            # Otherwise, if the number queue has a working value, grab it, grab an operation to perform 
            # and perform the operation between the working value and the token
            else:
                # Grab the working number
                working_number = number_queue.get()
                # Grab the current operator
                operator = operation_queue.get()
                # If the operator is a plus sign, do addition
                if operator == '+':
                    result = working_number + int(token)
                # Otherwise if the operator is an asterisk, do multiplication
                elif operator == '*':
                    result = working_number * int(token)
                if ending_parenthese:
                    for i in range(end_parens):
                        if not operation_queue.empty():
                            operator = operation_queue.get()
                            old_value = number_queue.get()
                            if operator == '+':
                                result += old_value
                            # Otherwise if the operator is an asterisk, do multiplication
                            elif operator == '*':
                                result *= old_value
                # Push the result back onto the numbers queue
                number_queue.put(result)
        # If the token is an operator, we can store the operation to be performed
        elif token == '+' or token == '*':
            # Add the operator to the operations queue for later use
            operation_queue.put(token)
    temp = number_queue.get()
    if not (number_queue.empty() and operation_queue.empty()):
        print("Error")
    return temp
def main():
    total = 0
    with open("input.txt") as f:
        for line in f:
            line = line.strip()
            if line == "":
                continue
            total += evaluate(line)
    print(total)
if __name__ == "__main__":
    main()