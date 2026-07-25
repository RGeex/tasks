"""
Музей невероятно скучных вещей
Музей невероятно скучных вещей хочет избавиться от некоторых экспонатов.
Мириам, архитектор интерьеров, придумывает план по удалению самых неинтересных
экспонатов. Она присваивает им рейтинг, а затем убирает тот, у которого самый
низкий рейтинг.

Однако, как только она закончила оценивать все экспонаты, она отправляется на
важную выставку, поэтому просит вас написать программу, которая сообщит ей
рейтинги экспонатов после удаления самого низкого. Вполне справедливо.

Задача
Дана последовательность целых чисел. Удалите наименьшее значение из массива.
Не изменяйте исходный массив/список. Если есть несколько элементов с одинаковым
значением, удалите тот, у которого наименьший индекс. Если получен пустой
массив/список, верните пустой массив/список.

Не меняйте порядок оставшихся элементов.

Примеры
* Input: [1,2,3,4,5], output = [2,3,4,5]
* Input: [5,3,2,1,4], output = [5,3,2,4]
* Input: [2,2,1,2,1], output = [2,2,2,1]


"""
import unittest
from typing import Any, Callable, List, Tuple


def remove_smallest(numbers: List[int]) -> List[int]:
    """
    Удаляет минимальный элемент из списка, не изменяя исходный список.
    """
    min_index = (numbers or [0]).index(min(numbers or [0]))
    return numbers[:min_index] + numbers[min_index + 1:]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(remove_smallest, (
        ([1, 2, 3, 4, 5], [2, 3, 4, 5]),
        ([5, 3, 2, 1, 4], [5, 3, 2, 4]),
        ([1, 2, 3, 1, 1], [2, 3, 1, 1]),
        ([], []),
    ))
