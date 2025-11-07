"""
Китайский зодиак представляет собой повторяющийся 12-летний цикл, где каждый год представлен определённым животным и его предполагаемыми атрибутами.
Лунный календарь разделён на циклы по 60 лет каждый, и каждый год представляет собой сочетание животного и стихии. Существует 12 животных и 5 стихий;
животные меняются каждый год, а стихии — каждые 2 года. Текущий цикл начался в 1984 году, году Деревянной Крысы.

Поскольку текущий календарь — григорианский, я буду использовать только годы с эпохи 1924 года. Для простоты я считаю год целиком, а не с января/февраля до конца года.

Задача
Если задан год, верните элемент и животное, которые представляет этот год («Элемент Животное»). Например, я родился в 1998 году, поэтому я «Земляной Тигр».

animals(или $animalsв Ruby) — это предварительно загруженный массив, содержащий животных в следующем порядке:

["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]

elements(или $elementsв Ruby) — это предварительно загруженный массив, содержащий элементы в следующем порядке:

["Wood", "Fire", "Earth", "Metal", "Water"]
"""
import typing
import unittest


animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
elements = ["Wood", "Fire", "Earth", "Metal", "Water"]


def chinese_zodiac(year: int) -> str:
    """
    Определяет год по китайскому календарю.
    """
    return ' '.join((elements[(year // 2 + 3) % 5], animals[(8 + year) % 12]))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(chinese_zodiac, (
        (1965, "Wood Snake"),
        (1938, "Earth Tiger"),
        (1998, "Earth Tiger"),
        (2016, "Fire Monkey"),
        (1924, "Wood Rat"),
        (1968, "Earth Monkey"),
        (2162, "Water Dog"),
        (6479, "Earth Goat"),
        (3050, "Metal Dog"),
        (6673, "Water Rooster"),
        (6594, "Wood Tiger"),
        (9911, "Metal Goat"),
        (2323, "Water Rabbit"),
        (3448, "Earth Rat"),
        (1972, "Water Rat"),
    ))
