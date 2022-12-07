from puzzle import ptext
from copy import copy, deepcopy

ptextCopy=ptext
#ptextCopy="mjqjpqmgbljsphdztnvjfqwrcgsmlb"


def isUnique(seq):
    seqList=list(seq)
    return len(set(seqList)) == len(seqList)

def part1():
    for i in range(len(ptextCopy)-3):
        print(i, ptextCopy[i:i+4], isUnique(ptextCopy[i:i+4]))
        if isUnique(ptextCopy[i:i+4]):
            print(f"Number is {i+4}")
            break

def part2():
    for i in range(len(ptextCopy)-3):
        print(i, ptextCopy[i:i+14], isUnique(ptextCopy[i:i+14]))
        if isUnique(ptextCopy[i:i+14]):
            print(f"Number is {i+14}")
            break

part2()