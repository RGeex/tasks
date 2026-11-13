"""
Задача
Нам нужно преобразовать заданное целое число в число, имеющее только одну ненулевую цифру,
используя метод округления до последнего знака после запятой. Это означает, что на каждом
шаге мы берем последнюю ненулевую цифру числа и округляем ее до 0 или до 10.
Если она меньше 5, мы округляем ее до 0; если она больше или равна 5, мы округляем ее до
10 (округление до 10 означает увеличение следующей значащей цифры на 1). Процесс немедленно
останавливается, как только остается только одна ненулевая цифра.

Пример
При значении = 15, результат должен быть следующим.20

При значении = 1234 вывод должен быть следующим 1000: .

1234 -> 1230 -> 1200 -> 1000.

При значении = 1445 вывод должен быть следующим 2000: .

1445 -> 1450 -> 1500 -> 2000.

Ввод/вывод
[input]целое числоvalue

Положительное целое число.

Ограничения: 1 ≤ значение ≤ 10 8

[output]целое число

Округленное число.
"""
import unittest
from typing import Any, Callable, Tuple


def rounders(value: int) -> int:
    """
    Округляет число учитывая каждую цифру отдельно.
    """
    for i in range(len(str(value)) - 1):
        value += ((y := value % (10 ** (i + 1))) >= 5 * (10 ** i)) * 10 ** (i + 1) - y
    return value


def rounders_2(value: int) -> int:
    """
    Округляет число учитывая каждую цифру отдельно.
    """
    return value if value < 10 else 10 * rounders(value // 10 + (value % 10 >= 5))


def rounders_3(value: int) -> int:
    """
    Округляет число учитывая каждую цифру отдельно.
    """
    for i in range(1, len(str(value))):
        value = round(value / 10 ** i + 0.01) * 10 ** i
    return value


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(rounders, (
        (15, 20),
        (1234, 1000),
        (1445, 2000),
        (14, 10),
        (99, 100),
        (10, 10),
    ))
    test(rounders_2, (
        (15, 20),
        (1234, 1000),
        (1445, 2000),
        (14, 10),
        (99, 100),
        (10, 10),
    ))
    test(rounders_3, (
        (15, 20),
        (1234, 1000),
        (1445, 2000),
        (14, 10),
        (99, 100),
        (10, 10),
    ))
