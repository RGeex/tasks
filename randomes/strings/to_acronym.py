"""
Напишите функцию, которая принимает строку и преобразует её в аббревиатуру.

Правило составления акронимов в этой ката:

разделить строку на слова по символу пробела
взять первую букву каждого слова из заданной строки
заглавной буквой это
объединить их
Например:

Code wars -> C, w -> C W -> CW
Примечание: В заданной строке должно быть как минимум два слова!
"""
import unittest
from typing import Any, Callable, Tuple


def to_acronym(inp: str) -> str:
    """
    Строку преобразует её в аббревиатуру.
    """
    return "".join(st[0] for st in inp.upper().split())


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(to_acronym, (
        ("Code Wars", "CW"),
        ("Water Closet", "WC"),
        ("Portable Network Graphics", "PNG"),
        ("PHP: Hypertext Preprocessor", "PHP"),
        ("hyper text markup language", "HTML"),
    ))
