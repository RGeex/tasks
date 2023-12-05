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


def greatest_product1(st: str) -> int:
    """
    Максимальное значение произведений цифр подстроки.
    """
    return max(reduce(mul, map(int, st[x:x + 5])) for x in range(len(st) - 4))


def greatest_product2(st: str) -> int:
    """
    Максимальное значение произведений цифр подстроки.
    """
    r, w, z = 0, 0, 1
    for i, x in enumerate(st):
        w, z = [w, i + 5][x == '0'], [z * int(x), 1][x == '0']
        r = [r, max(r, z := z // [1, int(st[i - 5])][4 < i and w < i])][3 < i and w <= i]
    return r


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
        assert greatest_product1(key) == val
        assert greatest_product2(key) == val


if __name__ == '__main__':
    test()
