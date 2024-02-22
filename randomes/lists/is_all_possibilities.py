"""
Непустой массив aдлины nназывается массивом всех возможностей,
если он содержит все числа между [0,a.length-1].Напишите метод
с именем isAllPossibilitiesкоторый принимает целочисленный
массив и возвращает true если массив представляет собой массив
всех возможностей, иначе false.
"""


def is_all_possibilities(arr: list) -> bool:
    """
    Проверяет, является ли переданный список - массивом всех возможностей.
    """
    return bool(arr) and len(set(arr)) == len(arr) and len(arr) * (len(arr) - 1) // 2 == sum(arr)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ([0, 2, 19, 4, 4], False),
        ([3, 2, 1, 0], True),
        ([0, 1, 2, 3], True),
        ([1, 2, 3, 4], False),
        ([0, 2, 3], False),
        ([0], True),
        ([], False),
        ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], True),
        ([0, 1, 3, -2, 5, 4], False),
        ([1, -1, 2, -2, 3, -3, 6], False),
    )
    for key, val in data:
        assert is_all_possibilities(key) == val


if __name__ == '__main__':
    test()
