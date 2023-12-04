"""
Завершить greatestProductметод так, чтобы он нашел наибольшее произведение пяти последовательных
цифр в заданной строке цифр.

Например:

greatestProduct("123834539327238239583") // should return 3240

Входная строка всегда содержит более пяти цифр.

Адаптировано из проекта Эйлера.
"""


from operator import mul
from functools import reduce


def greatest_product(st: str) -> int:
    """
    Максимальное значение произведений цифр подстроки.
    """
    return max(reduce(mul, map(int, st[x:x + 5])) for x in range(len(st) - 4))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("8538519919900634", 6561),
        ("123834539327238239583", 3240),
        ("395831238345393272382", 3240),
        ("92494737828244222221111111532909999", 5292),
        ("02494037820244202221011110532909999", 0),
    )
    for key, val in data:
        assert greatest_product(key) == val


if __name__ == '__main__':
    test()
