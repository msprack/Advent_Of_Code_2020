#!/usr/bin/env python3

class Node:
    def __init__(self):
        self.children = []
    def add_child_rule(self, child_rule):
        self.children.append(child_rule)
    def find_match(self, sentence, indices=[0]):
        # Need some way of working with indices across children
        # Only once a child is completed should anything be added to the return indices
        # Need to validate index
        # print(indices)
        original = indices
        return_indices = []
        # Go through the sub_rule node lists one by one
        for child in self.children:
            # Temp indices resets to original indices
            temp_indices = indices.copy()
            # Evaluate the attached nodes
            for element in child:
                # If the element is a string, fill a secondary temp list and set the temp list accordingly
                if type(element) == str:
                    temp_temp_indices = []
                    for index in temp_indices:
                        # print(index)
                        if index != len(sentence) and element == sentence[index]:
                            temp_temp_indices.append(index + 1)
                    temp_indices = temp_temp_indices
                # Otherwise, temp list becomes the result of recursive call
                else:
                    temp_indices = element.find_match(sentence, temp_indices)
            return_indices += (temp_indices)
        return return_indices

def main():
    # count starts at 0
    total = 0
    # A dictionary associating ID's to child nodes
    language = {}
    # Initially process the rules into the language dictionary
    with open("input.txt") as f:
        # Evaluate rules in file
        for line in f:
            line = line.strip()
            # An empty line marks the end of the rules
            if line == "":
                break
            rule_id, rules = line.split(": ")
            rules = rules.split(" | ")
            if rule_id not in language:
                language[rule_id] = Node()
            for rule in rules:
                child = []
                for element in rule.split():
                    if element.startswith('"'):
                        element = element[1]
                    else:
                        if element not in language:
                            language[element] = Node()
                        element = language[element]
                    child.append(element)
                language[rule_id].add_child_rule(child)
        # Starter is rule 0
        starter_rule = language["0"]
        total = 0
        for line in f:
            line = line.strip()
            indices = starter_rule.find_match(line)
            for index in indices:
                if index == len(line):
                    total += 1
                    break
        print(total)
if __name__ == "__main__":
    main()