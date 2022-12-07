from puzzle import ptext
import sys

list1=ptext.split('\n')

list2=[]
for item in list1:
    list2.append(item.split(','))

list3=[]
for item in list2:
    list3.append([])
    for item2 in item:
        tmpList=item2.split('-')
        tmpList2=[]
        for item3 in tmpList:
            tmpList2.append(int(item3))
        list3[-1].append(tmpList2)

def isBetween(myList):
    if myList[0][0] <= myList[1][0]:
        if myList[0][1] >= myList [1][1]:
            return True
    if myList[0][0] >= myList[1][0]:
        if myList[0][1] <= myList [1][1]:
            return True
    return False

def doesOverlap(myList):
    if myList[0][0] <= myList[1][0]:
        if myList[0][1] >= myList [1][0]:
            return True
    if myList[0][0] >= myList[1][0]:
        if myList[0][0] <= myList [1][1]:
            return True
    return False

acc=0

for item in list3:
    #print(item, isBetween(item))
    if isBetween(item):
        acc=acc+1

acc2=0

for item in list3:
    print(item, doesOverlap(item))
    if doesOverlap(item):
        acc2=acc2+1

"""
print()
print(list1)
print()
print(list2)
print()
print(list3)
"""
#print()
#print(acc)
print()
print(acc2)
