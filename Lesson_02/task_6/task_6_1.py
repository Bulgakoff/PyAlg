"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

ЧЕРЕЗ ЦИКЛ
"""
import random

rand_num = int(random.random() * 100)
count = 1
while count <= 10:
    print(f'attempt {count}')
    user_answer = int(input('enter num : '))
    if rand_num == user_answer:
        print('you winner ')
        break
    elif rand_num > user_answer:
        print('загаданное число больше вашего')
    else:
        print('загаданное число меньше вашего')
    count += 1
else:
    print(f'вы потратили все попытки {count - 1} шт')


