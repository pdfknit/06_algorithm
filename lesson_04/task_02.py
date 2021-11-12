'''
Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное
и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.

Первый — с помощью алгоритма «Решето Эратосфена».
Второй — без использования «Решета Эратосфена».
'''

# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
import cProfile
import timeit


def primes_01(n):
    if n <= 20:
        max_range = n * 4
    elif n <= 1000:
        max_range = int((n ** 0.5) * n)
    else:
        max_range = int((n ** 0.3) * n)
    sieve = [i for i in range(max_range)]

    sieve[1] = 0
    for i in range(2, max_range):
        if sieve[i] != 0:
            j = i + i
            while j < max_range:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    return res[n - 1]


def primes_02(n):
    primes_array = [2]
    i = 2
    while True:
        if len(primes_array) >= n:
            break
        i += 1
        primes = True
        for idx in range(0, len(primes_array)):
            if i ** 0.5 < primes_array[idx]:
                break
            if i % primes_array[idx] == 0:
                primes = False
                break
        if primes:
            primes_array.append(i)

    return primes_array[-1]


def main(n):
    primes_01(n)
    primes_02(n)


# n = 10_000
# cProfile.run(f'main({n})')

#  n = 10_000
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.471    0.471 <string>:1(<module>)
#      1    0.061    0.061    0.072    0.072 task_02.py:15(primes_01)
#      1    0.006    0.006    0.006    0.006 task_02.py:22(<listcomp>)
#      1    0.005    0.005    0.005    0.005 task_02.py:32(<listcomp>)
#      1    0.376    0.376    0.398    0.398 task_02.py:36(primes_02)
#      1    0.001    0.001    0.471    0.471 task_02.py:56(main)
#      1    0.000    0.000    0.471    0.471 {built-in method builtins.exec}
# 209455    0.021    0.000    0.021    0.000 {built-in method builtins.len}
#   9999    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# n = 100_000
#  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       1    0.000    0.000   10.969   10.969 <string>:1(<module>)
#       1    1.525    1.525    1.792    1.792 task_02.py:15(primes_01)
#       1    0.167    0.167    0.167    0.167 task_02.py:22(<listcomp>)
#       1    0.100    0.100    0.100    0.100 task_02.py:32(<listcomp>)
#       1    8.883    8.883    9.155    9.155 task_02.py:36(primes_02)
#       1    0.023    0.023   10.969   10.969 task_02.py:56(main)
#       1    0.000    0.000   10.969   10.969 {built-in method builtins.exec}
# 2599415    0.262    0.000    0.262    0.000 {built-in method builtins.len}
#   99999    0.010    0.000    0.010    0.000 {method 'append' of 'list' objects}
#       1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

for test in range(3, 2_100, 200):
    print(timeit.timeit('primes_01(test)', number=1000, globals=globals()))
    print(timeit.timeit('primes_02(test)', number=1000, globals=globals()), end='\n\n')

for test in range(3_103, 9_100, 2000):
    print(timeit.timeit('primes_01(test)', number=1000, globals=globals()))
    print(timeit.timeit('primes_02(test)', number=1000, globals=globals()), end='\n\n')

'''

Графики: https://docs.google.com/spreadsheets/d/1jD-X8WmfwoghxEAxCCclgmC7oL213nQ3glQfaw0fk_o/edit?usp=sharing

Вывод: Решето Эратосфена работает быстрее, чем классический метод нахождения простых чисел. 
И чем больше значения, тем больше разницы. По форме графика похоже, что классический метод за счет вложенного цикла усложняется нелинейно, 
что еще больше невыгодно.

В решете Эратосфена для больших чисел можно еще скореектировать максимальное число для прорешечивания, тем самым не создавая лишних ячеек.
Честно говоря, у меня не получилось применить формулы, которые нашла в Википедии, потому что не до конца разобралась в ней 
и коэффициенты выбирала на основе табличных сравнений разницы между количеством простых чисел и натуральных чисел в этом же диапазоне
'''
