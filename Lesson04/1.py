from timeit import timeit as my_timer
import cProfile
import random

"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

"""
MIM_N = 0
MAX_N = 100000000000000000000000000000000000000*100000000000000000000000000000000000000000
NUM = random.randint(MIM_N, MAX_N)
print(f' == {NUM}')
print('# вариант 1')


def qwe1(num):
    result = 0
    while num > 0:
        result = result * 10 + num % 10
        num = num // 10
    return result


print(my_timer('qwe1(NUM*1000)', number=100, globals=globals()))  # 0.0.0074923

print(my_timer('qwe1(NUM*10000)', number=100, globals=globals()))  # 0.007705799999999999
print(my_timer('qwe1(NUM*100000)', number=100, globals=globals()))  # 0.008703700000000009
print(my_timer('qwe1(NUM*1000000)', number=100, globals=globals()))  # 0.009402099999999997
print()
cProfile.run('qwe1(NUM)')

print('# =========2==========while==========================================')


def qwe2(num):
    revers = ''
    while num > 0:
        rem_num = num % 10
        num //= 10
        rem_num_str = str(rem_num)
        revers += rem_num_str
    return revers


print(my_timer('qwe2(NUM*1000)', number=100, globals=globals()))  # 0.019315099999999988
print(my_timer('qwe2(NUM*10000)', number=100, globals=globals()))  # 0.010403899999999994
print(my_timer('qwe2(NUM*100000)', number=100, globals=globals()))  # 0.010180999999999996
print(my_timer('qwe2(NUM*1000000)', number=100, globals=globals()))  # 0.010123400000000005
print()
cProfile.run('qwe2(NUM)')

print('# =========================рекурсия========================3')


def qwe3(numb):  # 63/1    0.000    0.000    0.000    0.000 NEW.py:54(qwe3)
    if numb < 10:
        return str(numb)
    else:
        return str(numb % 10) + ' ' + qwe3(numb // 10)


# print(qwe3(NUM))

print(my_timer('qwe3(NUM*1000)', number=100, globals=globals()))  # 0.016114900000000015
print(my_timer('qwe3(NUM*10000)', number=100, globals=globals()))  # 0.005654900000000004
print(my_timer('qwe3(NUM*100000)', number=100, globals=globals()))  # 0.015248100000000014
print(my_timer('qwe3(NUM*1000000)', number=100, globals=globals()))  # 0.013254899999999986
print()
cProfile.run('qwe3(NUM)')

'''
     фунции оказались простыми можно только сказать что быстродейтсвие 
     снижается от первой к третьей задачи 
     по cProfile слабых мест не выявлено

'''