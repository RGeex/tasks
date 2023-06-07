"""
Даны 2 отсортированных списка чисел,
необходимо найти медиану этих списков.

медиана это - среднее значение элементов списка при
нечетном кол-ве эелементов, при четном - среднее значение
суммы двух центральных элементов.
"""


def median(a: list, b: list):
    """Поиск медианного значения двух списков."""

    # общая длина двух списков
    lnx = sum(map(len, (a, b)))
    # искомые индексы элементов
    ndx = {(x := lnx // 2), x - int(not lnx % 2)}
    # результирующий список и стартовые индексы списков
    res, m, n = [], 0, 0

    while len(res) < len(ndx):
        if len(a) > m and a[m] < b[n]:
            tmp = a[m]
            m += 1
        else:
            tmp = b[n]
            n += 1
        if m + n - 1 in ndx:
            res.append(tmp)

    res = sum(res) / len(res)
    return int(res) if res.is_integer() else res


def test() -> None:
    """Тестирование работы алгоритмов."""
    data = [
        (([1, 2, 3], [4, 5, 6]), 3.5),
        (([1, 2, 3, 5], [4, 5, 6]), 4),
    ]

    for args, val in data:
        assert median(*args) == val


if __name__ == '__main__':
    test()
