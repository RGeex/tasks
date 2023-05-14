"""
Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
Очевидно, что 6-е простое число - 13.

Какое число является 10001-м простым числом?
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


def pop_prime(N: int) -> int:
    """Поиск простого числа по его порядковому номеру в списке
    простых чисел"""
    primes = primeses()
    for _ in range(N):
        result = next(primes)
    return result


def test() -> None:
    """Тестирование работы алгоритмов."""
    assert pop_prime(6) == 13
    assert pop_prime(10001) == 104743


if __name__ == '__main__':
    test()
