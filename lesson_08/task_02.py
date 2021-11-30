'''
Закодируйте любую строку по алгоритму Хаффмана.
Превратитет строку текста в строку из нулей и единиц - визуальное текстовое представление сжатие данных.
'''
from collections import Counter


def haffman_algotithm(src_string):
    str_len = len(src_string)

    letter_counter = Counter(src_string)
    if len(letter_counter) == 0:
        return None
    else:
        i = 1
        while i < len(letter_counter):
            min_list = letter_counter.most_common()[-i:-2 - i:-1]
            letter_counter[f'{min_list[0][0] + min_list[1][0]}'] = min_list[0][1] + min_list[1][1]
            i += 2

        # добавляю значения в результирующий словарь
        # я понимаю, что предполагалось использования дерева, но я не поняла как(

        result_dict = {}
        add_val = '1'
        for el, val in letter_counter.most_common()[1:]:
            for letter in el:
                try:
                    result_dict[letter] += add_val
                except:
                    result_dict[letter] = add_val
            if add_val == '0':
                add_val = '1'
            else:
                add_val = '0'

        return result_dict


src_string = input('Введите строку для кодирования\n')
code_dict = haffman_algotithm(src_string)
print('Результат кодирования:')
if code_dict:
    for k, v in code_dict.items():
        print(f'{k}: {v}')
