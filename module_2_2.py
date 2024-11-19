print('Введите 3 числа для проверки на равенство')
first = int(input('первое число '))
second = int(input('второе число '))
third = int(input('третье число '))
if first == second and first == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)