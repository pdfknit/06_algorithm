# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
import random


def mediana(array):
    for _ in range(len(array) // 2):
        array.remove(min(array))  # если мин и макс еще не используем, ниже закоментированная функция с циклами
    mediana_val = min(array)
    return mediana_val


# def mediana(array):
#     for _ in range(len(array) // 2):
#         min_ = array[0]
#         for el in array:
#             if min_ > el:
#                 min_ = el
#         array.remove(min_)
#     min2 = array[0]
#     for el in array:
#         if min2 > el:
#             min2 = el
#     mediana_val = min2
#     return mediana_val


def rand_array(size, min_v, max_v):
    if size % 2 == 0:  # для нечетности
        size += 1
    array = [random.randint(min_v, max_v) for _ in range(size)]
    return array


cur_array = rand_array(11, 0, 49)
# cur_array = [0, 3, 1, 1, 4, 5, 6]
print(f'Исходный список = {cur_array}')
print(f'Медиана списка = {mediana(cur_array)}')
