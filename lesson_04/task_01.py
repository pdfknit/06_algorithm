'''Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.'''

# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.


import random
import timeit


def mirror_01(digit, mirror_digit=0):
    if digit == 0:
        return mirror_digit
    else:
        cur_element = digit % 10
        mirror_digit = mirror_digit * 10 + cur_element
        return mirror_01(digit=digit // 10, mirror_digit=mirror_digit)


def mirror_02(digit):
    mirror_digit = ''
    for letter in digit[::-1]:
        mirror_digit += letter
    return int(mirror_digit)


def mirror_03(digit):
    mirror_digit = ''
    for letter in reversed(digit):
        mirror_digit += letter
    return mirror_digit


el = 1
a_list = []
while el < 1_000_000_000_000_000_000_000_000_000_000_000_000:
    a_list.append(random.randint(el, el * 9))
    el *= 1000
print(a_list)

for a in a_list:
    print(timeit.timeit('mirror_01(a)', number=1000, globals=globals()))
    print(timeit.timeit('mirror_02(str(a))', number=1000, globals=globals()))
    print(timeit.timeit('mirror_03(str(a))', number=1000, globals=globals()))
    print()


'''
Графики: https://docs.google.com/spreadsheets/d/1jD-X8WmfwoghxEAxCCclgmC7oL213nQ3glQfaw0fk_o/edit?usp=sharing
'''

# Вывод: при линейном усложнении функции, вариант 1 изменяется неоднозначно: непонятно экспоненциально или ленейно(нужно больше измерений, но точно медленнее, чем второй и третий.
# Второй и третий изменяются линейно и разницы между reversed и [::-1] нет
