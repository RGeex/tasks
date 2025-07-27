"""
Вам дана строка nстроки, каждая подстрока которых является nсимволы длинные.
Например:

s = "abcd\nefgh\nijkl\nmnop"

Мы изучим «горизонтальное» и «вертикальное» масштабирование этого квадрата
струн.

Горизонтальное масштабирование строки по k состоит из копирования k раз
каждый символ строки (кроме '\n').

    Пример: 2-горизонтальное масштабирование
    s: => "aabbccdd\neeffgghh\niijjkkll\nmmnnoopp"

V-вертикальное масштабирование строки состоит из репликации vраз каждую часть
квадрата строки.

    Пример: 2-вертикальное масштабирование
    s: => "abcd\nabcd\nefgh\nefgh\nijkl\nijkl\nmnop\nmnop"

Функция scale(strng, k, v)выполнит k-горизонтальное масштабирование и
v-вертикальное масштабирование.

Example: a = "abcd\nefgh\nijkl\nmnop"
scale(a, 2, 3) --> "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"

Напечатано:

abcd   ----->   aabbccdd
efgh            aabbccdd
ijkl            aabbccdd
mnop            eeffgghh
                eeffgghh
                eeffgghh
                iijjkkll
                iijjkkll
                iijjkkll
                mmnnoopp
                mmnnoopp
                mmnnoopp

Задача:

    Функция записи scale(strng, k, v) k и v будут положительными целыми
    числами. Если strng == "" возвращаться "".
"""
import typing
import unittest


def scale(st: str, k: int, v: int) -> str:
    """
    Масштабирует строку горизонтально и вертикально.
    """
    return st and '\n'.join([b for a in [[''.join(x * [1, k][x != '\n'] for x in w)] * v for w in st.split('\n')] for b in a])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(scale, (
        (("abcd\nefgh\nijkl\nmnop", 2, 3), "aabbccdd\naabbccdd\naabbccdd\neeffgghh\neeffgghh\neeffgghh\niijjkkll\niijjkkll\niijjkkll\nmmnnoopp\nmmnnoopp\nmmnnoopp"),
        (("", 5, 5), ""),
        (("Kj\nSH", 1, 2),"Kj\nKj\nSH\nSH"),
        (("lxnT\nqiut\nZZll\nFElq", 1, 2), "lxnT\nlxnT\nqiut\nqiut\nZZll\nZZll\nFElq\nFElq"),
        (("YVjosW\nHGhKGZ\nLHNMLm\nJtcWCj\ngVtjyk\nOJBkOK", 2, 2), "YYVVjjoossWW\nYYVVjjoossWW\nHHGGhhKKGGZZ\nHHGGhhKKGGZZ\nLLHHNNMMLLmm\nLLHHNNMMLLmm\nJJttccWWCCjj\nJJttccWWCCjj\nggVVttjjyykk\nggVVttjjyykk\nOOJJBBkkOOKK\nOOJJBBkkOOKK"),
        (("YVjosW\nHGhKGZ\nLHNMLm\nJtcWCj\ngVtjyk\nOJBkOK", 1, 2), "YVjosW\nYVjosW\nHGhKGZ\nHGhKGZ\nLHNMLm\nLHNMLm\nJtcWCj\nJtcWCj\ngVtjyk\ngVtjyk\nOJBkOK\nOJBkOK"),
        (("WgaB\nMmIn\nqJwv\nAhho", 2, 1), "WWggaaBB\nMMmmIInn\nqqJJwwvv\nAAhhhhoo"),
        (("CG\nla", 2, 3), "CCGG\nCCGG\nCCGG\nllaa\nllaa\nllaa")  ,
    ))
