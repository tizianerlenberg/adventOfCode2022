from puzzle import ptext
import sys
from copy import copy, deepcopy

def myPrint(*args, **kwargs):
    if len(sys.argv) > 1:
        if sys.argv[1] == 'debug':
            print(*args, **kwargs)

class Path():
    def __init__(self, rootDir):
        self.rootDir=rootDir
        self.innerPath=[]
    def cd(self, pathString):
        match pathString:
            case '/':
                self.innerPath = []
            case '..':
                self.innerPath.pop()
            case _:
                self.innerPath.append([pathString, 
                                       self.getDir().getDir(pathString)])
    def getDir(self):
        if not self.innerPath:
            return self.rootDir
        return self.innerPath[-1][1]

class Dir():
    def __init__(self):
        self.container={}
    def getSize(self):
        result=0
        if not self.container:
            return 0
        for item in self.container.values():
            result = result + item.getSize()
        return result
    def getDir(self, dirName):
        return self.container[dirName]
    def put(self, name, obj):
        self.container[name] = obj
    def delete(self, name):
        self.container.pop(name)
    def meetsReq1(self):
        if self.getSize() <= 100000:
            return True
        return False
    def getSubDirs(self):
        result = []
        for name, item in self.container.items():
            if isinstance(item, Dir):
                result.append([name, item])
        return result
    def getAllSubDirs(self):
        result = []
        for name, item in self.container.items():
            if isinstance(item, Dir):
                result.append([name, item])
                result.extend(item.getAllSubDirs())
        return result
    def getAllSubDirsReq1(self):
        result = []
        for name, item in self.container.items():
            if isinstance(item, Dir):
                if item.meetsReq1():
                    result.append([name, item])
                    result.extend(item.getAllSubDirs())
                else:
                    result.extend(item.getAllSubDirsReq1())
        return result

class File():
    def __init__(self, size):
        self.size=size
    def getSize(self):
        return self.size

def parse(myInput):
    myPath = Path(Dir())
    
    for item in myInput:
        match item.split(' '):
            case ['$', 'ls']:
                myPrint('ls')
            case ['$', 'cd', directory]:
                myPrint('cd', directory)
                myPath.cd(directory)
            case ['dir', directory]:
                myPrint('dir', directory)
                myPath.getDir().put(directory, Dir())
            case [*fileData]:
                myPrint('file', fileData[1], fileData[0])
                myPath.getDir().put(fileData[1], File(int(fileData[0])))
    myPath.cd('/')
    return myPath

def part1(myPath):
    myPrint('#######################')
    myPath.cd('/')
    theDirs=myPath.getDir().getAllSubDirsReq1()
    acc=0
    for item in theDirs:
        myPrint(item[0])
        acc=acc+item[1].getSize()
    return acc

def part2(myPath):
    myPrint('#######################')
    myPath.cd('/')

    """
    theDirs=myPath.getDir().getAllSubDirs()
    theSizes=[]
    for item in theDirs:
        theSizes.append([item[0], item[1].getSize()])
    theSizes2=[]
    for item in theSizes:
        theSizes2.append(item[1])
        
    listOfSizes= theSizes2
    listOfSizes.sort()
    """

    used=myPath.getDir().getSize()
    total=70000000
    free=total-used
    
    required=30000000
    tofree=required-free
    
    myPrint(tofree)

    #################################

    theDirs=myPath.getDir().getAllSubDirs()
    theSizes={}
    for item in theDirs:
        theSizes[item[1].getSize()]= item[0]
    #myPrint(theSizes)

    listOfSizes= list(theSizes.keys())
    listOfSizes.sort()
    myPrint(listOfSizes)

    theSizeToFree=0

    for item in listOfSizes:
        if item >= tofree:
            theSizeToFree = item
            myPrint(theSizeToFree)
            break
    myPrint(theSizes[theSizeToFree])
    return theSizeToFree

def main():
    myInput = ptext.split('\n')
    
    myPrint(myInput)
    myPrint()
    
    myPath = parse(myInput)
    
    print(f"Answer for Part 1: {part1(myPath)}")
    print(f"Answer for Part 2: {part2(myPath)}")

if __name__ == '__main__':
    main()
