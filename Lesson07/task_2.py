import random
"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

arr_start = [round(random.uniform(0, 50), 2) for _ in range(10)]
print(f'------начало-------{arr_start}')


def del_merge(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        del_merge(left)
        del_merge(right)

        i = 0
        j = 0
        s = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[s] = left[i]
                i += 1
                s += 1
            else:
                arr[s] = right[j]
                j += 1
                s += 1
        while i < len(left):
            arr[s] = left[i]
            i += 1
            s += 1
        while j < len(right):
            arr[s] = right[j]
            j += 1
            s += 1
        return arr


print(f'--------конец----------{del_merge(arr_start)}')
