"""
Неудачная сортировка — исправление ошибки #4
О нет, сортировка Тимми, похоже, не работает? Ваша задача — исправить функцию sortArray,
чтобы она сортировала все числа в порядке возрастания.
def sort_array(value):
    return "".join(sorted(value,key=lambda a: -int(a)))
"""
import unittest
from typing import Any, Callable, Tuple


def sort_array(value: str) -> str:
    """
    Сортирует строку цифр в порядке возхрастания.
    """
    return ''.join(sorted(value, key=int))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(sort_array, (
        ('12345', '12345'),
        ('54321', '12345'),
        ('34251', '12345'),
    ))
