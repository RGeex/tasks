"""
В этой ката вам нужно перевести минуты ( int) в часы и минуты в формате hh:mm( string).

Если входные данные 0Если значение отрицательное, то следует вернуть "00:00"

Подсказка: для решения этой задачи используйте операцию по модулю.
Операция по модулю просто возвращает остаток от деления. Например,
остаток от деления 5 на 2 равен 1, поэтому 5 по модулю 2 равно 1.
Пример

Если входные данные 78тогда вам следует вернуться "01:18"Потому что 78 минут — это 1 час и 18 минут.

Удачи! :D


"""
import unittest
from typing import Any, Callable, Tuple


def time_convert(num: int) -> str:
    """
    Определяет кол-во часов и минут в заданном кол-ве минут.
    """
    return f'{(num > 0 and num) // 60:0>2}:{(num > 0 and num) % 60:0>2}'


def time_convert_2(num: int) -> str:
    """
    Определяет кол-во часов и минут в заданном кол-ве минут.
    """
    return '{:02}:{:02}'.format(*divmod(num > 0 and num, 60))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(time_convert, (
        (0, '00:00'),
        (-6, '00:00'),
        (8, '00:08'),
        (32, '00:32'),
        (75, '01:15'),
        (63, '01:03'),
        (134, '02:14'),
        (180, '03:00'),
        (970, '16:10'),
        (565757, '9429:17'),
    ))
    test(time_convert_2, (
        (0, '00:00'),
        (-6, '00:00'),
        (8, '00:08'),
        (32, '00:32'),
        (75, '01:15'),
        (63, '01:03'),
        (134, '02:14'),
        (180, '03:00'),
        (970, '16:10'),
        (565757, '9429:17'),
    ))
