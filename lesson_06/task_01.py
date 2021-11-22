import sys
import random


def find_memory_sum(all_variables_dict):
    memory_sum = 0

    for variable, value in all_variables_dict.items():
        memory_sum += sys.getsizeof(value)
        if isinstance(value, list):
            variables_list = {}
            for num, el in enumerate(value):
                variables_list[num] = el
            memory_sum += find_memory_sum(variables_list)

    return memory_sum


def rand_array(size, min, max):
    array = [random.randint(min, max) for _ in range(size)]
    print(f'Сумма памяти {rand_array.__name__} = {find_memory_sum(dict(locals()))}')
    return array


'''В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.'''


def find_summ_01(array):
    min_index = 0
    max_index = 0

    for i in range(1, len(array)):
        if array[i] < array[min_index]:
            min_index = i
        elif array[i] > array[max_index]:
            max_index = i

    result = 0

    if max_index > min_index:
        start = min_index + 1
        last_el = max_index
    else:
        start = max_index + 1
        last_el = min_index

    for i in range(start, last_el):
        result += array[i]

    print('Сумма элементов между максимальным и минимальным = ', result)
    print(f'Сумма памяти {find_summ_01.__name__} = {find_memory_sum(dict(locals()))}')


def find_summ_02(array):
    for idx, el in enumerate(array):
        if min(array) == el:
            min_index = idx
        if max(array) == el:
            max_index = idx

    if max_index < min_index:
        array = sum(array[max_index + 1: min_index])
    else:
        array = sum(array[min_index + 1: max_index])

    print('Сумма элементов между максимальным и минимальным = ', array)
    print(f'Сумма памяти {find_summ_02.__name__} = {find_memory_sum(dict(locals()))}')


def find_summ_03(array):
    for idx, el in enumerate(array):
        if min(array) == el:
            min_index = idx
        if max(array) == el:
            max_index = idx

    indexes = [[max_index, min_index] if max_index < min_index else [min_index, max_index]][0]
    result_list = array[(indexes[0] + 1): indexes[1]]
    result = 0
    for el in result_list:
        result += el

    print('Сумма элементов между максимальным и минимальным = ', result)
    print(f'Сумма памяти {find_summ_03.__name__} = {find_memory_sum(dict(locals()))}')


array = rand_array(1000, 1, 10000)
print('_' * 55)
find_summ_01(array)
print('_' * 55)
find_summ_02(array)
print('_' * 55)
find_summ_03(array)

rand_array(10, 1, 100)

'''
Ссылка на таблицу с результатами
https://docs.google.com/spreadsheets/d/1wSGMfWDASIWh-ckar0dROfOV8LjPnJBhsD0LFwXey2I/edit?usp=sharing 

Вывод:
Первое впечатление было, что результат 2 варианта лучше остальных, однако, если подумать о том, что там перезаписывается 
array, а результат считается по финальным переменным, то для более точного решения задачи оптимизации памяти пришлось вычитать 
память, занимаемую массивом.

Отдельно хочется отметить, что после 1000 объем памяти массива не увеличивается. Я думаю, это связано с тем, что числа 
при генерации начали повторяться и перестали занимать отдельные ячейки памяти

В результате решение 1 оказалось наиболее эффективным по памяти и не увеличивается с ростом массива
Решение 2 я считаю тоже приемлемым, потому что оно тоже констатное и, выбирая между ними, я бы посмотрела еще разницу в скорости их выполнения
Решение 3 показало себя наименее эффективным по памяти (что и понятно, ведь перед суммированием формируется еще 1 массив 
из всех элементов, которые необходимо суммировать) и количество памяти растет линейно с ростом последовательности.
Пики на графике 3-го решения вызван тем, что расстояние между мин и макс индексами может варьироваться независимо от длины массива
'''

# Сумма памяти rand_array = 274
# Сумма памяти find_summ_01 = 316
# Сумма памяти find_summ_02 = 72
# Сумма памяти find_summ_03 = 466

100
# Сумма памяти rand_array = 1894
# Сумма памяти find_summ_01 = 1938
# Сумма памяти find_summ_02 = 72
# Сумма памяти find_summ_03 = 2232

1000

# Сумма памяти rand_array = 18550
# Сумма памяти find_summ_01 = 18594
# Сумма памяти find_summ_02 = 72
# Сумма памяти find_summ_03 = 26520

10_000
# Сумма памяти rand_array = 18550
# Сумма памяти find_summ_01 = 18594
# Сумма памяти find_summ_02 = 72
# Сумма памяти find_summ_03 = 22668

100_000
# Сумма памяти rand_array = 18550
# Сумма памяти find_summ_01 = 18594
# Сумма памяти find_summ_02 = 72
# Сумма памяти find_summ_03 = 22182

1_000_000
# Сумма памяти rand_array = 18550
# Сумма памяти find_summ_01 = 18594
# Сумма памяти find_summ_02 = 72
# Сумма памяти find_summ_03 = 34278
