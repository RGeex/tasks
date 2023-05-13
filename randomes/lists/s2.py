"""
Имеются гири: 1 г, 2 г, …, N г . Напишите программу,
распределяющую эти гири на max. кол-во пар, чтобы
вес гирь в каждой паре было простым числом.
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


def get_primes_list(num: int) -> list:
    """Генерирует список простых чисел не более num."""
    primes = []
    for prime in primeses():
        if prime > num:
            break
        primes.append(prime)
    return primes


def func(num: int) -> list:
    """Распределяет числа от 1 до num по парам чисел,
    сумма которых простое число."""

    result = []
    primes = get_primes_list(num * 2)

    for i in range(1, num):
        if i in result:
            continue
        for j in range(i + 1, num + 1):
            if j in result:
                continue
            if i + j in primes:
                result.extend((i, j))
                break

    return [result[i:i+2]for i in range(0, len(result), 2)]


def test() -> None:
    """Тестирование работы алгоритмов."""
    assert func(9) == [[1, 2], [3, 4], [5, 6], [8, 9]]
    assert func(10) == [[1, 2], [3, 4], [5, 6], [7, 10], [8, 9]]


if __name__ == '__main__':
    test()
