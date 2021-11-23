# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами на промежутке
# [-100; 100). Выведите на экран исходный и отсортированный массивы
import random


def rand_array(size, min_v, max_v):
    array = [random.randint(min_v, max_v) for _ in range(size)]
    return array


def bubble_sort(array):
    n = 1
    while n < len(array) - 1:
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        n += 1
    return array


cur_array = rand_array(10, -100, 99)
print(f'Исходный массив: {cur_array}')
print(f'Результат сортировки пузырьком: {bubble_sort(cur_array)}')
