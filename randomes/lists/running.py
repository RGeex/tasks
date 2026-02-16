"""
Задача

Реализуйте функцию, которая принимает список значений. lstи функция fn
в качестве аргументов и возвращает новый список, в котором i-й элемент является результатом
левостороннего приведения первого элемента. i+1элементы lst с использованием fn.

Предполагая lst[:n]синтаксис означает взятие первого nэлементы lst
Функция, которую вы должны
реализовать, должна выдавать следующий результат:

[
  reduce(lst[:1], fn),
  reduce(lst[:2], fn),
  reduce(lst[:3], fn),
  ...,
  reduce(lst, fn)
]

Снижение

Сокращение — это процесс объединения списка значений в одно значение с помощью функции.
Предполагая lst[-1]Для доступа к последнему элементу списка используется левостороннее сокращение,
эквивалентное следующему псевдокоду:

reduce(lst, fn) {
  result = lst[0]
  result = fn(result, lst[1])
  result = fn(result, lst[2])
  result = fn(result, lst[3])
  ...
  result = fn(result, lst[-1])
  return result
}

Примеры

running([1,1,1,1], add) = [1,2,3,4]
running([10,3,4,1], sub) = [10,7,3,2]
running([1,9,2,10], max) = [1,9,9,10]
running([1,9,2,10], min) = [1,1,1,1]


"""
import unittest
from typing import Any, Callable, List, Tuple


def running(lst: List[int], fn: Callable[[int, int], int]) -> List[int]:
    """
    Производит операции над списком по заданой функции.
    """
    return [t := (fn(t, n) if i else n) for i, n in enumerate(lst)]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(running, (
        (([1, 9, 2, 10], max), [1, 9, 9, 10]),
        (([1, 9, 2, 10], min), [1, 1, 1, 1]),
    ))
