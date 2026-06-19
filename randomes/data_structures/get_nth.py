"""
Связанные списки - получить N-й

Реализуйте GetNth()Функция, которая принимает связанный список и целочисленный индекс и
возвращает узел, хранящийся по этому индексу. Nthиндексная позиция. GetNth()Используется
система нумерации C, согласно которой первый узел имеет индекс 0, второй — индекс 1 и так далее.

Итак, список 42 -> 13 -> 666, GetNth(1)должен вернуться Node(13);

getNth(1 -> 2 -> 3 -> null, 0).data === 1
getNth(1 -> 2 -> 3 -> null, 1).data === 2

Индекс должен находиться в заданном диапазоне. [0..length-1]Если это не так, или если список пуст,
GetNth()следует сгенерировать исключение ( ArgumentExceptionна языке C#, InvalidArgumentExceptionв PHP,
Exception(на языке Java).

"""
import unittest
from typing import Any, Callable, Tuple


class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def get_nth(node: Node, index: int) -> Node:
    """
    Определяет значение связного списка по индексу.
    """
    if not isinstance(node, Node):
        raise ValueError("None linked list should throw error.")
    curr = 0
    while curr < index and node.next:
        node, curr = node.next, curr + 1
    if curr != index:
        raise ValueError("Invalid index value should throw error.")
    return node


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    linked_list = Node(1, Node(2, Node(3, None)))
    test(lambda x: x, (
        (get_nth(linked_list, 0).data, 1),
        (get_nth(linked_list, 1).data, 2),
        (get_nth(linked_list, 2).data, 3),
    ))
