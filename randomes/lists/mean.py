"""
Вам будет предоставлен массив, содержащий как целые числа, так и символы.

Верните массив длиной 2, в котором a[0] представляет собой среднее значение десяти целых чисел в
виде чисел с плавающей запятой. В массиве всегда будет 10 целых чисел и 10 символов. Создайте одну
строку из символов и верните её в виде a[1], сохранив исходный порядок.

lst = ['u', '6', 'd', '1', 'i', 'w', '6', 's', 't', '4', 'a', '6', 'g', '1', '2', 'w', '8', 'o', '2', '0']

Вот пример вашей налоговой декларации.

[3.6, "udiwstagwo"]


"""
import unittest
from typing import Any, Callable, List, Tuple


def mean(lst: List[str]) -> List[float | str]:
    """
    Производит заданные операции со списком.
    """
    return [''.join(x) if i else sum(map(int, ''.join(x))) / 10 for i, x in enumerate(zip(*[[x, ''][::x.isdigit() or -1] for x in lst]))]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(mean, (
        (["u", "6", "d", "1", "i", "w", "6", "s", "t", "4", "a", "6", "g", "1", "2", "w", "8", "o", "2", "0"], [3.6, "udiwstagwo"]),
        (["0", "c", "7", "x", "6", "2", "3", "5", "w", "7", "0", "y", "v", "u", "h", "i", "n", "u", "0", "0"], [3.0, "cxwyvuhinu"]),
        (["0", "u", "a", "y", "0", "a", "9", "q", "3", "v", "g", "7", "6", "4", "y", "d", "8", "6", "0", "d"], [4.3, "uayaqvgydd"]),
        (["s", "n", "9", "l", "0", "m", "i", "z", "9", "7", "y", "4", "z", "3", "3", "k", "4", "1", "0", "k"], [4.0, "snlmizyzkk"]),
        (["5", "v", "u", "k", "8", "4", "9", "b", "9", "g", "5", "z", "3", "f", "6", "u", "i", "6", "6", "t"], [6.1, "vukbgzfuit"]),
        (["1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "a", "a", "d", "d", "g", "q", "u", "v", "y", "y"], [0.9, "aaddgquvyy"]),
        (["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "a", "a", "d", "d", "g", "q", "u", "v", "y", "y"], [1.0, "aaddgquvyy"]),
    ))
