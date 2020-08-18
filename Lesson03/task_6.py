"""
Задание_6.	В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Их самих  в сумму не включать.

"""
import random

SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

mii = array[0]
maa = array[1]
imi = 0
ima = 0
sum_ = 0
for i in range(len(array)):
    if array[i] < mii:
        mii = array[i]
        imi = i
    elif array[i] > maa:
        maa = array[i]
        ima = i
if ima < imi:
    for i in range(ima + 1, imi):
        sum_ += array[i]
elif imi < ima:
    for i in range(imi + 1, ima):
        sum_ += array[i]

print(f'Сумма элементов между минимальным ({mii})  '
      f'и максимальным ({maa}) элементами: {sum_}')
