"""
Задание 4. Написать программу, которая генерирует в указанных пользователем границах:
    случайное целое число;
    случайное вещественное число;
    случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

"""

from random import random

# =============случайное целое число================
left_bount = ord(input('enter the integer left_bount --> a : '))
right_bound = ord(input('enter the integer left_right --> f : '))

int_rand = int(random() * ((right_bound - (left_bount + 1)))) + left_bount
print(int_rand)

# =============вещественное число================

left_bount_fl = float(ord(input('enter the float left_bount --> a : ')))
right_bound_fl = float(ord(input('enter the float left_right --> f : ')))

fl_rand = int(random() * ((right_bound_fl - (left_bount_fl + 1)))) + left_bount_fl
print(fl_rand)
# =============случайный символ=============

left_bount = ord(input('enter the random char left_bount --> a : '))
right_bound = ord(input('enter the integer char left_right --> f : '))
chr_rand = chr(int(random() * ((right_bound - (left_bount - 1)))) + left_bount)
print(chr_rand)
