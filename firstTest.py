'''
 конкатенация строк
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
 конкатенация строк
'''
S1 = 'First word '
S2 = 'second word!'
print(S1 + S2)
