"""
В наборе 8 шаров, пронумерованных от 0 до 7. Семь из них имеют одинаковый вес. Один тяжелее.
Ваша задача — найти его вес.

Ваша функция findBallполучит один аргумент - scalesобъект. scalesОбъект содержит внутренне хранимый
массив из 8 элементов (индексы 0-7), каждый из которых имеет одинаковое значение, за исключением одного,
которое больше. Он также имеет публичный метод с именем getWeight(left, right)Эта функция принимает два
массива индексов и возвращает -1, 0 или 1 в зависимости от суммы значений, найденных по переданным индексам,
которые указывают на больший, равный или меньший вес.

getWeightвозвраты:

-1если левая сковорода тяжелее

1если правая сковорода тяжелее

0если обе сковороды весят одинаково

Примеры scales.getWeight()использование:

scales.getWeight([3], [7])возвраты -1если шар 3 тяжелее шара 7, 1если мяч №7 тяжелее, или 0Эти мячи
имеют одинаковый вес.

scales.getWeight([3, 4], [5, 2])возвраты -1если вес шаров 3 и 4 больше веса шаров 5 и 2 и т. д.

Так в чем же подвох, спросите вы? Дело в том, что весы очень старые. Их можно использовать всего 4
раза, прежде чем они сломаются.
"""
import unittest
from typing import Any, Callable, List, Tuple
from operator import lt, gt


class ScaleMock:
    """
    Весы для шаров.
    """
    def __init__(self, heaviver: int) -> None:
        self.heaviver = heaviver
        self.life = 4

    def get_weight(self, arr1: List[int], arr2: List[int]) -> int:
        """
        Сравнивает веса двух груп шаров.
        """
        if not self.life:
            raise ValueError('Все 4 попытки исчерпаны, весы сломались.')
        self.life -= 1
        vals = [sum(n == self.heaviver for n in arr) for arr in (arr1, arr2)]
        return {gt(*vals): -1, lt(*vals): 1}.get(1, 0)


def find_ball(scales: ScaleMock, x: List[int] = list(range(8))) -> int:
    """
    Определяет индекс самого тяжелого шара.
    """
    return x[0] if (n:=len(x))==1 else find_ball(scales, (t:=(x[:n//2], x[n//2:]))[scales.get_weight(*t)==1])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_ball, (
        (ScaleMock(1), 1),
        (ScaleMock(2), 2),
        (ScaleMock(7), 7),
    ))
