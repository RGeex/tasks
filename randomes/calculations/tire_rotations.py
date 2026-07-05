"""
Размер шины указывается в формате "205/55R16" где:

    205→ ширина шины в миллиметрах
    55→ соотношение сторон (высота боковины в процентах от ширины)
    16→ диаметр обода в дюймах

Соотношение сторон обода и диаметра диска может быть задано следующим образом.
R, ZR, B, или D. tire-dimensions-by-code-gs-night-landscape-750.webp
Получив строку с размером шины и расстояние в километрах, верните количество оборотов шины.

Сигнатура функции:

def tire_rotations(tire_size: str, distance_km: float) -> float:

Примеры:

tire_rotations("205/55R16", 110) ≈ 55410.8047
tire_rotations("185/65ZR15", 900) ≈ 460947.5423
tire_rotations("225/45B17", 0) == 0.0

Примечания:

    Использовать π = math.pi
    1 дюйм = 25,4 мм

"""
import unittest
from typing import Any, Callable, Tuple
from math import pi
import re


def tire_rotations(tire_size: str, distance_km: float) -> float:
    """
    Определят кол-во оборотов шины.
    """
    w, a, d = map(int, re.findall(r'\d+', tire_size))
    return distance_km * 10 ** 6 / (pi * (d * 25.4 + w * a / 50))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(tire_rotations, (
        (("205/55R16", 110), 55410.80468462886),
        (("185/65ZR15", 140), 71702.9510309424),
        (("225/45R17", 0), 0),
    ))
