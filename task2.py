# Написать программу, которая генерирует двумерный массив на A x B элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными методами подсчета суммы)

from random import randint
A = int(input('Введите кол-во столбцов: '))
B = int(input('Введите кол-во строк: '))

toy = [[0 for i in range(A)] for j in range(B)]

sum_toy = 0
midl_value_toy = 0
for i in range(A):
    for j in range(B):
        toy[i][j] = randint(1,9)

for i in range(A):
    for j in range(B):
        print(toy[i][j], end = '')
    print('')
print(' ')
for i in range(A):
    for j in range(B):
        sum_toy += toy[i][j]
        midl_value_toy = sum_toy / A
print(f'сумма элементов строки = {sum_toy}')
print(f'среднее значение элементов строки = {midl_value_toy}')