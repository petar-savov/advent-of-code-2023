from itertools import cycle

with open("input-8.txt") as f:
    instruction_line, nodes = f.read().split("\n\n")
    nodes = nodes.strip().split("\n")


nodes = {node.split(" = ")[0]: node.split(" = ")[1].removeprefix("(").removesuffix(")") for node in nodes}


# Part 1
instructions = cycle(instruction_line)
c = 0
curr = "AAA"

while curr != "ZZZ":
    instr = next(instructions)
    elements = nodes[curr].split(", ")
    if instr == "L":
        curr = elements[0]
    elif instr == "R":
        curr = elements[1]
    c += 1

print(c)
