"""
Задание_1. В диапазоне натуральных чисел от 2 до 99 определить,
сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

"""
for j in range(2, 9 + 1):
    ccc = 0
    for i in range(2, 99 + 1):
        if i % j == 0:
            ccc += 1
    print(f'В диапазоне 2-99: {ccc} чисел кратны {j}')