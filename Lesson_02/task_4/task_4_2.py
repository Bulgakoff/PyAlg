"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
ЧЕРЕЗ РЕКУРСИЮ
"""
q_elem = int(input('Введите количество элементов: '))


def rec4(n, rrr):
    if n == 1:
        return rrr
    else:
        return rrr + rec4(n - 1, rrr / -2)


print(rec4(q_elem, 1))