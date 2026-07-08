"""
История

Ворону хочется пить. Он хочет найти воду.
Ворона испытывала жажду и искала воду повсюду.

Он нашёл бутылку, в которой было совсем немного воды.
Была обнаружена бутылка, в которой находилось лишь небольшое количество воды.

Уровень воды очень низкий, у него короткий рот.
Воду пить нельзя.
Горлышко бутылки очень узкое, уровень воды очень низкий, а горлышко слишком короткое,
чтобы пить воду.

Умная ворона рядом нашла несколько маленьких камней.
Положите мелкие камешки в бутылку.
Умная ворона нашла неподалеку несколько камешков и бросила их в бутылку.

В бутылке становилось всё больше камней, вода поднималась.
И наконец ворона выпила воду.
По мере того как в бутылку наполнялось все больше и больше камней, уровень воды поднимался,
и ворона наконец-то смогла напиться.
Задача

Полная функция drinkWater()/ drink_water()которая принимает пять аргументов:

bottleHeight/ $bottle_heightВысота бутылки.

bottleRadius/ $bottle_radiusРадиус бутылки.

waterHeight/ $water_heightВысота уровня воды.

crowMouth/ $crow_mouthДлина пасти вороны

littleStones/ $little_stonesМассив. Список объемов нескольких маленьких камней.

Вам нужно рассчитать, сколько камней нужно использовать, чтобы заставить ворону напиться воды
(используя только рот). Вам нужно вернуться. a list of the stones to be used
(Камень можно использовать только слева направо).

Если ворона может пить воду (нет необходимости класть камни), вернитесь. [].

Если все камни использованы, но ворона все равно не может напиться воды. Пожалуйста, вернитесь.
"The crow is dead."

Можно предположить, что бутылка имеет стандартную цилиндрическую форму.
Это поможет вам рассчитать объем.
Примеры

drinkWater(10,2,3,4,[5,6,7,8,9,10,11,12])
should return [5,6,7,8,9,10]

drinkWater(20,1,2,3,[4,5,6,7,8,9,10,11,12])
should return [4,5,6,7,8,9,10]

drinkWater(20,1,2,3,[4,5,6,7,8,9,10])
should return [4,5,6,7,8,9,10]

drinkWater(20,2,15,6,[4,5,6,7,8,9,10])
should return []

drinkWater(20,2,15,5,[4,5,6,7,8,9,10])
should return []

drinkWater(20,1,2,3,[4,5,6,7,8,9])
should return "The crow is dead."

"""
import unittest
from typing import Any, Callable, List, Tuple
import math


def drink_water(bottle_height: int, bottle_radius: int, water_height: int, crow_mouth: int, little_stones: List[int]) -> List[int] | str:
    """
    Рассчитывает, сколько камней нужно использовать, чтобы заставить ворону напиться воды.
    """
    s = (bottle_height-crow_mouth-water_height)*bottle_radius**2*math.pi
    i = 0
    while s > 0 and i < len(little_stones):
        s -= little_stones[i]
        i += 1
    return little_stones[:i] if s <= 0 else 'The crow is dead.'


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(drink_water, (
        ((10, 2, 3, 4, [5, 6, 7, 8, 9, 10, 11, 12]), [5, 6, 7, 8, 9, 10]),
        ((20, 1, 2, 3, [4, 5, 6, 7, 8, 9, 10, 11, 12]), [4, 5, 6, 7, 8, 9, 10]),
        ((20, 1, 2, 3, [4, 5, 6, 7, 8, 9, 10]), [4, 5, 6, 7, 8, 9, 10]),
        ((20, 2, 15, 6, [4, 5, 6, 7, 8, 9, 10]), []),
        ((20, 2, 15, 5, [4, 5, 6, 7, 8, 9, 10]), []),
        ((20, 1, 2, 3, [4, 5, 6, 7, 8, 9]), "The crow is dead."),
    ))
