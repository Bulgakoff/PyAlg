"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
ЧЕРЕЗ ЦИКЛ
"""

num_el = int(input('enter 3 '))
summ = 0
range_num = 1
for i in range(num_el):
    summ += range_num
    range_num /= -2

print(summ)
