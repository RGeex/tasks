"""
Вам будет предоставлен массив чисел, представляющих высоту вашего персонажа над уровнем моря через
равные промежутки времени:

    Положительные числа обозначают высоту над уровнем воды.
    0 — это уровень моря.
    Отрицательные числа обозначают глубину под поверхностью воды.

Создайте функцию, которая возвращает значение, указывающее, выжил ли ваш персонаж после
самостоятельного погружения под воду, при условии, что ей задан массив целых чисел.

    Ваш персонаж начинает игру с запасом дыхания, равным 10 , что является максимальным значением.
    При погружении под воду запас дыхания уменьшается на 2 за каждый элемент в массиве.
    Будьте осторожны! Если запас дыхания уменьшится до 0 , ваш персонаж погибнет!

    Чтобы этого избежать, вы можете восполнять запасы дыхания на 4 (максимум до 10) за каждый
    элемент в массиве, где вы находитесь на уровне моря или выше.

    Ваша функция должна возвращать Trueесли ваш персонаж выживет, и Falseесли нет.

Пример решения

[-5, -15, -4, 0, 5] ➞ True

// Breath meter starts at 10.
// -5 is below water, so breath meter decreases to 8.
// -15 is below water, so breath meter decreases to 6.
// -4 is below water, so breath meter decreases to 4.
// 0 is at sea level, so breath meter increases to 8.
// 5 is above sea level and breath meter is capped at 10 (would've been 12 otherwise).
// Character survives!

Примеры

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ➞ True

[-3, -6, -2, -6, -2] ➞ False

[2, 1, 2, 1, -3, -4, -5, -3, -4] ➞ False

"""
import unittest
from typing import Any, Callable, List, Tuple


def diving_minigame(lst: List[int], limit: int = 10) -> bool:
    """
    Определяет выживет ли персонаж погружаясь под воду.
    """
    oxg = limit
    for n in lst:
        oxg = min(limit, oxg + [4, -2][n < 0])
        if oxg <= 0:
            return False
    return True


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(diving_minigame, (
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], True),
        ([-5, -15, -4, 0, 5], True),
        ([0, -4, 0, -4, -5, -2], True),
        ([-4, -3, -4, -3, 5, 2, -5, -20, -42, -4, 5, 3, 5], True),
        ([-3, -6, -2, -6, -2], False),
        ([1, 2, 1, 2, 1, 2, 1, 2, 1, -3, -4, -5, -3, -4], False),
        ([-5, -5, -5, -5, -5, 2, 2, 2, 2, 2, 2, 2, 2], False),
        ([20, 3, 4, -20, 14, 3, 8, -18, -20, -13, 13, -14, -12, -1, 20, -6, -20, -2], False),
    ))
