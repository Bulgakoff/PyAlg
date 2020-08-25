"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала  для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

"""

from collections import defaultdict

QU_CO = int(input('Введите количество предприятий для расчета прибыли: '))
QU_QUART = 4
d = defaultdict(int)
for i in range(QU_CO):
    company = input('Введите название предприятия: ')
    d[company] = 0
    for j in range(QU_QUART):
        revenue = int(input('введите прибыль данного предприятия квартал(Всего 4 квартала): '))
        d[company] += revenue
sum_revenue = 0
for v in d.values():
    sum_revenue += v
average_rev = int(sum_revenue // QU_CO)
for k, v in d.items():
    if v > average_rev:
        print(f'Предприятие {k} имеет прибыль  {v}, это выше среднего -- ({average_rev}) ')
    if v < average_rev:
        print(f'Предприятие {k} имеет прибыль  {v}, это ниже среднего -- ({average_rev}) ')
