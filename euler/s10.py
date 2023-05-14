"""
Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.

Найдите сумму всех простых чисел меньше двух миллионов.
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


def find_sum(num: int) -> int:
    """Поиск суммы простых чисел > num."""
    result = []
    for prime in primeses():
        if prime >= num:
            break
        result.append(prime)
    return sum(result)


def test() -> None:
    """Тестирование работы алгоритмов."""
    assert find_sum(10) == 17
    assert find_sum(2_000_000) == 142913828922


if __name__ == '__main__':
    test()
