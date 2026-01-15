"""
Диаграмма «стебель-лист» группирует точки данных, имеющие одинаковую первую цифру,
напоминая гистограмму. Например, для входных данных [11, 35, 14, 9, 39, 23, 35]
Это может выглядеть примерно так:

stem | leaf
-----------
  0  | 9
  1  | 1 4
  2  | 3
  3  | 5 5 9

Вот несколько важных моментов, на которые следует обратить внимание:

    Любое однозначное число, например: 9, имеет 0в качестве его ствола;
    Листья расположены в порядке возрастания;
    Листья можно повторять (как, например, две пятерки в последнем ряду).

Создайте функцию с именем stem_and_leafчто, если дан список целых чисел i в качестве
входных данных ( 0 <= i <= 99Функция возвращает словарь Python, содержащий диаграмму
«стебель-лист». Каждый ключ словаря должен представлять собой «стебель», а каждое
значение — список «листьев», в соответствии с указанным выше форматом.

В приведенном выше примере результат будет следующим:

{0: [9], 1: [1, 4], 2: [3], 3: [5, 5, 9]}
"""
import unittest
from typing import Any, Callable, Dict, List, Tuple


def stem_and_leaf(data: List[int]) -> Dict[int, List[int]]:
    """
    Группирует числа по первой цифре числа.
    """
    res: Dict[int, List[int]] = {}
    for n in sorted(data, key=str):
        a, b = map(int, f'{n:0>2}')
        res.setdefault(a, [])
        res[a].append(b)
    return res


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(stem_and_leaf, (
        ([11, 35, 14, 9, 39, 23, 35], {0: [9], 1: [1, 4], 2: [3], 3: [5, 5, 9]}),
    ))
