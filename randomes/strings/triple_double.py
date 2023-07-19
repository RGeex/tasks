"""

Написать функцию:
которая принимает числа num1 и num2 и возвращает 1, если в любом месте num1
есть прямая тройка числа, а также прямая двойная часть того же числа в num2.

Если это не так, верните 0
"""


def triple_double(*args: int) -> int:
    """Поиск подряд идущих дубликатов равных
    3-м в первом и 2-м во втором числах."""
    res = []
    for x, n in zip(map(str, args), (3, 2)):
        res.append({v for i, v in enumerate(x[:1-n]) if v * n == x[i:i+n]})

    return int(bool(set.intersection(*res)))


def test() -> None:
    """Тестирование работы алгоритмов."""

    data = (
        ((1112, 122), 0),
        ((12345, 12345), 0),
        ((10560002, 100), 1),
        ((1222345, 12345), 0),
        ((666789, 12345667), 1),
        ((451999277, 41177722899), 1),
    )

    for key, val in data:
        assert triple_double(*key) == val


if __name__ == '__main__':
    test()