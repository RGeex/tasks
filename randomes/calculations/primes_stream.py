"""
Создайте бесконечный генератор, выдающий простые числа.
Генератор должен быть в состоянии произвести миллион простых чисел за несколько секунд.
"""

import itertools as it
from typing import Generator


class Primes:
    """
    Простые числа.
    """
    @staticmethod
    def stream1() -> Generator:
        """
        Бесконечный генератор простых чисел.
        """
        x = 1
        while True:
            x += 2 if 2 < x else 1
            if next((0 for n in range(3, int(x ** .5) + 1, 2) if not x % n), 1):
                yield x

    @staticmethod
    def stream2() -> Generator:
        """
        Бесконечный генератор простых чисел.
        """
        D = {}
        yield 2
        for q in it.islice(it.count(3), 0, None, 2):
            p = D.pop(q, None)
            if p is None:
                D[q*q] = q
                yield q
            else:
                x = q + 2*p
                while x in D:
                    x += 2*p
                D[x] = p

    @staticmethod
    def stream3() -> Generator:
        """
        Бесконечный генератор простых чисел.
        """
        D = {9: 3, 25: 5}
        yield 2
        yield 3
        yield 5
        MASK = 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0,
        MODULOS = frozenset((1, 7, 11, 13, 17, 19, 23, 29))

        for q in it.compress(
                it.islice(it.count(7), 0, None, 2),
                it.cycle(MASK)):
            p = D.pop(q, None)
            if p is None:
                D[q*q] = q
                yield q
            else:
                x = q + 2*p
                while x in D or (x % 30) not in MODULOS:
                    x += 2*p
                D[x] = p


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    def verify(from_n, *vals: int) -> None:
        stream1 = Primes.stream1()
        stream2 = Primes.stream2()
        stream3 = Primes.stream3()

        for _ in range(from_n):
            next(stream1)
            next(stream2)
            next(stream3)

        for v in vals:
            assert next(stream1) == v
            assert next(stream2) == v
            assert next(stream3) == v

    verify(0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    verify(10, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71)
    verify(100, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601)
    verify(1000, 7927, 7933, 7937, 7949, 7951, 7963, 7993, 8009, 8011, 8017)


if __name__ == '__main__':
    test()
