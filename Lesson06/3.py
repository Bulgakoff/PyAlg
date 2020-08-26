from random import randint
from memory_profiler import profile
import sys
import platform

print(f'разрядность интерпритатора и '
      f''
      f'ОС соответсвенно-->{platform.architecture()}')
print(f'Версия Python ---->{platform.python_version()}')
print(f'Расширение  ---->{platform.machine()}')
print('# вариант №3')
"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

"""


# Вариант №3

# @profile()
def qwe3():
    number = input('Введите целое число: ')
    print(f'start === {number}')
    revers = number[::-1]
    print(f'finish == {revers}')
    lst_var = [revers, number]
    return lst_var


lst = qwe3()
print(lst)


def show(ooo):
    print(f'тип объекта == {type(ooo)}, память == {sys.getsizeof(ooo)} байт, объект == {ooo} ')
    sum_memo = 0
    if hasattr(ooo, '__iter__'):
        if hasattr(ooo, 'items'):
            for key, item in ooo.items():
                show(key)
                show(item)
                sum_memo += sys.getsizeof(item)
                sum_memo += sys.getsizeof(key)
            sum_memo += sys.getsizeof(ooo)

        elif not isinstance(ooo, str):
            for p in ooo:
                show(p)
                sum_memo += sys.getsizeof(p)
            sum_memo += sys.getsizeof(ooo)

    return f'общая память == {sum_memo} байт '


print(show(lst))
# ('32bit', 'WindowsPE')
# Python 3.8.2
# Введите целое число: 123
# start === 123
# finish == 321
# ['321', '123']
# тип объекта == <class 'list'>, память == 36 байт, объект == ['321', '123']
# тип объекта == <class 'str'>, память == 28 байт, объект == 321
# тип объекта == <class 'str'>, память == 28 байт, объект == 123
# общая память == 92 байт

# Вывод: как не странно из всех вариантов получился самый экономичный вариант по памяти
