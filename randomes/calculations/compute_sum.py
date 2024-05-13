"""
Найдите сумму цифр всех чисел из 1к N(оба конца включены).
Примеры

# N = 4
1 + 2 + 3 + 4 = 10

# N = 10
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) = 46

# N = 12
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + (1 + 0) + (1 + 1) + (1 + 2) = 51
"""


def compute_sum(n: int) -> int:
    """
    Вычисляет сумму всех цифр диапазона от 0 до N включетельно.
    """
    return sum(sum(map(int, str(x))) for x in range(n + 1))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (1, 1),
        (2, 3),
        (3, 6),
        (4, 10),
        (10, 46),
        (12, 51),
    )
    for key, val in data:
        assert compute_sum(key) == val


if __name__ == '__main__':
    test()
