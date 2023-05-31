"""
В заданном списке чисел, найти сумму всех делителей,
являющихся простыми числами и сгруппированнми по делителю.
Например:
lst = [12, 15], где делители [2, 12], [3, 12], [3, 15] =>
# return [[2, 12], [3, 27], [3, 15]]
"""


def sum_for_list(lst: list) -> list[list]:
    """Поиск суммы сгруппированных простых делителей."""
    res = {}
    for num in lst:
        tmp, dl = num, 1

        while abs(tmp) > dl:
            dl += 1
            if not tmp % dl:
                res[dl] = res.get(dl, 0) + num
                while not tmp % dl:
                    tmp //= dl

    return sorted([k, v] for k, v in res.items())


def test() -> None:
    """Тестирование работы алгоритмов."""

    arr1 = [12, -15]
    arr2 = [15, 21, 24, 30, 45, 81]

    lst1 = [[2, 12], [3, -3], [5, -15]]
    lst2 = [[2, 54], [3, 216], [5, 90], [7, 21]]

    assert sum_for_list(arr1) == lst1
    assert sum_for_list(arr2) == lst2


if __name__ == '__main__':
    test()
