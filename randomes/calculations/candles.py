"""
Задача

Когда свеча догорает, остается остаток. Из остатков можно сделать новую свечу, которая, догорев,
оставит еще один остаток.

У вас есть количество свечей. Какое общее количество свечей вы можете сжечь, предполагая,
что вы будете зажигать новые свечи, как только у вас останется достаточное количество?
Пример

При candlesNumber = 5 и makeNew = 2, результат должен быть следующим: 9.

Вот что вы можете сделать, чтобы сжечь 9 свечей:

Сожгите 5 свечей, получите 5 остатков;
Создайте еще 2 свечи, используя 4 оставшихся (1 оставшаяся);
Сжечь 2 свечи, в итоге останется 3 лишние;
Создайте еще одну свечу, используя 2 оставшихся свечи (1 оставшаяся свеча останется);
Сожгите получившуюся свечу, в результате чего останется еще одна (всего 2 лишние свечи);
Сделайте свечу из оставшихся остатков;
Сожгите последнюю свечу.
Таким образом, вы можете сжечь 5 + 2 + 1 + 1 = 9 свечей, что и является ответом.

Ввод/вывод

    [input]целое число candlesNumber

    Количество свечей, которыми вы располагаете.

    Ограничения: 1 ≤ количество свечей ≤ 50.

    [input]целое число makeNew

    Количество остатков, которые можно использовать для создания новой свечи.

    Ограничения: 2 ≤ makeNew ≤ 5.

    [output]целое число
"""
import unittest
from typing import Any, Callable, Tuple


def candles(candles_number: int, make_new: int, x: int = 0) -> int:
    """
    Определяет кол-во свечей которые можно сжечь.
    """
    n, x = divmod(candles_number + x, make_new)
    return int(candles_number) + (candles(n, make_new, x) if n or x >= make_new else 0)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(candles, (
        ((5, 2), 9),
        ((1, 2), 1),
        ((3, 3), 4),
        ((11, 3), 16),
    ))
