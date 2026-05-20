"""
Предположим, у меня есть большой лист бумаги, и я хочу нарисовать. nколичество grids
Просто сложив его (см. пример). Сколько раз мне нужно его сложить, чтобы получить...? n
количество grids.
например.

n=1 , 0 operation, the original paper is one grid.

n=2, 1 operations, i have to fold it 1 time to get 2 grids (A,B).

 _______
|   |   |
| A | B |
|   |   |
|   |   |
|___|___|

Исключений нет, все входные данные допустимы, за исключением некоторых встроенных.
Math функции будут иметь NOЗдесь есть электропитание.



"""
import unittest
from typing import Any, Callable, Tuple


def number_of_folds(n: int) -> int:
    """
    Определяет какое кол-во раз необходимо свернуть бумагу, что бы получить сетку заданных размеров.
    """
    return next(i for i in range(n) if n <= 2 ** i)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(number_of_folds, (
        (1,  0),
        (2,  1),
    ))
