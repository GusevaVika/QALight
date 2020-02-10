a = int(input('введите число '))
b = int(input('введите число '))
c = int(input('введите число '))
d = int(input('введите число '))
def makeList(a, b, c, d):
    numbers = [a, b, c, d]
    print(numbers[0])
    print(numbers[3])
makeList(a, b, c, d)

'''вариант два'''
def lastFirst(string):
    list1 = []
    for i in list(string):
        list1.append(i)
    print(list1[0])
    print(list1[-1])

str = input('введите любые числа ')
lastFirst(str)

