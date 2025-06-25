"""
Вы вырастили растение, и после месяцев упорного труда пришло время пожинать плоды вашего труда.
Когда оно росло, вы добавляли воду и удобрения и поддерживали постоянную температуру.
Пришло время проверить, насколько выросло ваше растение.

Растение изображается горизонтально, от основания налево, до конца направо:

---@---@---@

Основа представлена ​​дефисами. -, а цветы представлены символами. Растение всегда начинается со
стебля и всегда заканчивается цветами.

Будут даны четыре параметра. Четыре параметра:

    seed(строка) - определяет тип цветков, образуемых растением.
    water(целое число) - каждая единица воды удлиняет часть стебля между цветами. Это также дает,
    сколько раз стебли + соцветия должны повторяться
    fert(целое число) - каждая единица удобрения увеличивает количество цветов, сгруппированных в
    соцветия
    temp(целое число) - если заданная температура находится в диапазоне от 20°C до 30°C, растение
    растет нормально, в противном случае все цветки погибают, за исключением одного цветка на
    конце стебля.

Учитывая указанные выше параметры, ваша задача — вернуть строку, представляющую растение.
Примеры

plant("@", 3, 3, 25) => "---@@@---@@@---@@@"
# Water gives the length of the stem portions between flowers
# Water also gives the total number of segments(number of times flowers + stems should be repeated)
# Fertilizer gives the length of the flower clusters.
# Temperature is in the range of 20°C and 30°C

plant("$", 4, 2, 30) => "----$$----$$----$$----$$"

plant("&", 1, 5, 20) => "-&&&&&"

plant("^", 3, 3, 35) => "---------^"
# The temperature is not in the correct range, so all flowers die, except the last one at the end.
# The stem is not affected by the temperature

Примечания

    Пограничные условия не будут проверяться, то есть параметры воды или удобрения или температуры
    равны нулю. Это не будет проверяться. Параметры всегда будут действительными (нуля нет).
    Температурные пределы указаны включительно (20 и 30 будут включены как 21, 22, 23, 24...)

Удачного кодирования!
"""
import typing
import unittest


def plant(seed: str, water: int, fert: int, temp: int) -> str:
    """
    Выращивает растения.
    """
    return ''.join([x + ['', seed * fert][(n := 19 < temp < 31)] for x in ['-' * water] * water]) + [seed, ''][n]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(plant, (
        ((",", 3, 7, 25), "---,,,,,,,---,,,,,,,---,,,,,,,"),
        (("+", 1, 3, 15), "-+"),
    ))
