"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
то надо вывести число 6843.

ЧЕРЕЗ ЦИКЛ
"""
num = 123
revers = ''
while num > 0:
    rem_num = num % 10
    num //= 10
    rem_num_str = str(rem_num)
    revers += rem_num_str
print(revers)




