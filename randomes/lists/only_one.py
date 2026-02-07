"""
Задача: Напишите функцию, которая возвращает Trueесли ТОЛЬКО ОДИН из логических флагов равен True
в противном случае вернуть False Если логический флаг отсутствует, вернуть значение. False
Вход 	Ожидаемый результат
[] 	False
[True, False, False] 	True
[True, False, False, True] 	False
[False, False, False, False] 	False
"""
import unittest
from typing import Any, Callable, List, Tuple


def only_one(*args: List[bool]) -> bool:
    """
    ОЛпределяет является ли только 1 еэемент True.
    """
    return sum(args) == 1


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(only_one, (
        ([], False),
        ([True, False], True),
        ([False, False, False], False),
        ([True, False, False, True], False),
    ))

