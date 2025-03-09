"""
Учитывая строку, верните True, если первый экземпляр «x» в строке сразу же следует строке «xx».

"abraxxxas" → true
"xoxotrololololololoxxx" → false
"softX kitty, warm kitty, xxxxx" → true
"softx kitty, warm kitty, xxxxx" → false

Примечание :

    Capital X не считается появлением «X».
    Если нет "x"


"""
import typing
import unittest


def triple_x(st: str) -> bool:
    """
    Поиск в строке первого соответсвия началоному шаблону и соответствия его полному шаблону.
    """
    return st[st.find('x'):].startswith('xxx')


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(triple_x, (
        ("", False),
        ("there's no XXX here", False),
        ("abraxxxas", True),
        ("xoxotrololololololoxxx", False),
        ("soft kitty, warm kitty, xxxxx", True),
        ("softx kitty, warm kitty, xxxxx", False),
    ))
