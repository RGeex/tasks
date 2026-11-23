"""
Создайте функцию, которая принимает любую сумму денег и разбивает её на минимально возможное
количество купюр. В качестве входных данных принимаются только целые числа, числа с
плавающей запятой не принимаются. Функция должна выводить последовательность,
где каждый элемент представляет собой сумму определённого типа купюр.
Последовательность будет сформирована следующим образом:

sequence[0]---> обозначает долларовые купюры

sequence[1]---> обозначает купюры номиналом 5 долларов

sequence[2]---> обозначает 10-долларовые купюры

sequence[3]---> обозначает 20-долларовые купюры

sequence[4]---> обозначает купюры номиналом 50 долларов

sequence[5]---> обозначает купюры номиналом 100 долларов

В приведенном ниже примере мы разделили 365 долларов на 1 купюру в 5 долларов,
1 купюру в 10 долларов, 1 купюру в 50 долларов и 3 купюры по 100 долларов:

365 =>  [0,1,1,0,1,3]
В следующем случае мы разделили 217 долларов на 2 однодолларовые купюры,
1 пятидолларовую купюру, 1 десятидолларовую купюру и 2 стодолларовые купюры:

217 => [2,1,1,0,0,2]
"""
import unittest
from typing import Any, Callable, Tuple


def give_change(amount: int) -> Tuple[int, int, int, int, int, int]:
    """
    Заданную сумму денег и разбивает её на минимально возможное количество купюр.
    """
    result = []
    for n in [100, 50, 20, 10, 5, 1]:
        result.append(amount // n)
        amount %= n
    return tuple(result[::-1])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(give_change, (
        (365, (0,1,1,0,1,3)),
        (217, (2,1,1,0,0,2)),
    ))
