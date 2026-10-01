"""
Вы когда-нибудь хотели узнать, сколько вам дней? Дополните функцию,
которая возвращает ваш возраст в днях. Дата рождения указана в следующем
порядке: year, month, day. Можете считать, что она в прошлом.

Например, если сегодня 30 ноября 2015 года, то

2015, 11, 1 => "You are 29 days old"
"""
import unittest
from typing import Any, Callable, Tuple
from datetime import date, timedelta


def age_in_days(year: int, month: int, day: int) -> str:
    """
    Вычисляет кол-во дней с рождения.
    """
    return 'You are {} days old'.format((date.today() - date(year, month, day)).days)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    today = date.today()
    bday = today - timedelta(days=2)
    test(age_in_days, (
        ((bday.year, bday.month, bday.day), 'You are 2 days old'),
    ))
    bday = today - timedelta(days=365)
    test(age_in_days, (
        ((bday.year, bday.month, bday.day), 'You are 365 days old'),
    ))
