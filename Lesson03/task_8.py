"""
Задание_8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.

"""
mmm = 5
nnn = 4
qwe = []
for i in range(mmm):
    inter = []
    for j in range(nnn):
        inter.append(3)
    qwe.append(inter)
print(qwe)

# вывод матрицы с суммой в строке #1 ====================
for i in range(len(qwe)):
    for j in range(len(qwe[i])):
        print(f'{qwe[i][j]:4}', end=' ')
    print(f'  ==>{sum(inter):4}')
    print()

# #2 ========================
for line in qwe:
    sum_line = 0
    for i, el in enumerate(line):
        sum_line += el
        print(f'{el:5}', end=' ')
    print(f'{sum_line:5}')
