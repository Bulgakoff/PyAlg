"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

 ЧЕРЕЗ ЦИКЛ
"""

nut_nu = input('Введите натуральное число: ')
count_even = 0
count_odd = 0
even = ' '
odd = ' '
for p in nut_nu:
    if int(p) % 2 == 0:
        count_even += 1
        even += str(p)
    else:
        count_odd += 1
        odd += str(p)

print(f'В числе {nut_nu} всего {count_odd + count_even} '
      f'цифр, из которых {count_even} чётных ({even}) и '
      f'{count_odd} нечётных ({odd})')

