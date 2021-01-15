#!/usr/bin/env python3
def main():
    # Set up the accumulator at 0
    accumulator = 0
    # Get all of the lines in the input, store it in a list named instructions
    with open("input.txt") as f:
        instructions = f.readlines()
    # Create a visited list of Falses with as many slots as instructions
    visited = [False] * len(instructions)
    # instruction_pointer starts at 0
    instruction_pointer = 0
    # While the instruction has not been visited
    while not visited[instruction_pointer]:
        # set the instruction to visited
        visited[instruction_pointer] = True
        # grab the instruction and argument
        instruction, argument = instructions[instruction_pointer].strip().split()
        argument = int(argument)
        # If the instruction is jmp add the argument to the instruction_pointer
        if instruction == "jmp":
            instruction_pointer += argument
        # Else 
        else:
            # if the instruction is acc add the argument to the accumulator
            if instruction == "acc":
                accumulator += argument
            # increase the instruction pointer by one
            instruction_pointer += 1
    # Print the accumulator value
    print(accumulator)
if __name__ == "__main__":
    main()