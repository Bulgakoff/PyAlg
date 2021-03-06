"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.

ЧЕРЕЗ РЕКУРСИЮ
"""


def foo1(n):
    if n <= 1:
        return n
    else:
        return n + foo1(n - 1)


def foo2(n):
    return n * (n + 1) / 2


num = int(input('Введите любое натуральное число: '))

if foo2(num) == foo1(num):
    print(f'для множества натуральных чисел выполняется равенство:'
          f' 1+2+...+n = n(n+1)/2 , в данном случае {foo1(num)}')
else:
    print('для множества натуральных чисел равенство не выполняется ')
