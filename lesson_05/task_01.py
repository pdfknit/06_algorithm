# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего.
from collections import Counter, defaultdict

PROFIT_COUNT = 4


def add_factory():
    profit_counter = Counter()
    while True:
        factory_name = input('Введите название предприятия или Enter')
        if factory_name == '':
            break
        for quart in range(PROFIT_COUNT):
            factory_profit = float(input(f'Прибыть предприятия за {quart + 1} квартал:'))
            profit_counter[factory_name] += factory_profit
    return profit_counter


def count_profit(profit_dict):
    result_list = defaultdict(list)
    average_profit = sum(profit_dict.values()) / len(profit_dict)
    for factory, val in profit_dict.items():
        if val > average_profit:
            result_list['Выше среднего'].append(factory)
        elif val < average_profit:
            result_list['Ниже среднего'].append(factory)
    return result_list


profits_dict = add_factory()
result_list = count_profit(profits_dict)
for name, val in result_list.items():
    print(f'{name}: {", ".join(val)}')
