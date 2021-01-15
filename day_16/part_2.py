#!/usr/bin/env python3

def main():
    # Read the tickets file
    with open("input.txt") as f:
        rules = {}
        # Some flags to track the state of the program:
        in_rules = True
        in_tickets = False
        # Count the number of valid tickets
        total_tickets = 0
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
                # Process the rules into a list of field descriptions that may apply to each field
                potential_fields = [ [] for i in rules.keys() ]
                for description in rules.keys():
                    for field in potential_fields:
                        field.append(description)
                in_tickets = True
                continue
            
            # Read in the rules with the descriptions as keys and a list of tuples containing the bounds as the values
            if in_rules:
                description = line.split(": ")[0]
                bounds = line.split(": ")[1].split(" or ")
                bound_list = []
                for bound in bounds:
                    bound1, bound2 = bound.split('-')
                    bound_list.append((bound1, bound2))
                rules[description] = bound_list
            # Read in our ticket value
            elif not in_tickets:
                my_fields = line.split(',')
            # Process the scanned tickets around us.
            else:
                total_tickets += 1
                ticket_fields = line.split(',')
                valid_fields = 0
                bad_ticket = False
                # Identify bad tickets that have any invalid fields and disregard them
                # Loop through the indices of ticket fields, applying the rules to each field until you find one that fits.
                # If none of the rules fit a field use bad_ticket to avoid processing
                for field in ticket_fields:
                    try:
                        for bound_list in rules.values():
                            for bound1, bound2 in bound_list:
                                if int(bound1) <= int(field) <= int(bound2):
                                    raise StopIteration
                        bad_ticket = True
                    except StopIteration:
                        pass
                    if bad_ticket:
                        break
                # Only process the good tickets
                if not bad_ticket:
                    # Using the indices to manage the possible field descriptions for each field, look at each field in the ticket
                    for i in range(len(ticket_fields)):
                        remove_list = []
                        # Look at each potential rule for that field, if the rule doesn't apply, remove it from the possibility list
                        for description in potential_fields[i]:
                            try:
                                for bound1, bound2 in rules[description]:
                                    if int(bound1) <= int(ticket_fields[i]) <= int(bound2):
                                        raise StopIteration
                                remove_list.append(description)
                            except StopIteration:
                                pass
                        j = 0
                        for removal in remove_list:
                            print("removing ", removal, " from ", i)
                            j+= 1
                            potential_fields[i].remove(removal)
        # Find the field that has a determined field description, remove it from other possibilities
        # Do this until no removals take place
        while True:
            removed = False
            for i in range(len(potential_fields)):
                if len(potential_fields[i]) == 1:
                    for j in range(len(potential_fields)):
                        if i == j:
                            continue
                        if potential_fields[i][0] in potential_fields[j]:
                            potential_fields[j].remove(potential_fields[i][0])
                            removed = True
            if not removed:
                break
        total = 1
        # Multiply all of the departure values together
        for i in range(len(potential_fields)):
            if potential_fields[i][0].startswith("departure"):
                total *= int(my_fields[i])
        print(total)

if __name__ == "__main__":
    main()