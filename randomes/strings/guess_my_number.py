"""
Ваша задача — создать функцию, которая принимает две строки: предполагаемый номер телефона
и сам номер телефона.

Исходя из предположения, функция должна отобразить часть номера телефона:

guess_my_number('052', '123-451-2345')
would return the string: '#2#-#5#-2##5'

or

guess_my_number('142', '123-451-2345')
would return the string: '12#-4#1-2#4#'
Порядок символов в строке с предположением не имеет значения и не должен содержать дубликатов
десятизначных чисел от 0 до 9. Предположение никогда не будет пустой строкой и не будет содержать никаких других символов. Номер телефона всегда будет десятизначным числом в формате ###-###-####.

Номер по умолчанию 123-451-2345 должен быть указан, но его можно перезаписать другим номером,
если он будет предоставлен во время выполнения.
"""
import unittest
from typing import Any, Callable, Tuple


def guess_my_number(guess: str, number: str = '123-451-2345') -> str:
    """
    Заменят цифры в строке на # кроме указанных.
    """
    return "".join(["#", x][x in guess + "-"] for x in number)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(guess_my_number, (
        (('0'), '###-###-####'),
        (('01',), '1##-##1-####'),
        (('012',), '12#-##1-2###'),
        (('0123',), '123-##1-23##'),
        (('01234',), '123-4#1-234#'),
        (('012345',), '123-451-2345'),
    ))
