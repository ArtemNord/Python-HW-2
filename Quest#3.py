#Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

Num = int(input('Введите число: '))
i = 2
flag = True

while flag:
    if Num % i == 0:
        print(i)
        flag = False
    i += 1