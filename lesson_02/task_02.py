# 2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

def count_sum(digit, even_sum=0, uneven_sum=0):
    if digit != 0:
        cur_element = digit % 10
        if cur_element % 2 == 0:
            even_sum += cur_element
        else:
            uneven_sum += cur_element
        even_sum, uneven_sum = count_sum(digit // 10, even_sum, uneven_sum)
    return even_sum, uneven_sum


a = int(input('Введите число'))

sum1, sum2 = count_sum(a)
print(sum1, sum2)
