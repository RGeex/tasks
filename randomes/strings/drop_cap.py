"""
DropCaps означает, что первая буква начального слова абзаца должна быть заглавной,
а остальные — строчными, как в газете.

Но для разнообразия давайте сделаем это для каждого слова данной строки.
Ваша задача — сделать заглавными все слова, длина которых больше 2, оставив меньшие слова как есть.

*должно работать также с начальными и конечными пробелами и заглавными буквами.

"apple"            => "Apple"
"apple of banana"  => "Apple of Banana"
"one   space"      => "One   Space"
"   space WALK   " => "   Space Walk   "

Примечание: вам будет предоставлено как минимум одно слово, и вы должны принять строку в
качестве входных данных и вернуть строку в качестве выходных данных.

"""
import typing
import unittest


def drop_cap(words: str) -> str:
    """
    Делает заглавными слова длиной более 2 символов, остально оставляет как есть.
    """
    return ' '.join([x, x.capitalize()][2 < len(x)] for x in words.split(' '))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(drop_cap, (
        ('', ''),
        ('apple', 'Apple'),
        ('one   space', 'One   Space'),
        ('apple of banana', 'Apple of Banana'),
        ('   space WALK   ', '   Space Walk   '),
    ))
