from timeit import timeit as my_timer
import cProfile

"""№1 с использованием решета Эратосфена"""


def test_foo(foo):
    arr = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    for i in range(len(arr)):
        if arr[i] == foo(i + 1):
            print(f'все ок значение в pos {(i + 1)} == {arr[i]}')


def ero_1(pos):
    SIZE = 10 * 1000
    arr = [i for i in range(SIZE)]
    arr[1] = 0
    for i in range(2, len(arr)):
        if arr[i] != 0:
            j = i * 2
            while j < len(arr):
                arr[j] = 0
                j += i
    arr = [i for i in arr if i != 0]

    return arr[pos - 1]
    del arr


# print(f'для функции ero_1 c решетом Эратосфена == {ero_1(2)}')
test_foo(ero_1)

print(my_timer('ero_1(2)', number=5, globals=globals()))  # 0.0350955
print(my_timer('ero_1(5)', number=5, globals=globals()))  # 0.028800499999999993
print(my_timer('ero_1(10)', number=5, globals=globals()))  # 0.03386779999999999
print(my_timer('ero_1(20)', number=5, globals=globals()))  # 0.036306599999999994
cProfile.run('ero_1(5)')
# 24299    0.003    0.000    0.003    0.000 {built-in method builtins.len}
# так же видно наполнение стека вызовов len
# оптимизировал -  del arr))
# сложность квадратичная O(n**2)
# скорость  способа №1 в 10 раз больше чем №2
# =======================================================================
"""№2 без решета Эратосфена"""


def ero_2(position):
    SIZE = 10 * 1000
    arr = [i for i in range(SIZE)]
    value = 2
    arr[1] = 0
    while value < arr[-1]:
        i = 0
        while i < len(arr):
            if arr[i] % value == 0 and arr[i] != value:
                arr.pop(i)
            i += 1
        for j in range(len(arr)):
            if arr[j] > value:
                value = arr[j]
                break
    return arr[position - 1]


# print(f'для функции ero_2 без решета Эратосфена == {ero_2(2)}')
# test_foo(ero_2)
# print(my_timer('ero_2(2)', number=5, globals=globals()))  # 2.9540117
# print(my_timer('ero_2(5)', number=5, globals=globals()))  # 2.6180329999999996
# print(my_timer('ero_2(10)', number=5, globals=globals()))  # 2.953104800000001
# print(my_timer('ero_2(20)', number=5, globals=globals()))  # 2.565106199999999
# cProfile.run('ero_2(5)')

#    1524927    0.177    0.000    0.177    0.000 {built-in method builtins.len}
# (слабое звено  в месте наполнения стека вызовов встроенной функции len, как я понимаю)
# 8771    0.004    0.000    0.004    0.000 {method 'pop' of 'list' objects} - и так же вызовы pop()
# сложность выглядит как O(n**3), потому number=5 - комп не потянул.
