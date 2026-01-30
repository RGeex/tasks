"""
Данная задача основана на задаче 539 из проекта Эйлера.
Объект

Найдите последнюю цифру между 1 и n(включая) тот, который выживает после процесса исключения
Как это работает

Начните с первого числа слева, затем удаляйте каждое второе число, двигаясь вправо,
пока не дойдете до конца. Затем из оставшихся чисел начните с первого числа справа
и удаляйте каждое второе число, двигаясь влево. Повторяйте процесс, чередуя движение
влево и вправо, пока не останется только одно число,
которое вы возвращаете как «последнего выжившего».
Пример

given an input of `9` our set of numbers is `1 2 3 4 5 6 7 8 9`

start by removing from the left    2   4   6   8
                                 1   3   5   7   9


then from the right                2       6
                                       4       8


then the left again                        6
                                   2


until we end with `6` as the last man standing

"""
import unittest
from typing import Any, Callable, List, Tuple


def last_man_standing(n: int, lst: List = []) -> int:
    """
    Поиск послежднего выжившего.
    """
    return last_man_standing(n, [x for i, x in enumerate(lst or range(1, n + 1)) if i % 2][::-1]) if not lst or len(lst) > 1 else lst[0]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(last_man_standing, (
        (9, 6),
        (10, 8),
        (100, 54),
        (1000, 510),
    ))
