'''
 task 1
'''
import random
cycleStartValue = 0
list1 = []
while cycleStartValue <= 10:
    list1.append(random.randint(1, 100))
    cycleStartValue = cycleStartValue + 1
print(list1)
list1.pop()
print(list1)

'''
 task 2
'''
S1 = 'this is '
S2 = 'how it works'
print(S1 + S2)
S3 = 'this is '
S4 = 'how it works'
S5 = S3+S4
print(S5)

'''
task 3
'''
one = 8
two = 5
three = 13
four = 25
print((one+two)*three)
print(four*10-two)
print(three/two)
print(four-three)
