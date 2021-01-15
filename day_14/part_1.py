#!/usr/bin/env python3

def binary_string(decimal:int)->str:
    return_string = ""
    for i in range(35, -1, -1):
        if 2**i <= decimal:
            return_string += '1'
            decimal -= 2**i
        else:
            return_string += '0'
    return return_string

def apply_mask(value:str, mask:str)->int:
    value = list(value)
    for i in range(36):
        # If the bit is unmarked, skip.
        if mask[i] == 'X':
            continue
        value[i] = mask[i]
    return ''.join(value)

def main():
    with open("input.txt") as f:
        memory = {}
        for line in f:
            line = line.strip()
            syntax = line.split(" = ")
            if syntax[0] == "mask":
                mask = syntax[1]
            else:
                address = syntax[0].split('[')[1].strip(']')
                binary_value = binary_string(int(syntax[1]))
                masked_binary = apply_mask(binary_value, mask)
                memory[address] = int(masked_binary, 2)
    print(sum(memory.values()))


if __name__ == "__main__":
    main()