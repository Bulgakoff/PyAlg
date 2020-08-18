"""
Задание_7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.

"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
fel = array[0]
fii = 0
sel = array[1]
sii = 1
for i in range(len(array)):
    if array[i] < fel:
        fel = array[i]
        fii = i
j = 0
while j < len(array):
    if array[j] != fel:
        if sel > array[j]:
            sel = array[j]
    j += 1
print(f'Первый Наименьший элемент: {fel} ,'
      f' Второй наименьший элемент: {sel} ')
