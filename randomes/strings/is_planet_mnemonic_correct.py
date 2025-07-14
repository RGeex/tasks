"""
О нет! Планеты снова перепутались!
О

Знаете ли вы, что существует мнемонический прием, позволяющий запомнить порядок расположения
планет в нашей Солнечной системе?

Мнемонический прием – это предложение «Моя очень эффективная мама только что угостила нас орехами»,
где M«My» означает Меркурий, V«Очень» для Венеры, E«Эффективного» для Земли и т. д.
ЗАДАЧА

Теперь, когда все планеты перемешались, некоторые люди решили придумать новую мнемонику, и ваша
задача — с помощью программы подтвердить, соответствует ли созданная ими мнемоника новой Солнечной
системе.

Итак, если Солнечная система представлена в виде списка, вам необходимо вернуть логическое значение,
которое либо Trueесли мнемоника верна или Falseесли это не так.

Однако, Asteroidего следует игнорировать, поскольку он не должен быть частью мнемоники.

Плутон никогда не станет частью Солнечной системы.
ПРИМЕРЫ

["Earth", "Jupiter", "Asteroid", "Asteroid", "Mercury", "Asteroid", "Saturn"],
"Even Jaguars Make Spaghetti" -> True
# E of "Even" stands for Earth
# J of "Jaguars" stands for Jupiter
# Asteroid is ignored
# Another Asteroid is ignored
# M of "Make" stands for Mercury
# Asteroid is ignored again
# Finally, S of "Spaghetti" stands for Saturn
# As the whole mnemonic fits the given Solar System, you have to just return True

["Asteroid", "Mars", "Uranus", "Asteroid"], "Water Melon" -> False

ПРИМЕЧАНИЯ

    Все названия планет будут начинаться с заглавной буквы, как и мнемоническое слово.
    Никогда не будет больше одного экземпляра чего-либо, кроме астероидов.
    Если Солнечная система пуста или содержит только астероиды, то пустая строка "" допустима.
    Однако "Hello" недопустимо.
    Солнечная система никогда не будет содержать ничего внешнего.
    ["Asteroid", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    Плутон никогда не станет частью Солнечной системы

"""
import re
import typing
import unittest
from itertools import zip_longest


def is_planet_mnemonic_correct_1(solar_system: list[str], mnemonic: str) -> bool:
    return all(a[0] == b[0] for a, b in zip_longest([x for x in solar_system if x != 'Asteroid'], mnemonic.split(), fillvalue=' '))


def is_planet_mnemonic_correct_2(solar_system: list[str], mnemonic: str) -> bool:
    return re.findall(r'(?!A)([A-Z])', ' '.join(solar_system)) == re.findall(r'[A-Z]', mnemonic)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(is_planet_mnemonic_correct_1, (
        ((["Earth", "Jupiter", "Asteroid", "Asteroid", "Mercury", "Asteroid", "Saturn"], "Even Jaguars Make Spaghetti"), True),
        (([], "Hello"), False),
        (([], ""), True),
        ((["Asteroid", "Asteroid", "Asteroid", "Asteroid", "Asteroid", "Asteroid"], ""), True),
        ((["Mars", "Jupiter"], "My Shoes"), False),
        ((["Mercury", "Asteroid", "Saturn"], "My Shoes"), True),
    ))
    test(is_planet_mnemonic_correct_2, (
        ((["Earth", "Jupiter", "Asteroid", "Asteroid", "Mercury", "Asteroid", "Saturn"], "Even Jaguars Make Spaghetti"), True),
        (([], "Hello"), False),
        (([], ""), True),
        ((["Asteroid", "Asteroid", "Asteroid", "Asteroid", "Asteroid", "Asteroid"], ""), True),
        ((["Mars", "Jupiter"], "My Shoes"), False),
        ((["Mercury", "Asteroid", "Saturn"], "My Shoes"), True),
    ))
