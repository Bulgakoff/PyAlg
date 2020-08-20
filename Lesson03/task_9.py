"""
Задание_9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.

"""
from random import randint



SIZE = 4
MIN_ITEM = -100
MAX_ITEM = 100
array = [[randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]
print(array)

# array = []
# for i in range(3):
#     inter = []
#     for j in range(4):
#         inter.append(randint(1, 99))
#     array.append(inter)

for i in range(len(array)):
    for j in range(len(array[i])):
        print(f'{array[i][j]:4}', end=' ')
    print()

min_coll_lst = []
for i in range(len(array[1])):
    min_coll_el = array[2][i]
    for j in range(len(array)):
        if array[j][i] < min_coll_el:
            min_coll_el = array[j][i]
    min_coll_lst.append(min_coll_el)
print(f'{min_coll_lst} минимальные значения по столбцам')

max_from_min =min_coll_lst[0]
for h in range(len(min_coll_lst)):
    if max_from_min < min_coll_lst[h]:
        max_from_min = min_coll_lst[h]

print(f'Максимальное  среди них = {max_from_min}')