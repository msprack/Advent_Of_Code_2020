#!/usr/bin/env python3

def main():
    # Read the tickets file
    with open("input.txt") as f:
        rules = {}
        # Some flags to track the state of the program:
        in_rules = True
        in_tickets = False
        # Error rate starts at 0
        error_rate = 0
        # An empty list of potential field descriptions
        for line in f:
            line = line.strip()
            # Manage state transitions
            if line == "":
                continue
            elif line == "your ticket:":
                in_rules = False
                continue
            elif line == "nearby tickets:":
                in_tickets = True
                continue
            
            # Read in the rules with the descriptions as keys and a list of tuples as the bounds
            if in_rules:
                description = line.split(": ")[0]
                bounds = line.split(": ")[1].split(" or ")
                bound_list = []
                for bound in bounds:
                    bound1, bound2 = bound.split('-')
                    bound_list.append((bound1, bound2))
                rules[description] = bound_list
            elif not in_tickets:
                my_fields = line.split(',')
            else:
                ticket_fields = line.split(',')
                # Loop through the indices of ticket fields
                for field in ticket_fields:
                    # Use exceptions to avoid checking unneccesary rules
                    try:
                        for bound_list in rules.values():
                            for bound1, bound2 in bound_list:
                                if int(bound1) <= int(field) <= int(bound2):
                                    raise StopIteration
                        # If we get to this line, no rule applied to this value and it is in error
                        error_rate += int(field)
                    except StopIteration:
                        pass
        print(error_rate)

if __name__ == "__main__":
    main()