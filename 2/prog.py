from puzzle import ptext

class G():
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    LOSE = 1
    DRAW = 2
    WIN = 3


inputList=ptext.split('\n')
list1=[]
list2=[]

for item in inputList:
    match item[0]:
        case 'A':
            list1.append(1)
        case 'B':
            list1.append(2)
        case 'C':
            list1.append(3)
        case other:
            raise

for item in inputList:
    match item[2]:
        case 'X':
            list2.append(1)
        case 'Y':
            list2.append(2)
        case 'Z':
            list2.append(3)
        case other:
            raise


def part1():
    acc=0

    for item in list2:
        acc = acc + item

    print(f"Accumulator: {acc}")

    for i, item in enumerate(list2):
        match list1[i]:
            case G.ROCK:
                match item:
                    case G.ROCK:
                        acc=acc+3
                    case G.PAPER:
                        acc=acc+6
                    case G.SCISSORS:
                        acc=acc+0
            case G.PAPER:
                match item:
                    case G.ROCK:
                        acc=acc+0
                    case G.PAPER:
                        acc=acc+3
                    case G.SCISSORS:
                        acc=acc+6
            case G.SCISSORS:
                match item:
                    case G.ROCK:
                        acc=acc+6
                    case G.PAPER:
                        acc=acc+0
                    case G.SCISSORS:
                        acc=acc+3
            case other:
                raise

    print(f"Accumulator: {acc}")

def part2():
    acc=0

    for i, item in enumerate(list2):
        match list1[i]:
            case G.ROCK:
                match item:
                    case G.LOSE:
                        acc=acc+0
                        acc=acc+3
                    case G.DRAW:
                        acc=acc+3
                        acc=acc+1
                    case G.WIN:
                        acc=acc+6
                        acc=acc+2
            case G.PAPER:
                match item:
                    case G.LOSE:
                        acc=acc+0
                        acc=acc+1
                    case G.DRAW:
                        acc=acc+3
                        acc=acc+2
                    case G.WIN:
                        acc=acc+6
                        acc=acc+3
            case G.SCISSORS:
                match item:
                    case G.LOSE:
                        acc=acc+0
                        acc=acc+2
                    case G.DRAW:
                        acc=acc+3
                        acc=acc+3
                    case G.WIN:
                        acc=acc+6
                        acc=acc+1
            case other:
                raise

    print(f"Accumulator: {acc}")

part2()
