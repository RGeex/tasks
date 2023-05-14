"""
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?

"""

from typing import Generator


def primeses() -> Generator:
    """Генератор бесконечного ряда простых чисел."""
    num = 1
    yield 2
    while True:
        num += 2
        for i in range(3, int(num ** 0.5 + 1), 2):
            if not num % i:
                break
        else:
            yield num


def get_div_num(num: int) -> list:
    """Поиск делителей числа num, являющихся простыми числами."""
    result = []
    values = int(num ** 0.5 + 1)
    for prime in primeses():
        if prime > values:
            break
        if not num % prime:
            result.append(prime)

    return result


def dvrs(*args) -> int:
    """Поиск максимального делителя числа N, являющегося простым числом."""
    return max(get_div_num(*args))


def test() -> None:
    """Тестирование работы алгоритмов."""
    assert get_div_num(13195) == [5, 7, 13, 29]
    assert dvrs(600851475143) == 6857


if __name__ == '__main__':
    test()
