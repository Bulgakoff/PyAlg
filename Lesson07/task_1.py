import random
import timeit

"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).
"""

qwe = [random.randint(-100, 100) for _ in range(5)]

print(qwe)

print('#1 ==============вариант ДЗ===============')


def qqq(arr):
    j = 1
    while j < len(arr):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        j += 1
    # print(arr)


# qqq(qwe)
print(timeit.timeit('qqq(qwe*5)', number=1000, globals=globals()))  # 0.14937809999999999
print(timeit.timeit('qqq(qwe*10)', number=1000, globals=globals()))  # 0.8505477000000001
print(timeit.timeit('qqq(qwe*20)', number=1000, globals=globals()))  # 1.9337297
print(timeit.timeit('qqq(qwe*30)', number=1000, globals=globals()))  # 4.4304722000000005
print(timeit.timeit('qqq(qwe*40)', number=1000, globals=globals()))  # 8.0174022
#
print('#2 ================flag=================================0')


#
#
def flag(arr):
    fl = True
    while fl:
        fl = False
        i = 0
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                fl = True
    # print(arr)


# flag(qwe)
print(timeit.timeit('flag(qwe*5)', number=1000, globals=globals()))  # 0.1100479
print(timeit.timeit('flag(qwe*10)', number=1000, globals=globals()))  # 0.48323360000000004
print(timeit.timeit('flag(qwe*20)', number=1000, globals=globals()))  # 1.6452176
print(timeit.timeit('flag(qwe*30)', number=1000, globals=globals()))  # 4.0659277
print(timeit.timeit('flag(qwe*40)', number=1000, globals=globals()))  # 7.0912823000000005
# Второй вариант с флагом быстрее №1, но медленнее чем №3
print('#3 ================improved_bobble=================================0')


#
def improved_bobble(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    # print(arr)


# improved_bobble(qwe)

print(timeit.timeit('improved_bobble(qwe*5)', number=1000, globals=globals()))  # 0.08841400000000021  #
print(timeit.timeit('improved_bobble(qwe*10)', number=1000, globals=globals()))  # 0.3100883000000003  #
print(timeit.timeit('improved_bobble(qwe*20)', number=1000, globals=globals()))  # 1.4584013999999996  #
print(timeit.timeit('improved_bobble(qwe*30)', number=1000, globals=globals()))  # 2.7925448000000017  #
print(timeit.timeit('improved_bobble(qwe*40)', number=1000, globals=globals()))  # 5.1088874  #

# №3 самый быстрый из вариантов благодаря невозврату в отсортирванную часть.
