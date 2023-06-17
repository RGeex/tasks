"""
Даны 2 отсортированных списка чисел,
необходимо найти медиану этих списков.

медиана это - среднее значение элементов списка при
нечетном кол-ве эелементов, при четном - среднее значение
суммы двух центральных элементов.
"""


def median(*args: list) -> int | float:
    """Поиск медианного значения отсортированных списков в кол-ве от 1 до N."""

    # общая длина списков
    lnx = sum(map(len, args))
    # индексы элементов, которые нужно найти
    ndx = {(x := lnx // 2), x - int(not lnx % 2)}
    # результирующий список и стартовые индексы списков
    res, inx = [], [0] * len(args)

    while len(res) < len(ndx):
        # минимальное значение среди списков
        tmp = min((args[i][val], i) for i, val in enumerate(inx) if len(args[i]) > val)
        if sum(inx) in ndx:
            res.append(tmp[0])
        inx[tmp[1]] += 1

    res = sum(res) / len(res)
    return int(res) if res.is_integer() else res


def test() -> None:
    """Тестирование работы алгоритмов."""
    data = [
        (([1, 2, 3, 4, 5, 6, 7],), 4),
        (([1, 2, 3], [4, 5, 6]), 3.5),
        (([1, 2, 3, 5], [4, 5, 6]), 4),
        (([5], [1, 2, 6], [8, 9], [3]), 5),
    ]

    for args, val in data:
        assert median(*args) == val


if __name__ == '__main__':
    test()
