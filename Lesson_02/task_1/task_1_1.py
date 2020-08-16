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

ЧЕРЕЗ ЦИКЛ
"""

'https://drive.google.com/file/d/18ftA2QRvdWm_FEwlTJLkGVlzmKZLCQek/view?usp=sharing'

flag = True
while flag:
    try:
        fir_num = int(input('Введите первое число:  '))
        sec_num = int(input('Введите второе число:  '))

        while True:
            oper = input('Введите операцию (+, -, *, / или 0 для выхода):')
            if oper == '0':
                flag = False
                print('Вы ввели 0 - до свидания')
                break
            if oper == '+':
                res = fir_num + sec_num
                print(res)
                break
            elif oper == '-':
                res = fir_num - sec_num
                print(res)
                break
            elif oper == '*':
                res = fir_num * sec_num
                print(res)
                break
            elif oper == '/':
                res = fir_num / sec_num
                print(res)
                break
            if oper != '+' or oper != '-' or oper != '*' or oper != '/' or oper != 0:
                print(f'вы ввели {oper} введите корректные данные ')
                continue
    except ValueError:
        print(f' введите цифру ')
        continue
    except ZeroDivisionError:
        print('вы делите на ноль - все с начала')
        continue
