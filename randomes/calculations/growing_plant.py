"""
Задача

Каждый день растение растет на upSpeedметров. Каждую ночь высота этого растения уменьшается на
downSpeedиз-за недостатка солнечного тепла. Изначально высота растения составляет 0 метров.
Мы сажаем семена в начале дня. Мы хотим узнать, когда высота растения достигнет определенного уровня.
Пример

Для upSpeed = 100, downSpeed = 10 and desiredHeight = 910Результат должен быть следующим: 10.

After day 1 --> 100
After night 1 --> 90
After day 2 --> 190
After night 2 --> 180
After day 3 --> 280
After night 3 --> 270
After day 4 --> 370
After night 4 --> 360
After day 5 --> 460
After night 5 --> 450
After day 6 --> 550
After night 6 --> 540
After day 7 --> 640
After night 7 --> 630
After day 8 --> 730
After night 8 --> 720
After day 9 --> 820
After night 9 --> 810
After day 10 --> 910 

Для upSpeed = 10, downSpeed = 9 and desiredHeight = 4Результат должен быть следующим: 1.

Потому что растение достигает желаемой высоты на первый день (10 метров).

After day 1 --> 10

Ввод/вывод

    [input]целое число upSpeed

    Положительное целое число, представляющее собой суточный прирост.

    Ограничения: 5 ≤ upSpeed ≤ 100.

    [input]целое число downSpeed

    Положительное целое число, обозначающее ночное снижение уровня воды.

    Ограничения: 2 ≤ downSpeed < upSpeed.

    [input]целое число desiredHeight

    Положительное целое число, представляющее собой пороговое значение.

    Ограничения: 4 ≤ desiredHeight ≤ 1000.

    [output]целое число

    Количество дней, которое потребуется растению, чтобы достичь/превысить желаемую высоту
    (включая последний день общего подсчета).
"""
import unittest
from typing import Any, Callable, Tuple


def growing_plant(up_speed: int, down_speed: int, desired_height: int) -> int:
    """
    Подсчитывак кол-во дней необходимых, что бы растение достигло заданной стадии роста.
    """
    res, i = 0, 1
    while res < desired_height:
        res, i = res + [-down_speed, up_speed][i % 2], i + 1
    return i // 2 + bool(i % 2)


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(growing_plant, (
        ((100, 10, 910), 10),
        ((10, 9, 4), 1),
        ((5, 2, 0), 1),
        ((5, 2, 5), 1),
        ((5, 2, 6), 2),
    ))
