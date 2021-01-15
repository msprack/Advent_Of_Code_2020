#!/usr/bin/env python3
import inspect
import itertools

class Node:
    def __init__(self, rule_id):
        self.children = []
        self.rule_id = rule_id
        self.literals = None
    def add_child_rule(self, child_rule):
        self.children.append(child_rule)

    def generate(self):
        # An empty list to be populated with sub rules and returned
        return_list = []
        # Evaluate each sub-rule
        for sub_rule in self.children:
            child_list = []
            # Look at the items in the sub_rule
            for i, item in enumerate(sub_rule):
                if type(item) == str:
                    return [item]
                # Initially populate list on first iteration
                if i == 0:
                    child_list += item.generate()
                # Replace list with all possible combinations of the list so far with results.
                else:
                    child_list = list(itertools.product(child_list, item.generate()))
                    child_list = [''.join(entry) for entry in child_list]
            return_list += child_list
        self.literals = return_list
        return return_list

    def find_match(self, sentence, indices=[0]):
        # Need some way of working with indices across children
        # Only once a child is completed should anything be added to the return indices
        # Need to validate index
        #print(visited)
        return_indices = []
        if self.rule_id == "8":
            new_indices = self.children[0][0].find_match(sentence, indices)
            return_indices += new_indices
            while new_indices:
                new_indices = self.children[0][0].find_match(sentence, new_indices)
                return_indices += new_indices
            return return_indices
        if self.rule_id == "11":
            # Indices for the first, non-recursive sub-rule
            temp_indices = self.children[0][0].find_match(sentence, indices)
            temp_indices = self.children[0][1].find_match(sentence, temp_indices)
            return_indices += temp_indices
            # Indices for the recursive rule, the number of 42's must meet the number of 31's
            forty_two = {}
            thirty_one = {}
            for i in itertools.count(1):
                if i == 1:
                    forty_two['1'] = self.children[1][0].find_match(sentence, indices)
                else:
                    forty_two[str(i)] = self.children[1][0].find_match(sentence, forty_two[str(i-1)])
                if not forty_two[str(i)]:
                    break
                for j in range(i):
                    if j == 0:
                        thirty_one[str(i)] = self.children[1][2].find_match(sentence, forty_two[str(i)])
                    else:
                        thirty_one[str(i)] = self.children[1][2].find_match(sentence, thirty_one[str(i)])
            # Process the thirty one indices
            for l in thirty_one.values():
                for index in l:
                    if index not in return_indices:
                        return_indices.append(index)
            return return_indices
        if self.literals != None:
            for index in indices:
                if index >= len(sentence):
                    continue
                for literal in self.literals:
                    if sentence[index:].startswith(literal):
                        return_indices.append(index + len(literal))
            return return_indices
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
                        if index != len(sentence) and element == sentence[index]:
                            temp_temp_indices.append(index + 1)
                    temp_indices = temp_temp_indices
                # Otherwise, temp list becomes the result of recursive call
                else:
                    temp_indices = element.find_match(sentence, temp_indices)
            return_indices += temp_indices
        return return_indices

def main():
    # count starts at 0
    total = 0
    # A dictionary associating ID's to child nodes
    language = {}
    # Initially process the rules into the language dictionary
    with open("input2.txt") as f:
        # Evaluate rules in file
        for line in f:
            line = line.strip()
            # An empty line marks the end of the rules
            if line == "":
                break
            rule_id, rules = line.split(": ")
            rules = rules.split(" | ")
            if rule_id not in language:
                language[rule_id] = Node(rule_id)
            for rule in rules:
                child = []
                for element in rule.split():
                    if element.startswith('"'):
                        element = element[1]
                    else:
                        if element not in language:
                            language[element] = Node(element)
                        element = language[element]
                    child.append(element)
                language[rule_id].add_child_rule(child)
        # Calculate values for 42 and 31
        language["42"].generate()
        language["31"].generate()
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