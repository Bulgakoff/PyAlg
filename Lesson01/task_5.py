"""
Задание 5.
Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв.
"""
letter1 = ord(input('enter first letter (a): ').lower())
letter2 = ord(input('enter second letter (z): ').lower())

# ==========колличество символов между буквами ================
QWE = 96
if letter1 <= letter2:
    qwe = (letter2 - letter1) - 1
    print(letter1 - QWE, '  ', letter2 - QWE)
    print(qwe)
else:
    letter2, letter1 = letter1, letter2
    qwe = (letter2 - letter1) - 1
    print(letter2 - QWE, '  ', letter1 - QWE)
    print(qwe)
