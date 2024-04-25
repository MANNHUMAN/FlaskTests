'''
for i in range(101):
    result=''
    if i==0:
        print('0')
        continue
    if i%3==0:
        result+='Fizz'
    if i%5==0:
        result+='Buzz'
    if result!='':
        print(result+'!')
    else:
        print(i)
'''
import random
numList=[]
for _ in range(6):
    numList.append(random.randint(1,10))
targetNum=random.randint(1,15)
correctNums=[]
for x in numList:
    for y in numList:
        if x+y==targetNum:
            correctNums.append([x,y])
print(numList)
print(targetNum)
if len(correctNums)==0:
    print('No correct combinations')
else:
    print(correctNums)