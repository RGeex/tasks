"""
Учитывая массив [x1, x2, ..., xn] определить, можно ли поставить + или - между
элементами и получим выражение, равное sum. Результат boolean

2 <= n <= 22
0 <= xi <= 20
-10 <= sum <= 10

Пример

arr = [1, 3, 4, 6, 8]

sum = -2

1 + 3 - 4 + 6 - 8 = -2

Результат: true
Примечания

Если невозможно найти решение, то следует вернуться false.
"""


def is_possible(lst: list, gl: int) -> bool:
    """
    Получится ли заданное число при различных комбинациях использования "+" или "-" между заданными числами.
    """
    return gl in [r := [x] if not i else [n for v in [(n + x, n - x) for n in r] for n in v] for i, x in enumerate(lst)][-1]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (([1, 3], 2), False),
        (([1, 3, 4, 6, 8], 8), True),
        (([1, 3, 4, 6, 8], -2), True),
        (([15, 2, 3], 10), True),
        (([1, 5, 3, 2, 5], -2), False),
    )
    for key, val in data:
        assert is_possible(*key) == val


if __name__ == '__main__':
    test()