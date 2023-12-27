"""
У нас есть массив со строковыми цифрами, который встречается более одного раза,
например: arr = ['1', '2', '2', '2', '3', '3'].
Сколько разных строковых чисел можно сгенерировать, используя одновременно 6 элементов?

Ниже мы представляем их список в несортированном виде:

['223213', '312322', '223312', '222133', '312223', '223321', '223231', '132223', '132322',
'223132', '322321', '322312', '231322', '222313', '221233', '213322', '122323', '321322',
'221332', '133222', '123232', '323221', '222331', '132232', '321232', '212323', '232213',
'232132', '331222', '232312', '332212', '213223', '123322', '322231', '321223', '231232',
'233221', '231223', '213232', '312232', '233122', '322132', '223123', '322123', '232231',
'323122', '323212', '122233', '212233', '123223', '332221', '122332', '221323', '332122',
'232123', '212332', '232321', '322213', '233212', '313222']

Есть 60разные цифры и 122233является самым низким и 332221самый высокий из всех.

Учитывая массив, arr, со строковыми цифрами (от '0' до '9'), вы должны указать точное количество
различных чисел, которые могут быть сгенерированы с наименьшим и наибольшим значением, но оба
преобразованы в целые значения, используя все цифры, данные в массиве для номер каждой
сгенерированной строки.

Функция будет вызываться как proc_arr().

proc_arr(['1', '2', '2', '3', '2', '3']) == [60, 122233, 332221]

Если цифра «0» присутствует в данном массиве, это приведет к созданию строковых чисел с ведущими
нулями, которые не будут учитываться при их преобразовании в целые числа.

proc_arr(['1','2','3','0','5','1','1','3']) == [3360, 1112335, 53321110]

Вы никогда не получите массив, в котором только одна цифра повторится n раз.

Особенности случайных тестов:

Low performance tests:
Number of tests: 100
Arrays of length between 6 and 10

Higher performance tests:
Number of tests: 100
Arrays of length between 30 and 100
"""


from operator import mul
from functools import reduce
from collections import Counter
from math import factorial as fl

from itertools import permutations as pm


def proc_arr1(arr: list[str]) -> list[int]:
    """
    Поиск кол-ва комбинаций, а так же минимальное и максимальные значения.
    """
    return [len(set(pm(arr, len(arr))))] + [int(''.join(sorted(arr)[::n])) for n in [1, -1]]


def proc_arr2(arr: list[str]) -> list[int]:
    """
    Поиск кол-ва комбинаций, а так же минимальное и максимальные значения.
    """
    return [fl(len(arr)) // reduce(mul, map(fl, Counter(arr).values()))] + [int(''.join(sorted(arr)[::n])) for n in [1, -1]]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (['1', '2', '2', '3', '2', '3'], [60, 122233, 332221]),
        (['1', '2', '3', '0', '5', '1', '1', '3'], [3360, 1112335, 53321110]),
    )
    for key, val in data:
        assert proc_arr1(key) == val
        assert proc_arr2(key) == val


if __name__ == '__main__':
    test()
