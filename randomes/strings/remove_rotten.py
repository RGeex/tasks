"""
У нашего фруктового парня есть мешок с фруктами (представленный в виде массива строк),
где некоторые фрукты гнилые. Он хочет заменить все гнилые кусочки фруктов свежими.
Например, учитывая ["apple","rottenBanana","apple"]замененный массив должен быть
["apple","banana","apple"]Ваша задача — реализовать метод, который принимает массив
строк, содержащих фрукты, и должен возвращать массив строк, где все гнилые фрукты заменены хорошими.

Примечания

    Если массив равен null/nil/None или пуст, следует вернуть пустой массив ( []).
    Название гнилого фрукта будет в этом верблюжьем ящике ( rottenFruit).
    Возвращаемый массив должен быть в нижнем регистре.
"""
import typing
import unittest


def remove_rotten(bag_of_fruits: list[str]) -> list[str]:
    """
    Убирает гнилые кусочи фруктов.
    """
    return [x.replace('rotten', '').lower() for x in bag_of_fruits] if isinstance(bag_of_fruits, list) else []


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(remove_rotten, (
        (["rottenApple","rottenBanana","rottenApple","rottenPineapple","rottenKiwi"], ["apple","banana","apple","pineapple","kiwi"]),
        ([], []),
    ))
