"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

"""
num_rows = 5
num_cols = 4
matr = []
for i in range(1, num_rows + 1):
    inter = []
    print(f'{i}-я строка:')
    for j in range(1, num_cols+1):
        inter.append(int(input(f'введите {j} число {i}  строки ')))
    matr.append(inter)
print(matr)

# вывод матрицы с суммой в строке
for i in range(len(matr)):
    for j in range(len(matr[i])):
        print(f'{matr[i][j]:4}', end=' ')
    print(f'  ==>{sum(inter):4}')
    print()

# #2 ========================
for line in matr:
    sum_line = 0
    for i, el in enumerate(line):
        sum_line += el
        print(f'{el:5}', end=' ')
    print(f'{sum_line:5}')
