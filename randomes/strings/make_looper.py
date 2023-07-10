"""
Функция принимает строку (ненулевой длины) в качестве аргумента.
Он возвращает функцию. Функция, которую он возвращает, будет
возвращать последовательные символы строки при последовательных
вызовах. Он начнется с начала строки, как только она достигнет конца.
"""
from typing import Callable
from itertools import cycle


class make_looper1:
    """Принимает строку в качестве аргумента, при последующих вызовах
    возвращает элементы строки зацикленно."""

    def __init__(self, string: str) -> None:
        self.string = string
        self.indexs = -1

    def __call__(self) -> str:
        self.indexs = (self.indexs + 1) % len(self.string)
        return self.string[self.indexs]


def make_looper2(string: str) -> Callable:
    """Принимает строку в качестве аргумента, при последующих вызовах
    возвращает элементы строки зацикленно."""
    index = -1

    def call():
        nonlocal index
        index = (index + 1) % len(string)
        return string[index]
    return call


def make_looper3(string: str) -> Callable:
    """Принимает строку в качестве аргумента, при последующих вызовах
    возвращает элементы строки зацикленно."""
    obj = cycle(string)
    return lambda: next(obj)


def test() -> None:
    """Тестирование работы алгоритмов."""

    string = 'abc'

    var1 = make_looper1(string)
    var2 = make_looper2(string)
    var3 = make_looper3(string)

    for x in string * 2:
        assert var1() == x
        assert var2() == x
        assert var3() == x


if __name__ == '__main__':
    test()
