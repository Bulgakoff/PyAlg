"""
Задание 8.	Определить, является ли год, который ввел пользователем,
високосным или не високосным.

"""

res_year = 2000

# вариант №1
if res_year % 4 != 0:
    print(f'год {res_year} обычный')
elif res_year % 100 != 0:
    print(f'год {res_year} високостный')
elif res_year % 400 == 0:
    print(f'год {res_year} високостный')
else:
    print(f'год {res_year} обычный')

# вариант №2
if res_year % 400 == 0:
    print(f'год {res_year} високостный')
elif res_year % 400 == 0:
    print(f'год {res_year} обычный')
elif res_year % 4 == 0:
    print(f'год {res_year} високостный')
else:
    print(f'год {res_year} обычный')