"""
Последовательность Пелла это последовательность целых чисел, определяемая начальными значениями.

P(0) = 0, P(1) = 1

и рекуррентное соотношение

P(n) = 2 * P(n-1) + P(n-2)

Первые несколько значений P(n)являются

0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, 33461, 80782, 195025, 470832, ..
"""


def pell(n: int) -> int:
    """
    Вычисляет N-ое число Пелла.
    """
    a, b, c = 0, 1, 1
    while c < n:
        a, b, c = b, a + 2 * b, c + 1
    return b if n else 0


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 5),
        (4, 12),
    )
    for key, val in data:
        assert pell(key) == val


if __name__ == '__main__':
    test()
