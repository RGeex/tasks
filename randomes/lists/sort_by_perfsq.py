"""
Вам будет предоставлен массив целых положительных чисел. Массив должен быть отсортирован по
количеству различных полных квадратов и перевернут, что можно получить из каждого числа,
переставив его цифры.

Например: arr = [715, 112, 136, 169, 144]

Number   Perfect Squares w/ its Digits   Amount
 715                -                       0
 112               121                      1
 136               361                      1
 169           169, 196, 961                3
 144             144, 441                   2

Таким образом, вывод будет иметь следующий порядок: [169, 144, 112, 136, 715]

Когда у нас есть два или более чисел с одинаковым количеством полных квадратов в их перестановках,
мы сортируем их по их значениям.

В приведенном выше примере мы видим, что 112 и 136 образуют идеальный квадрат. Итак, на первом
месте стоит 112.

Примеры этого ката:

sort_by_perfsq([715, 112, 136, 169, 144]) == [169, 144, 112, 136, 715]
# number of perfect squares:                   3    2    1    1    0

В массиве могут быть числа, принадлежащие к одному и тому же набору перестановок.

sort_by_perfsq([234, 61, 16, 441, 144, 728]) == [144, 441, 16, 61, 234, 728]
# number of perfect squares:                      2    2    1   0   0    0

Особенности случайных тестов:

    Количество тестов: 80
    Массивы от 4 до 20 элементов
    Включены целые числа, содержащие от 1 до 7 цифр.

"""
from itertools import permutations as pm


def sort_by_perfsq(arr: list) -> list:
    """
    Сортировка списка по кол-ву квадратов числа при перестановках цифр,
    в порядке убывания кол-ва квадратов, по возрастанию исходных чисел.
    """
    return sorted(arr, key=lambda x: (-sum(not int(''.join(n)) ** .5 % 1 for n in set(pm(str(x)))), x))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([715, 112, 136, 169, 144], [169, 144, 112, 136, 715]),
        ([234, 61, 16, 441, 144, 728], [144, 441, 16, 61, 234, 728]),
        ([4468, 446689, 169, 4477, 1345689], [1345689, 169, 4468, 4477, 446689]),
    )
    for key, val in data:
        assert sort_by_perfsq(key) == val


if __name__ == '__main__':
    test()
