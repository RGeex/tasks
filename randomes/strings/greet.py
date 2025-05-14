"""
Напишите метод, который принимает один аргумент в качестве имени,
а затем приветствует это имя, пишется с заглавной буквы и заканчивается восклицательным знаком.

Пример:

"riley" --> "Hello Riley!"
"JACK"  --> "Hello Jack!"


"""
import typing
import unittest


def greet(name: str) -> str:
    """
    Функция приветствия передаваемого имени.
    """
    return f'Hello {name.capitalize()}!'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(greet, (
        ('riley', 'Hello Riley!'),
        ('molly', "Hello Molly!"),
        ('BILLY', "Hello Billy!"),
    ))
