"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

 РЕКУРСИЯ
"""
QUANTITY = int(input('Введите количество чисел: '))



def rec_summ(num):
    if num < 10:
        return num
    else:
        return num % 10 + rec_summ(num // 10)


sum_max_num = 0
number_max_sum = 0

for i in range(1, QUANTITY + 1):
    num_num = int(input('Введите  цифру: '))
    if rec_summ(num_num) > sum_max_num:
        sum_max_num = rec_summ(num_num)
        number_max_sum = num_num
print(f'Наибольшее число : {number_max_sum},'
      f' сумма его цифр: {sum_max_num}')