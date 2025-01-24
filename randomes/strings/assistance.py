"""
На соревнованиях по пауэрлифтинге есть 2 помощника, которые собирают штангу для спортсменов.
Каждый из них отвечает за свою часть бара. Напишите функциональную помощь (вес) , которая
выводит, какие диски и в каком порядке следует повесить на каждом конце стержня.

Правила

Weight of barbell = 20 kg
lock = 2.5kg

Доступные диски:

red = 25 kg
blue = 20 kg
yellow = 15 kg
green = 10 kg
black = 5 kg
orange = 2.5 kg
white = 1.25 kg

Количество дисков не ограничено.

Самые тяжелые диски всегда висели в начале, и самые легкие диски висели в конце.

Если вы можете повесить минимальное количество весов на баре несколькими способами, выберите метод,
который имеет более тяжелые веса. (Проверьте последний пример)

Также у вас есть замок, этот вес 2,5 кг. Если на шее есть хотя бы один диск, то в конце стержня
должна быть замок.

Если вы не можете повесить требуемый вес, отобразите «Ошибка».

Входные данные

У вас есть доступ к одному значению - вес бара в кг. Вес может быть поплавок.

0 < weight < 500

Примеры

0 => "Error" (Because it's lower that minimum weight (20 kg))
20 => "Nothing to hang" (Because bar weight 20 kg already)
22.5 => "Error" (You can't hang disks without locks)
25 => "Only lock" (Because they weight 2.5 kg)
30 => "1 orange, lock"
35 => "1 black, lock"
50 => "1 green, 1 orange, lock"
65 => "1 blue, lock"
100 => "1 red, 1 green, 1 orange, lock"
102.5 => "1 red, 1 green, 1 orange, 1 white, lock"
103 => "Error"
345 => "6 reds, 1 green, lock" (If there are several pancakes, then it should be written in the plural)
105 => "1 red, 1 yellow, lock" ("You can't hang 2 blue and a lock because the red one is heavier than the blue one.")
"""
import typing
import unittest


def assistance(n: int) -> str:
    """
    Навешивает блины на штангу.
    """
    r, x = [], dict(zip([25, 20, 15, 10, 5, 2.5, 1.25], 'red blue yellow green black orange white'.split()))

    if n == 20:
        return "Nothing to hang"

    if n == 25:
        return "Only lock"

    if n < 25:
        return "Error"

    n = (n - 25) / 2

    for a, b in x.items():
        if t := int(n // a):
            n -= a * t
            r.append(f'{t} {b}{["", "s"][1 < t]}')

    return 'Error' if n else ', '.join(r + ['lock'])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(assistance, (
        (0, "Error"),
        (20, "Nothing to hang"),
        (22.5, "Error"),
        (25, "Only lock"),
        (30, "1 orange, lock"),
        (35, "1 black, lock"),
        (50, "1 green, 1 orange, lock"),
        (65, "1 blue, lock"),
        (100, "1 red, 1 green, 1 orange, lock"),
        (102.5, "1 red, 1 green, 1 orange, 1 white, lock"),
        (103, "Error"),
        (345, "6 reds, 1 green, lock"),
        (105, "1 red, 1 yellow, lock"),
    ))
