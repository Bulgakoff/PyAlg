"""
Задание 6.	Пользователь вводит номер буквы в алфавите.
Определить, какая это буква.

"""
user_num = int(input('enter number :  '))
QWE = 96
chr_num = chr(user_num + QWE)
print(chr_num)