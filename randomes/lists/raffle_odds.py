"""
Розыгрыш призов: каковы шансы?

Вы участвовали в нескольких независимых розыгрышах подряд. Каждый розыгрыш является отдельным.
Розыгрыш с одним победителем: из общего пула вытягивается один билет, и если он ваш, Ты победил.

Даны два массива одинаковой длины:

    totals— общее количество проданных билетов в каждой лотерее
    purchased— сколько билетов вы купили в каждом розыгрыше

Представьте вероятность выигрыша хотя бы в одном розыгрыше в упрощенном виде. строка дробей в виде
"numerator/denominator"Эту дробь необходимо полностью сократить, так что "4/8" превратится в "1/2", а "9/12" — в "3/4".
Подсказка по вероятности

Для независимых соревнований вероятность выигрыша хотя бы одного из них составляет в дополнение
к потере всех из них:

    P(A или B или ...) = 1 - P(!A) * P(!B) * ...

где P(!X) вероятность не выиграть в лотерею X. —
Примеры

# One raffle, 1 ticket out of 3
raffle_odds([3], [1]) # -> "1/3"

# Two raffles, 1 ticket each out of 4
raffle_odds([4,4], [1,1]) # -> "7/16"

# Three raffles
raffle_odds([2,3,6], [1,1,1]) # -> "13/16"

Примечания

    purchased[i] <= totals[i]
    Все числа в totalsявляются строго положительными целыми числами (1 или больше).
    Все числа в purchasedявляются неотрицательными (0 или выше)
    Если вы не приобрели ни одного билета в каком-либо розыгрыше, этот розыгрыш никак
    не повлияет на ваши шансы на выигрыш.
    Если вам гарантирован выигрыш в каком-либо розыгрыше, вернитесь. "1/1"
    Возвращаемая дробь должна быть полностью уменьшена.


"""
import unittest
from typing import Any, Callable, List, Tuple
from fractions import Fraction
from math import prod


def raffle_odds(totals: List[int], purchased: List[int]) -> str:
    """
    Определяет вероятность выйграть в лотерею.
    """
    return '{}/{}'.format(*str(1 - prod(1 - Fraction(*x) for x in zip(purchased, totals))).split('/') + ['1'])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(raffle_odds, (
        (([3], [1]), '1/3'),
        (([4, 4], [1, 1]), '7/16'),
        (([2, 3, 6], [1, 1, 1]), '13/18'),
        (([5], [5]), '1/1'),
        (([5, 3], [5, 1]), '1/1'),
        (([4, 4], [0, 0]), '0/1'),
        (([4, 4], [1, 0]), '1/4'),
        (([4, 4], [2, 2]), '3/4'),
        (([1], [1]), '1/1'),
        (([3, 5, 7], [3, 5, 7]), '1/1'),
        (([10, 10], [1, 1]), '19/100'),
    ))
