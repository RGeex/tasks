"""
Начнём с примера:

Возьмите номерок: 56789Поверните влево, и получите 67895.

Оставьте первую цифру на месте, а остальные цифры поверните влево: 68957.

Оставьте первые две цифры на месте, а остальные поверните: 68579.

Сохраните первые три цифры, а остальные поверните влево: 68597. Теперь все кончено, поскольку,
сохранив первые четыре цифры, осталась только одна цифра, которая Повернутое — это само по себе.

У вас есть следующая последовательность чисел:

56789 -> 67895 -> 68957 -> 68579 -> 68597

и вы должны вернуть величайшее: 68957.
Задача

Писать function max_rot(n)которое дано положительное целое число nВозвращает максимальное число,
полученное при выполнении вращений, аналогичных приведенному выше примеру.

Так max_rot (или maxRotили ... (в зависимости от языка) это может выглядеть так:

    max_rot(56789) should return 68957

    max_rot(38458215) should return 85821534
"""
import unittest
from typing import Any, Callable, Tuple


def max_rot(n: int) -> int:
    """
    Определяет максимальное число при переворачивании всех цифр числа.
    """
    return max([n] + [n := int(str(n)[:i] + str(n)[i + 1:] + str(n)[i]) for i in range(len(str(n)) - 1)])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(max_rot, (
        (56789, 68957),
        (38458215, 85821534),
        (195881031, 988103115),
        (896219342, 962193428),
        (69418307, 94183076),
    ))
