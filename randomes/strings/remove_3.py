"""
Писать

remove(text, what)

который принимает строку str( textв Python) и объект/хэш/словарь/словарь whatи возвращает
строку с удаленными символами what. Например:

remove('this is a string',{'t':1, 'i':2}) == 'hs s a string'
# remove from 'this is a string' the first 1 't' and the first 2 i's.
remove('hello world',{'x':5, 'i':2}) == 'hello world'
# there are no x's or i's, so nothing gets removed
remove('apples and bananas',{'a':50, 'n':1}) == 'pples d bnns'
# we don't have 50 a's, so just remove it till we hit end of string.

"""
import typing
import unittest


def remove(text: str, what: dict[str:int]) -> str:
    """
    Замена заданных символов указанное кол-во раз из строки.
    """
    return remove((lambda a, b: text.replace(a, '', b))(*what.popitem()), what) if what else text


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(remove, (
        (('this is a string',{'t':1, 'i':2}), 'hs s a string'),
        (('hello world',{'x':5, 'i':2}), 'hello world'),
        (('apples and bananas',{'a':50, 'n':1}), 'pples d bnns'),
        (('a',{'a':1, 'n':1}), ''),
        (('codewars',{'c':5, 'o':1, 'd':1, 'e':1, 'w':1, 'z':1, 'a':1, 'r':1, 's':1}), ''),
    ))
