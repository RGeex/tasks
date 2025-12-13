"""
Создать циклический список

Циклический список имеет конечный размер, но из него бесконечно можно запрашивать предыдущий и
следующий элементы. Это происходит потому, что он ведет себя так, как будто соединен на концах
и зацикливается.

Например, представьте себе кольцевой список (CircularList), состоящий из [1, 2, 3, 4]Пять призывов
next()Последовательно должны возвращаться 1, 2, 3, 4, а затем снова 1. На этом этапе пять вызовов
prev()В ряду должны возвращаться 4, 3, 2, 1, а затем снова 4.

Ваш CircularList создается путем передачи параметра с переменным числом аргументов, например: new
CircularList(1, 2, 3)В коде конструктора/инициализации списка, если ничего не передано, должно быть
выброшено исключение.

"""
import unittest
from typing import Any, Callable, List, Tuple


class CircularList():
    """
    Зацикливает переданные аргументы.
    """
    def __init__(self, *args) -> None:
        if not args:
            raise ValueError('there must be at least 1 argument')
        self.lst: List[Any] = args
        self.index: int | None = None

    def next(self) -> Any:
        """
        Следующий элемент зацикленного списка.
        """
        self.index = ((self.index or 0) + (self.index is not None)) % len(self.lst)
        return self.lst[self.index]

    def prev(self) -> Any:
        """
        Предыдущий элемент зацикленного списка.
        """
        self.index = ((self.index or 0) - 1) % len(self.lst)
        return self.lst[self.index]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    list = CircularList("one", "two", "three")
    test(list.next, (
        ((), "one"),
        ((), "two"),
        ((), "three"),
        ((), "one"),
        ((), "two"),
        ((), "three"),
    ))
    list = CircularList("one", "two", "three")
    test(list.prev, (
        ((), "three"),
        ((), "two"),
        ((), "one"),
        ((), "three"),
        ((), "two"),
        ((), "one"),
    ))
