a = int(input('input a    '))
b = int(input('input b    '))
c = int(input('input c    '))

if a > b:
    print('Свершилось!')
elif b > a:
    print("Да ну!")
else:
    print("А если так?")
    a = a + c
    b = b - c
    if a > b:
        print('Свершилось!')
    else:
        print("Да ну!")

while a < b:
    print("Пока что нет")
    print(a)
    a = a + c
print("Дождались!")
print(a)
