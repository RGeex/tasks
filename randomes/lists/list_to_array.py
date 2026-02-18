"""
Связанные списки — это структуры данных, состоящие из вложенных или связанных между собой объектов,
каждый из которых содержит одно значение и ссылку на следующий объект.

Вот пример списка:

class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
LinkedList(1, LinkedList(2, LinkedList(3)))

Напишите функцию, которая преобразует связанный список в массив, например, так:

[1, 2, 3]

Предположим, что все входные данные представляют собой допустимые списки,
содержащие как минимум одно значение. Для простоты все значения будут либо числами,
строками, либо логическими значениями (Boolean).

"""
import unittest
from typing import Any, Callable, List, Tuple


class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def list_to_array(node: LinkedList | None) -> list:
    """
    Связный список в массив.
    """
    return [node.value] + list_to_array(node.next) if node else []


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(list_to_array, (
        (LinkedList(1), [1]),
        (LinkedList(4, LinkedList(25, LinkedList(30))), [4, 25, 30]),
        (LinkedList(2, LinkedList(40, LinkedList(43, LinkedList(25, LinkedList(125))))), [2, 40, 43, 25, 125]),
    ))
