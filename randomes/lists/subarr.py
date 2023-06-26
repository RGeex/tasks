"""
Дано список чисел и дополнительное число k.
Найти кол-во подмассивов в сумме равное k.
"""


def subarr1(arr: list, k: int) -> int:
    """Поиск кол-ва подмассивов равное k."""
    res = 0
    for x, n in enumerate(arr):
        for y, m in enumerate(arr[x:]):
            n += m if y else y
            if n == k:
                res += 1
    return res


def subarr2(arr: list, k: int) -> int:
    """Поиск кол-ва подмассивов равное k."""
    temp, res, data = 0, 0, {0: 1}
    for n in arr:
        temp += n
        data[temp] = data.get(temp, 0) + 1
        res += data.get(temp - k, 0)
    return res


def test() -> None:
    """Тестирование работы алгоритмов."""
    data = [
        (([7, 2, -5, 1, 1, -1, 5, -5], 5), 5),
        (([7, 2, -5, 1, 1, -1, 5, -5], 3), 1),
    ]

    for (key, val), res in data:
        assert subarr1(key, val) == res
        assert subarr2(key, val) == res


if __name__ == '__main__':
    test()
