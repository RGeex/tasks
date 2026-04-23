"""
Квадратная строка — это строка из nстрок, каждая подстрока которых nдлина в символах.
Нам даны две строки размером n в квадрате.

Например:

s1 = "abcd\nefgh\nijkl\nmnop"

s2 = "qrst\nuvwx\nyz12\n3456"

Давайте создадим новую строку strngразмера (n + 1) x nследующим образом:

    первая строка strngсодержит первый символ первой строки s1 плюс символы последней строки s2.
    Вторая строка strngсодержит первые два символа второй строки s1 плюс символы предпоследней
    строки. строка s2, за исключением последнего символа
    и так далее до n-й строки strngсодержит n символов n-й строки из s1 плюс первый символ первой
    строки s2.

Итак, у нас есть:

strng --> "a3456\nefyz1\nijkuv\nmnopq"

or printed:
abcd    qrst  -->  a3456
efgh    uvwx       efyz1
ijkl    yz12       ijkuv
mnop    3456       mnopq
"""
import unittest
from typing import Any, Callable, Tuple


def compose(s1: str, s2: str) -> str:
    """
    Преобразование строки по заданному алгоритму из 2-х предоставленных строк.
    """
    return '\n'.join(a[:i + 1] + b[:-i or None] for i, (a, b) in enumerate(zip(s1.split('\n'), s2.split('\n')[::-1])))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(compose, (
        (("byGt\nhTts\nRTFF\nCnnI", "jIRl\nViBu\nrWOb\nNkTB"), "bNkTB\nhTrWO\nRTFVi\nCnnIj"),
        (("HXxA\nTGBf\nIPhg\nuUMD", "Hcbj\nqteH\nGbMJ\ngYPW"), "HgYPW\nTGGbM\nIPhqt\nuUMDH"),
        (("tSrJ\nOONy\nsqPF\nxMkB", "hLqw\nEZuh\nmYFl\nzlYf"), "tzlYf\nOOmYF\nsqPEZ\nxMkBh"),
        (("fn\nlr", "Kz\nmO"), "fmO\nlrK"),
        (("fctRKq\nBCorKQ\nZKGbDO\nbhHohe\nUjyNSg\nPCOiuM", "elSYAB\nLQMYuN\nTzQtaM\nFutqip\nwSAjZX\nuOPhSJ"), "fuOPhSJ\nBCwSAjZ\nZKGFutq\nbhHoTzQ\nUjyNSLQ\nPCOiuMe"),
        (("qtKz\negiP\niOgb\nRqly", "ZUCx\nShBJ\nmybK\neBZA"),"qeBZA\negmyb\niOgSh\nRqlyZ"),
        (("rmNE\naFQJ\nfsNe\ntDtw", "GvqU\noJlZ\ngJxQ\nVQvX"), "rVQvX\naFgJx\nfsNoJ\ntDtwG"),
        (("RCKr\naJwU\nqEyM\nNbdP", "hxYA\nlUtD\nLFmc\nssTy"), "RssTy\naJLFm\nqEylU\nNbdPh"),
        (("lFqaEC\nITEzHC\nqaEPEb\nexhzgU\nxoxRJc\nTxqlDN", "IMpAnn\nktLyDb\nHawiQt\nNVRips\ncrKROc\nJqPpty"), "lJqPpty\nITcrKRO\nqaENVRi\nexhzHaw\nxoxRJkt\nTxqlDNI"),
        (("wEGa\nhICc\nPrvY\nCuSd", "qfYz\nwJfU\noHhO\nNxaV"), "wNxaV\nhIoHh\nPrvwJ\nCuSdq"),
    ))
