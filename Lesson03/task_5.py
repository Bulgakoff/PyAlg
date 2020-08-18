"""
Задание_5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве.
"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
min_el = array[0]
min_ind = 0
max_min_ind = 0
max_min_el = min_el
for i in range(len(array)):
    if min_el > array[i]:
        min_el = array[i]
        min_ind = i
    if array[i] < 0:
        if max_min_el < array[i]:
            max_min_el = array[i]
            max_min_ind = i

print(f'Максимальный отрицательный элемент в данном массиве = {max_min_el},'
      f' его индекс {max_min_ind}')

# вариант №2 =====================================================
max_min_ind = 0
max_min_el = array[3]

for i in range(len(array)):
    if 0 > array[i] > array[max_min_ind]:
        max_min_ind = i
        max_min_el = array[i]
print(f'Максимальный  отрицательный элемент в данном массиве = '
      f'{max_min_el}, его индекс {max_min_ind}')
