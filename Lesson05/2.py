'''
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
 При этом каждое число представляется как коллекция, элементы которой — цифры числа.
 Например, пользователь ввёл A2 и C4F. Нужно сохранить их как
       [‘A’, ‘2’] и
  [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
  [‘C’, ‘F’, ‘1’],
  произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
'''

from collections import deque

f = deque(list(input('введите первое число : ').upper()))
s = deque(list(input('введите второе число : ').upper()))
n16 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']


def get_index(num16, value):
    for i, el in enumerate(num16):
        if el == value:
            return i


def sum16(first_num, second_num, num16):
    if len(first_num) > len(second_num):
        first_num, second_num = second_num, first_num
        second_num.extendleft('0' * (len(first_num) - len(second_num)))
    if len(second_num) > len(first_num):
        first_num.extendleft('0' * (len(second_num) - len(first_num)))

    over15 = 0
    j = -1
    i = -1
    rate = 16
    sum_int = deque()
    d = 0
    while d < len(second_num):
        first_index = get_index(num16, first_num[j])
        second_index = get_index(num16, second_num[i])
        sum_index = first_index + second_index
        egg = (sum_index + over15) % rate
        sum_int.appendleft(egg)
        if sum_index > 15:
            over15 = 1
        else:
            over15 = 0
        j -= 1
        i -= 1
        d += 1
    if over15 == 1:
        sum_int.appendleft(over15)

    sum_final = []
    for el in sum_int:
        char = num16.pop(el)
        sum_final.append(char)
        num16.insert(el, char)

    return sum_final


print(sum16(f, s, n16))
