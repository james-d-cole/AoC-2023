# Import required packages
import re
from math import lcm, gcd

# Read input
with open('input.txt') as source_file:
    items = [x.rstrip('\n') for x in source_file]

# Extract details
nodes = {}
insts = [x.replace("L", "0").replace("R", "1") for x in items[0]]
for node in [re.findall(r'([A-Z0-9]{3})', x) for x in items[2::]]:
    nodes[node[0]] = [node[1], node[2]]

# Part 1
mvs, zzz, nod = 0, False, 'AAA'
while not zzz:
    for inst in insts:
        # print(f"Starting node: {nod}, instruction: {inst}, node: {nodes[nod]}, end node: {nodes[nod][int(inst)]}")
        nod = nodes[nod][int(inst)]
        mvs += 1
        if nod == 'ZZZ':
            zzz = True
            print(f"The answer to question 1 is {mvs}")

def map_node(node, inst, mvs):
    if type(node) == int:
        return node
    elif nodes[node][int(inst)][2] == 'Z':
        return mvs
    else:
        return nodes[node][int(inst)]


# Part 2
anod = [x for x in nodes.keys() if x[2] == 'A']
mvs = 0
zzz = False
while not zzz:
    for inst in insts:
        mvs += 1
        anod = [map_node(x, inst, mvs) for x in anod]
        if len([x for x in anod if type(x) == int]) == len(anod):
            zzz = True
lcm = 1
for i in anod:
    lcm = lcm*i//gcd(lcm, i)
print(f"The answer to question 2 is {lcm}")

