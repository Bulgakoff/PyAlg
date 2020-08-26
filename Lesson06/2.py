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
# Вариант №2

print('# вариант №2')


# @profile()
def qwe2():
    MIM_N = 10
    MAX_N = 1000
    num = randint(MIM_N, MAX_N)
    print(f'start === {num}')
    revers = ''
    while num > 0:
        rem_num = num % 10
        num //= 10
        rem_num_str = str(rem_num)
        revers += rem_num_str
    print(f'finish == {revers}')
    lst_var = [MIM_N, MAX_N, revers, rem_num, rem_num_str]
    # lst_var = {'MIM_N': MIM_N, 'MAX_N': MAX_N, 'result': revers}

    return lst_var
    #


lst = qwe2()
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
# вариант №2
# start === 498
# finish == 894
# [10, 1000, '894', 4, '4']
# тип объекта == <class 'list'>, память == 48 байт, объект == [10, 1000, '894', 4, '4']
# тип объекта == <class 'int'>, память == 14 байт, объект == 10
# тип объекта == <class 'int'>, память == 14 байт, объект == 1000
# тип объекта == <class 'str'>, память == 28 байт, объект == 894
# тип объекта == <class 'int'>, память == 14 байт, объект == 4
# тип объекта == <class 'str'>, память == 26 байт, объект == 4
# общая память == 144 байт

# Вывод: из всех вариантов это  самый затратный вариант по памяти
