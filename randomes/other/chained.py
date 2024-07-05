"""
Ваша задача — написать функцию более высокого порядка для объединения в
цепочку. список унарных функций. Другими словами, он должен возвращать
функцию который выполняет складку влево для заданных функций.

chained([a,b,c,d])(input)

Должен дать тот же результат, что и

d(c(b(a(input))))
"""

from typing import Callable


def chained(x: list) -> Callable:
    """
    Складывает в цепочку переданные функции.
    """
    return lambda n: chained(x)(x.pop(0)(n)) if x else n


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    def f1(x): return x*2
    def f2(x): return x+2
    def f3(x): return x**2
    def f4(x): return x.split()
    def f5(xs): return [x[::-1].title() for x in xs]
    def f6(xs): return "_".join(xs)

    data = (
        ((([f1,f2,f3]), 0), 4),
        ((([f1,f2,f3]), 2), 36),
        ((([f3,f2,f1]), 2), 12),
        ((([f4,f5,f6]), "lorem ipsum dolor"), "Merol_Muspi_Rolod"),
    )
    for (x1, x2), val in data:
        assert chained(x1)(x2) == val


if __name__ == '__main__':
    test()
