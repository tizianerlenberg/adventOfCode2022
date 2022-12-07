from puzzle import ptext

outList=[]

for item in ptext.split('\n\n'):
    acc=0
    for item2 in item.split('\n'):
        acc = acc + int(item2)
    outList.append(acc)

outList.sort()
print(outList[-1] + outList[-2] + outList[-3])
