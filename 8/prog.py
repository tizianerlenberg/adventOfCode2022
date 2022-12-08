from puzzle import ptext
import sys
from copy import copy, deepcopy

def debug(*args, **kwargs):
    if len(sys.argv) > 1:
        if sys.argv[1] == 'debug':
            print(*args, **kwargs)

class Forest():
    def __init__(self):
        self.rows=[]
        self.colls=[]
        self.nRows=0
        self.nColls=0
    def parse(self, text):
        lines=text.split('\n')
        
        for item in lines:
            self.rows.append([])
            for item2 in list(item):
                self.rows[-1].append(int(item2))
        self.nRows=len(self.rows)
        self.nColls=len(self.rows[0])
        debug(self.rows)

        for item in self.rows[0]:
            self.colls.append([])

        for i, item in enumerate(self.rows):
            for i2, item2 in enumerate(item):
                self.colls[i2].append(item2)
        debug(self.colls)
    def getTop(self, x, y):
        tmp = deepcopy(self.colls[x][:y])
        tmp.reverse()
        return tmp
    def getBottom(self, x, y):
        return self.colls[x][y+1:]
    def getLeft(self, x, y):
        tmp = deepcopy(self.rows[y][:x])
        tmp.reverse()
        return tmp
    def getRight(self, x, y):
        return self.rows[y][x+1:]
    def isVisible(self, x, y):
        ownVal=self.colls[x][y]
        checks=0

        for item in self.getTop(x,y):
            if item >= ownVal:
                checks = checks +1
                break
        for item in self.getBottom(x,y):
            if item >= ownVal:
                checks = checks +1
                break
        for item in self.getLeft(x,y):
            if item >= ownVal:
                checks = checks +1
                break
        for item in self.getRight(x,y):
            if item >= ownVal:
                checks = checks +1
                break
        if checks >= 4:
            return False
        return True
    def getScore(self, x, y):
        ownVal=self.colls[x][y]
        scoreTop=0
        scoreBottom=0
        scoreLeft=0
        scoreRight=0

        debug('###############')
        debug(self.getTop(x,y))
        for i, item in enumerate(self.getTop(x,y)):
            if item < ownVal:
                scoreTop=i+1
            else:
                scoreTop=i+1
                break
        debug(self.getBottom(x,y))
        for i, item in enumerate(self.getBottom(x,y)):
            if item < ownVal:
                scoreBottom=i+1
            else:
                scoreBottom=i+1
                break
        debug(self.getLeft(x,y))
        for i, item in enumerate(self.getLeft(x,y)):
            if item < ownVal:
                scoreLeft=i+1
            else:
                scoreLeft=i+1
                break
        debug(self.getRight(x,y))
        for i, item in enumerate(self.getRight(x,y)):
            if item < ownVal:
                scoreRight=i+1
            else:
                scoreRight=i+1
                break
        debug(f'top: {scoreTop}')
        debug(f'bottom: {scoreBottom}')
        debug(f'left: {scoreLeft}')
        debug(f'right: {scoreRight}')
        debug('###############')
        return scoreTop * scoreBottom * scoreLeft * scoreRight

def part1(f):
    acc=0
    for x in range(f.nColls):
        for y in range(f.nRows):
            if f.isVisible(x,y):
                acc=acc+1
    return acc

def part2(f):
    maxVal=0
    for x in range(f.nColls):
        for y in range(f.nRows):
            score= f.getScore(x,y)
            if score > maxVal:
                maxVal = score
            debug(f'x: {x}, y: {y}, score: {score}')
    return maxVal

def main():
    myInput = ptext
    myInput2=r"""
30373
25512
65332
33549
35390"""[1:]
    f = Forest()
    f.parse(myInput)
    debug(f.isVisible(1,1))
    
    print(f"Answer for Part 1: {part1(f)}")
    print(f"Answer for Part 2: {part2(f)}")

if __name__ == '__main__':
    main()
