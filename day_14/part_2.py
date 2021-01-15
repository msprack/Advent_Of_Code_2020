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

def apply_mask(value:str, mask:str)->list:
    # Convert value string to a list for mutability
    value = list(value)
    mask = list(mask)
    for i in range(36):
        if mask[i] == '1':
            value[i] = '1'
        elif mask[i] == 'X':
            # Recurse on two versions of the memory address and place the elements of their lists side by side
            mask[i] = '0'
            value[i] = '0'
            return_value = apply_mask(''.join(value), mask)
            value[i] = '1'
            return_value += apply_mask(''.join(value), mask)
            # Return the results
            return return_value
    # Base case: if we reached the end, return a singular entry in a list
    return [str(int(''.join(value), 2))]
        

def main():
    with open("input.txt") as f:
        # Store the memory values with the address as a key
        memory = {}
        for line in f:
            line = line.strip()
            syntax = line.split(" = ")
            if syntax[0] == "mask":
                mask = syntax[1]
            else:
                address = int(syntax[0].split('[')[1].strip(']'))
                binary_address = binary_string(address)
                binary_value = binary_string(int(syntax[1]))
                masked_addresses = apply_mask(binary_address, mask)
                for iter_address in masked_addresses:
                    memory[iter_address] = int(binary_value, 2)
                
    print(sum(memory.values()))


if __name__ == "__main__":
    main()