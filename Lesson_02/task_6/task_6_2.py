"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЧЕРЕЗ РЕКУРСИЮ
"""
import random

rand_num = int(random.random() * 100)
count = 1


def rec6(rand_num, count):
    if count == 10:
        return f'потрачены все попытки '
    else:
        print(f'attempt {count}')
        user_answer = int(input('enter num : '))
        if rand_num == user_answer:
            return f'you winner '
        elif rand_num > user_answer:
            print('загаданное число больше вашего')
            return rec6(rand_num, count + 1)
        else:
            print('загаданное число меньше вашего')
            return rec6(rand_num, count + 1)


print(rec6(rand_num, count))
