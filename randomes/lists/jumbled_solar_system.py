"""
ЗАДАЧА
Дана вся Солнечная система в виде списка. Верните новый список, содержащий либо '<', '>' или
'='В зависимости от того, меньше ли эта планета, чем планета слева от неё, или нет.
Сравнивать нужно начинать со второго элемента, потому что у первого слева ничего нет.

Однако в Солнечной системе также есть астероиды. Все астероиды меньше всех планет.
Если два астероида находятся рядом друг с другом, то крайний левый будет зависеть от небесного тела,
расположенного слева от него. Тот, что справа, будет иметь '='.

Солнечная система может оказаться пустой.

Небесные тела расположены в порядке возрастания размера:

Asteroid < Pluto < Mercury < Mars < Venus < Earth < Neptune < Uranus < Saturn < Jupiter

Важно: карликовая планета Плутон также входит в Солнечную систему.
ПРИМЕРЫ

["Mars", "Asteroid", "Venus", "Jupiter", "Asteroid", "Earth", "Pluto"] -> ['<', '>', '>', '<', '>', '<']
# Asteriod is '<' Mars
# Venus is '>' any Asteroid
# Jupiter is '>' Venus
# Any Asteroid is '<' Jupiter
# Earth is '>' the Asteroid
# Finally, Pluto, being a dwarf planet, is '<' Earth

["Asteroid", "Asteroid", "Asteroid", "Earth", "Jupiter"] -> ['=', '=', '>', '>']
# Here, the Asteroid is '=' to the Asteroid on its left
# Again, it is '=' because there is another Asteroid on its left
# Earth is '>' than the Asteroid
# Finally, Jupiter, being the king of the planets, is '>' than Earth

["Mercury", "Venus", "Earth", "Mars", "Asteroid", "Jupiter", "Saturn", "Uranus", "Neptune", "Asteroid", "Pluto"] -> ['>', '>', '<', '<', '>', '<', '<', '<', '<', '>']
# Atleast here the Solar System is how it's supposed to be!

ПРИМЕЧАНИЯ

    За исключением астероидов, никогда не будет больше одного экземпляра чего-либо.

    Солнечная система никогда не будет содержать ничего за её пределами:

["Asteroid", "Pluto", "Mercury", "Mars", "Venus", "Earth", "Neptune", "Uranus", "Saturn", "Jupiter"]
"""
import unittest
from typing import Any, Callable, List, Tuple


def jumbled_solar_system(solar_system: List[str]) -> List[str]:
    """
    Определяет отношение планеты и соседа слева.
    """
    system = ["Asteroid", "Pluto", "Mercury", "Mars", "Venus", "Earth", "Neptune", "Uranus", "Saturn", "Jupiter"]

    def sol(a: int, b: int) -> str:
        return {b < a: '<', b > a: '>'}.get(True, '=')

    return [sol(*map(system.index, x)) for x in zip(solar_system, solar_system[1:])]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(jumbled_solar_system, (
        ([], []),
        (['Venus', 'Jupiter', 'Mercury'], ['>', '<']),
        (['Earth'], []),
        (['Saturn', 'Venus', 'Mars', 'Pluto', 'Asteroid'], ['<', '<', '<', '<']),
        (['Asteroid', 'Neptune', 'Jupiter', 'Saturn'], ['>', '>', '<']),
        (['Venus', 'Mars', 'Neptune', 'Uranus', 'Earth', 'Jupiter', 'Mercury'], ['<', '>', '>', '<', '>', '<']),
        (['Pluto', 'Neptune', 'Mercury', 'Venus', 'Uranus', 'Mars', 'Earth', 'Jupiter', 'Asteroid', 'Saturn', 'Asteroid', 'Asteroid', 'Asteroid', 'Asteroid'], ['>', '<', '>', '>', '<', '>', '>', '<', '>', '<', '=', '=', '=']),
    ))
