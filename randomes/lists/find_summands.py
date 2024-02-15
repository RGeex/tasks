"""
Можно ли вычислить куб как сумму?

В этой Ката вам будет присвоен номер n (где n >= 1) и ваша задача найти n последовательные нечетные
числа, сумма которых в точности равна кубу n.

Математически:
куб = n**3
сумма = a1 + a2 + a3 + ..... + an
сумма == куб
а2 == а1 + 2, а3 == а2 + 2, .......

Например:

find_summands(3) = [7,9,11] # because 7 + 9 + 11 = 27, the cube of 3. Note that there are only
n = 3 elements in the array.

Функция записи findSummands(n)который вернет массив из n последовательных нечетных чисел с суммой,
равной кубу n (n*n*n).
"""


def find_summands(n: int) -> list:
    """
    Декомпозиция куба числа на сумму нечетных чисел, в колличестве равном N.
    """
    return list(range((x := n ** 2) - n + 1, x + n, 2))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (1, [1]),
        (3, [7, 9, 11]),
        (4, [13, 15, 17, 19]),
    )
    for key, val in data:
        result = find_summands(key)
        assert len(result) == key
        assert result == val


if __name__ == '__main__':
    test()
