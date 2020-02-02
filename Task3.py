import random
from typing import List, Any, Union


def makeList(listLenght, maxVal):
    list = []
    var = 0
    while var < listLenght:
        list.append(random.randint(1, maxVal))
        var = var + 1
    return list



listLenght = int(input('input list lenght   '))
maxVal = int(input('input list max Value   '))

list1 = makeList(listLenght, maxVal)
list2 = makeList(listLenght, maxVal)

listIntersect = list(set(list1) & set(list2))

print(list1)
print(list2)
print(listIntersect)

for i in list1:
    if i > 7:
        print(i)






