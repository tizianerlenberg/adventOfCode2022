from puzzle import ptext
from copy import copy, deepcopy

set=ptext.split('\n')

#STACKS

for item in set:
    pass
    #print(item)
#print()

stacks = []

for i in range(9):
    stacks.append([])

for i in range(7, -1, -1):
    for otherI, i2 in enumerate(range(1,37,4)):
        item = list(set[i][i2])[0]
        if item != list(' ')[0]:
            stacks[otherI].append(item)

for i, item in enumerate(stacks):
    pass
    #print(f"{i+1} {item}")
#print()

#INSTRUCTIONS

instructions=[]

for item in set[10:]:
    tmp= item.split(' ')
    instructions.append([int(tmp[1]),int(tmp[3]),int(tmp[5])])

#print(instructions)
#print()

def part1(myStacks, myInstructions):
    for instruction in myInstructions:
        for i in range(instruction[0]):
            #print(f"popping from {instruction[1]-1} to {instruction[2]-1}")
            item = myStacks[instruction[1]-1].pop()
            myStacks[instruction[2]-1].append(item)
    return myStacks

def part2(myStacks, myInstructions):
    for instruction in myInstructions:
        tmpList=[]
        for i in range(instruction[0]):
            #print(f"popping from {instruction[1]-1} to {instruction[2]-1}")
            item = myStacks[instruction[1]-1].pop()
            tmpList.append(item)
        for i in range(instruction[0]):
            item = tmpList.pop()
            myStacks[instruction[2]-1].append(item)
    return myStacks

myNewStacks = part2(deepcopy(stacks), deepcopy(instructions))

for i, item in enumerate(myNewStacks):
    print(f"{i+1} {item}")
print()
