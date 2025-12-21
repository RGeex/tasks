"""
Написать функцию replaceAll(Python: replace_all) который заменит все вхождения одного элемента другим.

Python / JavaScript : Функция должна работать как со строками, так и со списками.

Пример: replaceAll [1,2,2] 1 2 -> в списке [1,2,2] мы заменяем 1 на 2, чтобы получить новый список [2,2,2]

replaceAll(replaceAll(array: [1,2,2], old: 1, new: 2) // [2,2,2]


"""
import unittest
from typing import Any, Callable, Tuple, List


def replace_all(obj: str | List[int], find: str | int, replace: str | int) -> str | List[int]:
    """
    Производит замену в списке или строке по переданным аргументам.
    """
    lst = [[x, replace][find == x] for x in obj]
    return lst if isinstance(obj, list) else ''.join(lst)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(replace_all, (
        (([], 1, 2), []),
        (([1, 2, 2], 1, 2), [2, 2, 2]),
        (([1, 1, 2], 1, 2), [2, 2, 2]),
        (([1, 2, 1, 2, 1], 1, 2), [2, 2, 2, 2, 2]),
        (("Hello World", 'o', '0'), "Hell0 W0rld"),
    ))
