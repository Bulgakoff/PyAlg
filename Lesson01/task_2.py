"""
Задание 2. Выполнить логические побитовые операции "И", "ИЛИ"
и др. над числами 5 и 6. Выполнить
над числом 5 побитовый сдвиг вправо и влево на два знака.

"""
a = 5  # 101
b = 6  # 110
qwe_left = 5 << 2
qwe_right = 5 >> 2

print(qwe_right)  # 1
print(qwe_left)  # 20

bit_and = (a & b)
bit_or = (a | b)
bit_ex = (a ^ b)
bit_un = (~a)

print(bit_and)
print(bit_or)
print(bit_ex)
print(bit_un)
