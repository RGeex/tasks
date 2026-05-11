"""
Классовая проблема - Исправление ошибки №7

О нет! Тимми ListКласс сломался! Можешь помочь Тимми и починить его класс? У Тимми... List
Он создал класс, который используется для массивов со строгим типом (которые Тимми называет списками).

Когда Тимми звонит countсвойство списка, оно по-прежнему остается в 0при добавлении товаров.

Также это не работает, когда Тимми пытается объединить рекламные объявления в цепочку, например.

my_list.add(0).add(1)


"""
import unittest
from typing import Any, Callable, Tuple


class List:
    def __init__(self, type):
        self.type = type
        self.items = []
        self.count = 0

    def add(self, item):
        if not isinstance(item, self.type):
            return "This item is not of type: %s" % str(self.type.__name__)
        self.items += [item]
        self.count += 1
        return self


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    my_list = List(str)
    test(lambda x: x, (
        (my_list.add('Hello').count, 1),
        (my_list.add(5), "This item is not of type: str"),
        (my_list.add(' ').add('World!').count, 3),
    ))
    my_list = List(int)
    test(lambda x: x, (
        (my_list.add('Hello'), "This item is not of type: int"),
        (my_list.add(5).count, 1),
        (my_list.add(8).add(9).count, 3),
    ))
