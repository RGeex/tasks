"""
Задача

Начинающему программисту дали две простые задачи: сложить и отсортировать элементы заданного
массива. arr= [ a1 , a2 , ..., an ] .

Он начал с суммирования и легко справился с этой задачей, но решил сохранить найденную сумму в
случайном месте исходного массива, что оказалось плохой идеей. Теперь ему нужно решить вторую
задачу — сортировку исходного массива arr, и это вызывает у него трудности, поскольку он его
модифицировал.

Дан массив shuffledФункция, состоящая из элементов a1 , a2 , ..., an и их суммарного значения в
случайном порядке, возвращает отсортированный массив исходных элементов a1 , a2 , ..., an .
Пример

Для shuffled = [1, 12, 3, 6, 2]Результат должен быть следующим: [1, 2, 3, 6].

1 + 3 + 6 + 2 = 12, что означает, что 1, 3, 6 и 2 являются исходными элементами массива.

Для shuffled = [1, -3, -5, 7, 2]Результат должен быть следующим: [-5, -3, 2, 7].
Ввод/вывод

    [input]целочисленный массив shuffled

    Массив, содержащий как минимум два целых числа. Гарантируется наличие индекса i такого,
    что shuffled[i] = shuffled[0] + ... + shuffled[i - 1] + shuffled[i + 1] + ... + shuffled[n].

    Ограничения:

    2 ≤ shuffled.length ≤ 30,

    -300 ≤ shuffled[i] ≤ 300.

    [output]целочисленный массив

    А sortedмассив из 1 элемента, перемешанного в разные стороны.


"""
import unittest
from typing import Any, Callable, List, Tuple


def shuffled_array(s: List[int]) -> List[int]:
    """
    Сортирует список элеменитов и удаляет из него сумму всех элементов.
    """
    return next(sorted(s) for n in s if sum(s) - n == n and not s.remove(n))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(shuffled_array, (
        ([1, 12, 3, 6, 2], [1, 2, 3, 6]),
        ([1, -3, -5, 7, 2], [-5, -3, 2, 7]),
        ([2, -1, 2, 2, -1], [-1, -1, 2, 2]),
        ([-3, -3], [-3]),
    ))
