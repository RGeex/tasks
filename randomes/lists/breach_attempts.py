"""
Система безопасности защищает сеть от попыток вторжения.

Хакеры пытаются взломать систему по одному, в указанном порядке.

У каждого хакера свой уровень мастерства.

Система изначально имеет заданный уровень безопасности.

Правила:

Для каждого хакера:

    Если уровень мастерства хакера строго превышает текущий уровень безопасности, он успешно взламывает систему.
    В противном случае система блокирует атаку и учится на ней, повышая уровень своей безопасности.

Каждая заблокированная атака повышает уровень безопасности на фиксированную величину.

Ваша задача — вернуть количество успешно выполненных нарушений .

Если массив пуст, вернуть 0.

Пример

breachAttempts([7, 6, 8, 9], 6, 2)

Начальные значения:

securityLevel = 6
increase = 2

Пошагово:

Hacker 7 vs security 6 → breach → security stays 6
Hacker 6 vs security 6 → blocked → security becomes 8
Hacker 8 vs security 8 → blocked → security becomes 10
Hacker 9 vs security 10 → blocked

Результат:

1

"""
import unittest
from typing import Any, Callable, List, Tuple


def breach_attempts(hackers: List[int], security_level: int, increase: int) -> int:
    """
    Подсчитывает кол-во успешных попыток взлома.
    """
    return ((hackers[0] > security_level) + breach_attempts(hackers[1:], security_level + (hackers[0] <= security_level and increase), increase)) if hackers else 0


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(breach_attempts, (
        (([7, 6, 8, 9], 6, 2), 1),
        (([10, 11, 12], 5, 3), 3),
        (([5, 5, 5], 5, 1), 0),
        (([], 4, 2), 0),
    ))
