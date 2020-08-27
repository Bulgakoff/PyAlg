from random import randint
from memory_profiler import profile
import sys
import platform

print(f'разрядность интерпритатора и '
      f''
      f'ОС соответсвенно-->{platform.architecture()}')
print(f'Версия Python ---->{platform.python_version()}')
print(f'Расширение  ---->{platform.machine()}')
"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

"""
# Вариант №1

print('# вариант 1')


# @profile()
def qwe1():
    MIM_N = 10
    MAX_N = 1000
    num = randint(MIM_N, MAX_N)
    print(f'start === {num}')
    revers = 0
    while num > 0:
        revers = revers * 10 + num % 10
        num = num // 10
    print(f'finish == {revers}')
    lst_var = [MIM_N, MAX_N, revers, num]

    return lst_var
    #
    del revers


lst = qwe1()
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
# разрядность интерпритатора и ОС соответсвенно-->('32bit', 'WindowsPE')
# Версия Python ---->3.8.2
# Расширение  ---->AMD64
# вариант 1
# start === 427
# finish == 724
# [10, 1000, 724, 0]
# тип объекта == <class 'list'>, память == 44 байт, объект == [10, 1000, 724, 0]
# тип объекта == <class 'int'>, память == 14 байт, объект == 10
# тип объекта == <class 'int'>, память == 14 байт, объект == 1000
# тип объекта == <class 'int'>, память == 14 байт, объект == 724
# тип объекта == <class 'int'>, память == 12 байт, объект == 0
# общая память == 98 байт

# Вывод:  переменных использованно большше чем в других вариантах задачи и экономичность по памяти минимальная
