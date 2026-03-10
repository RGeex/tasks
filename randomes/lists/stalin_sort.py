"""
Сталин Сорт

    «Если нет человека, то нет и проблемы».

В отличие от традиционных алгоритмов сортировки, которые переставляют элементы,
Сорт Сталина радикально решает проблему беспорядка: Любой элемент, нарушающий принцип
возрастания , исключается из списка.
Задача

Реализуйте функцию stalin_sort/ stalinSort, которая принимает массив целых чисел и изменяет
его на месте , удаляя все элементы, нарушающие восходящий порядок. относительно предыдущего
сохранившегося элемента.

Все остальные элементы считаются врагами порядка и должны быть устранены.
Правила

    Первый элемент всегда остаётся неизменным.
    Каждый последующий элемент сохраняется только в том случае, если он ≥ предыдущему
    сохранившемуся элементу.
    Порядок выживших сохранен.
    Пустой массив остается неизменным.
    При желании можно распечатать. "Расстрелять!"для каждого удаленного элемента в
    стандартный вывод.

Примеры

[1, 2, 3, 4, 5]        →  [1, 2, 3, 4, 5]   (all loyal, no executions)
[5, 3, 1, 2, 4]        →  [5]                (4 executions)
[1, 2, 2, 3, 1, 4]     →  [1, 2, 2, 3, 4]   (1 execution)
[3, 1, 4, 1, 5, 9, 2]  →  [3, 4, 5, 9]      (3 executions)
[]                      →  []                (no one to purge)

    ⚠ Функция ничего не возвращает — она напрямую изменяет массив.
    
    ► Сложность: O(n) времени, O(1) пространства — в теории.
    Реальная реализация может различаться в зависимости от
    насколько эффективно ваше правительство обрабатывает документы.


"""
import unittest
from typing import Any, Callable, List, Tuple


def stalin_sort(arr: List[int]) -> None:
    """
    Сортировка по возрастанию, с удилением элементов не соответствия.
    """
    arr[:] = [n for i, n in enumerate(arr) if (x := n if (x if i else n) <= n else x) <= n]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    stalin_sort(arr := [3, 1, 4, 1, 5, 9, 2])
    test(lambda x: x, (
        (arr, [3, 4, 5, 9]),
    ))
    stalin_sort(arr := [1, 2, 3])
    test(lambda x: x, (
        (arr, [1, 2, 3]),
    ))
    stalin_sort(arr := [5, 3, 1])
    test(lambda x: x, (
        (arr, [5]),
    ))
    stalin_sort(arr := [4, 6, 2, 5, 1, 8, 7, 3] )
    test(lambda x: x, (
        (arr, [4, 6, 8]),
    ))
