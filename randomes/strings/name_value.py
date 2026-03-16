"""
Дана строка "abc"Предположим, что каждая буква в строке имеет значение,
равное её позиции в алфавите. Тогда наша строка будет иметь значение,
равное... 1 + 2 + 3 = 6Это означает, что: a = 1, b = 2, c = 3 ... z = 26.

Вам будет предоставлен список строк, и ваша задача будет заключаться в том,
чтобы вернуть значения этих строк, как описано выше, умноженные на позицию каждой
строки в списке. В нашем случае позиция начинается с 1.

["abc", "abc abc"]должен вернуться [6, 24]из-за [ 6 * 1, 12 * 2 ]Обратите внимание,
что пробелы игнорируются.

"abc"имеет значение 6, пока "abc abc"имеет значение 12Теперь значение в позиции 1
умножается на 1при этом значение в позиции 2умножается на 2.

Вводимые данные будут содержать только строчные буквы и пробелы.

Удачи!

Если вам понравилась эта ката, попробуйте также: 
"""
import unittest
from typing import Any, Callable, List, Tuple


def name_value(my_list: List[str]) -> List[int]:
    """
    Вычисляет значение срок по заданному алгоритму.
    """
    return [sum(' abcdefghijklmnopqrstuvwxyz'.index(s) for s in x) * i for i, x in enumerate(my_list, 1)]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(name_value, (
        (["codewars", "abc", "xyz"], [88, 12, 225]),
        (["abc abc", "abc abc", "abc", "abc"], [12, 24, 18, 24]),
    ))
