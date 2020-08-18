"""
Задание_3.	В массиве случайных целых чисел поменять
местами минимальный и максимальный элементы.

"""
import random

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 1000
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
mii = array[0]
maa = array[1]
imi = 0
ima = 0
for i in range(len(array)):
    if array[i] < mii:
        mii = array[i]
        imi = i
    elif array[i] > maa:
        maa = array[i]
        ima = i
array[imi], array[ima] = array[ima], array[imi]
# print(mii, maa, imi, ima, sep='\n')
print(f'В данном массиве чисел максимальное число   {maa} стоит \n'
      f' на {imi} позиции, а минимальное число  {mii} стоит \n'
      f'на   {ima} позиции:  {array}')