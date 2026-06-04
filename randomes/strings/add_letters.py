"""
Ваша задача — сложить буквы, равные одной букве.

Функции будет передано переменное количество аргументов,
каждый из которых представляет собой букву для добавления.
Примечания:

    Буквы всегда будут строчными.
    Буквы могут выходить за пределы текста (см. предпоследний пример описания).
    Если буквы не указаны, функция должна вернуть 'z'

Примеры:

add_letters('a', 'b', 'c') = 'f'
add_letters('a', 'b') = 'c'
add_letters('z') = 'z'
add_letters('z', 'a') = 'a'
add_letters('y', 'c', 'b') = 'd' # notice the letters overflowing
add_letters() = 'z'


"""
import unittest
from typing import Any, Callable, Tuple


def add_letters(*letters: str) -> str:
    """
    Складывает буквы в 1 букву.
    """
    return chr((sum(ord(x) - 96 for x in letters) % 26 or 26) + 96)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(add_letters, (
        (['a', 'b', 'c'], 'f'),
        (['z'], 'z'),
        (['a', 'b'], 'c'),
        (['c'], 'c'),
        (['z', 'a'], 'a'),
        (['y', 'c', 'b'], 'd'),
        ([], 'z'),
    ))
