"""
Задание_4. Определить, какое число в массиве встречается чаще всего

"""
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 5
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
# array = [11, 0, 11, 8,8,8,8,8, 13]
print(array)
max_count = 0
max_ind = 0
for i in range(len(array)):
    ccc = 0
    j = i + 1
    for j in range(len(array)):
        if array[i] == array[j]:
            ccc += 1
    if max_count < ccc:
        max_count = ccc
        max_ind = i

print(f'число {array[max_ind]} в массиве встречается чаще, всего {max_count} раз(а))')
