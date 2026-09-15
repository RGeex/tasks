"""
Напишите регулярное выражение для проверки строки времени в 24-часовом формате. См. примеры, чтобы понять, что именно следует проверять:

Принял: 01:00, 1:00,00:00

Не принято: 24:00, 13:1,12:60

Необходимо проверить правильность длины и отсутствие пробелов.
"""
import unittest
from typing import Any, Callable, Tuple
import re


def validate_time(time: str) -> bool:
    """
    Проверяет правильность введенного времени.
    """
    return bool(re.match(r'^([01]?\d|2[0-3]):[0-5]\d$', time))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(validate_time, (
        ('1:00', True),
        ('13:1', False),
        ('12:60', False),
        ('12: 60', False),
        ('24:00', False),
        ('00:00', True),
        ('24o:00', False),
        ('24:000', False),
        ('', False),
        ('09:00', True),
        ('2400', False),
        ('foo12:00bar', False),
        ('010:00', False),
        ('1;00', False),
    ))
