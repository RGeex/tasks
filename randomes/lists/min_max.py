"""
История

У Бена есть очень простая идея, как получить прибыль: он покупает товар и продает его снова.
Конечно, это не принесло бы ему никакой прибыли, если бы он просто покупал и продавал по одной
и той же цене. Вместо этого он собирается купить товар по самой низкой возможной цене и продать
его по самой высокой.
Задача

Напишите функцию, которая возвращает как минимальное, так и максимальное число из заданного
списка/массива.
Примеры (Ввод --> Вывод)

[1,2,3,4,5] --> [1,5]
[2334454,5] --> [5,2334454]
[1]         --> [1,1]

Примечания

Все массивы или списки всегда будут содержать хотя бы один элемент, поэтому проверять их длину
не нужно. Кроме того, ваша функция всегда будет получать массив или список, вам не нужно
проверять их длину. null, undefinedили что-то подобное.

"""
import unittest
from typing import Any, Callable, List, Tuple


def min_max(lst: List[int]) -> List[int]:
    """
    Создание списка минимального и имаксимального значений списка.
    """
    return [min(lst), max(lst)]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(min_max, (
        ([1, 2, 3, 4, 5], [1, 5]),
        ([2334454, 5], [5, 2334454]),
    ))
