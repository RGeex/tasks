"""
Учитывая определенное целое число n, n > 0 и несколько разделов, k, k > 0;
мы хотим знать раздел, который имеет максимальное или минимальное
произведение его членов.

Функция find_spec_partition() , получит три аргумента, n, k и команда:
'max' or 'min'

Функция должна вывести раздел, имеющий максимальное или минимальное значение
произведения (это зависит от заданной команды), в виде массива с его членами
в порядке убывания.

Давайте рассмотрим некоторые случаи (Python и Ruby)

find_spec_partition(10, 4, 'max') == [3, 3, 2, 2]
find_spec_partition(10, 4, 'min') == [7, 1, 1, 1]

и Javascript:

findSpecPartition(10, 4, 'max') == [3, 3, 2, 2]
findSpecPartition(10, 4, 'min') == [7, 1, 1, 1]

Разделы 10 с 4 членами с их продуктами:

(4, 3, 2, 1): 24
(4, 2, 2, 2): 32
(6, 2, 1, 1): 12
(3, 3, 3, 1): 27
(4, 4, 1, 1): 16
(5, 2, 2, 1): 20 
(7, 1, 1, 1): 7   <------- min. productvalue
(3, 3, 2, 2): 36  <------- max.product value
(5, 3, 1, 1): 15
"""


def find_spec_partition(n: int, k: int, com: str) -> list[int]:
    """
    Раскладывает заданное число на слагаемые и выбирает среди них
    с указанным max или min произведением этих чисел, с лимитом k.
    """
    a, b = divmod(n, k)
    return [a + 1] * b + [a] * (k - b) if com == 'max' else [n - k + 1] + [1] * (k - 1)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ((10, 4, 'max'), [3, 3, 2, 2]),
        ((10, 4, 'min'), [7, 1, 1, 1]),
    )
    for key, val in data:
        assert find_spec_partition(*key) == val


if __name__ == '__main__':
    test()
