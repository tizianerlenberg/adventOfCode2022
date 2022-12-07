from puzzle import ptext

fullList=ptext.split('\n')

def between(num,a,b):
    if a < num and num < b: 
        return True
    else: 
        return False

def charToInt(myChar):
    ascii = ord(myChar)
    if(between(ascii, 96, 123)):
        return ascii - 96
    if(between(ascii, 64, 91)):
        return ascii - 38

def getRemaining(myList):
    tmp=[]
    for item in myList:
        tmp.append([*item])
    
    tmp2=tmp[0]
    result=tmp2.copy()
    
    for item in tmp[1:]:
        for item2 in tmp2:
            #print(item2)
            if item2 not in item:
                try:
                    result.remove(item2)
                except:
                    pass
    return result

def part1():
    list1= []
    list2= []
    listRemain= []
    listRemainVal = []
    mySum=0

    for item in fullList:
        list1.append(item[:int(len(item)/2)])
    for item in fullList:
        list2.append(item[int(len(item)/2):])

    for i, item in enumerate(list1):
        listRemain.append([])
        for item2 in item:
            if(item2 in list2[i]):
                if(item2 not in listRemain[i]):
                    listRemain[i].append(list(item2)[0])

    #listRemain.append([list('z')[0]])

    for item in listRemain:
        listRemainVal.append(charToInt(item[0]))

    for item in listRemainVal:
        if(item):
            mySum = mySum + item
    
    print(fullList)
    print()
    print(list1)
    print()
    print(list2)
    print()
    print(listRemain)
    print()
    print(listRemainVal)
    print()
    print(mySum)

def part2():
    groupedList=[]
    remainingList=[]


    for intI, i in enumerate(range(0, len(fullList), 3)):
        groupedList.append([])
        for i2 in range(i, i+3):
            if len(fullList) > i2:
                groupedList[intI].append(fullList[i2])
        
    for item in groupedList:
        print(item)
        print()
        remainingList.append(getRemaining(item))
        pass


    #print(fullList)
    print()
    #print(groupedList)
    print()
    print(remainingList)
    #print(getRemaining(['halot', 'welt', 'welt']))

    mySum=0

    for i in remainingList:
        mySum = mySum + charToInt(i[0])
    print(mySum)

part2()






