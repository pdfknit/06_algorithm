'''
Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
'''


def find_substring(src_string):
    result_set = set()
    for count_letter in range(1, len(src_string)):
        for idx in range(len(src_string) - count_letter + 1):
            cur_src = hash(src_string[idx: count_letter + idx])
            result_set.add(cur_src)
    return len(result_set)


src_string = input('Введите строку\n')
print('Количество уникальных подстрок:', find_substring(src_string))
