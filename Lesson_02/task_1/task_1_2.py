"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

 Рекурсией.

"""


def rec2_2():
    oper = input('Введите операцию (+, -, *, / или 0 для выхода): ')

    if oper == '0':
        return f'  0 для выхода'
    else:
        fir = int(input('Введите первое число: '))
        sec = int(input('Введите второе число: '))
        if oper == '+':
            res = fir + sec
            print(res)
            return rec2_2()
        elif oper == '-':
            res = fir - sec
            print(res)
            return rec2_2()
        elif oper == '*':
            res = fir * sec
            print(res)
            return rec2_2()
        elif oper == '/':
            res = fir / sec
            print(res)
            return rec2_2()
        return rec2_2()


try:
    print(rec2_2())
except ValueError as qwe:
    print('НЕ то ')
except ZeroDivisionError as qqq:
    print('на ноль поделили')