"""
Популяция медведей состоит из черных медведей, бурых медведей и белых медведей.

Входные данные — массив из двух элементов.

Определите, вернется ли потомство двух медведей. 'black', 'brown', 'white', 'dark brown', 'grey', 'light brown', или 'unknown'.

Элементы массива всегда будут строкой.
Примеры:

bear_fur(['black', 'black'])  returns 'black'

bear_fur(['brown', 'brown'])  returns 'brown'

bear_fur(['white', 'white'])  returns 'white'

bear_fur(['black', 'brown'])  returns 'dark brown'

bear_fur(['black', 'white'])  returns 'grey'

bear_fur(['brown', 'white'])  returns 'light brown'

bear_fur(['yellow', 'magenta'])  returns 'unknown'


"""
import typing
import unittest


def bear_fur(bears: list[str]) -> str:
    """
    Определяет цвет при популяции медведей.
    """
    data = {
        ('black', 'black'): 'black',
        ('brown', 'brown'): 'brown',
        ('white', 'white'): 'white',
        ('black', 'white'): 'grey',
        ('black', 'brown'): 'dark brown',
        ('brown', 'white'): 'light brown',
    }
    return data.get(tuple(sorted(bears)), 'unknown')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(bear_fur, (
        (['black', 'black'], 'black'),
        (['white', 'white'], 'white'),
        (['brown', 'brown'], 'brown'),
        (['black', 'brown'], 'dark brown'),
        (['black', 'white'], 'grey'),
        (['white', 'brown'], 'light brown'),
        (['pink', 'black'], 'unknown'),
    ))
