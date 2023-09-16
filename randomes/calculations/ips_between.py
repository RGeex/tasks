"""
Реализуйте функцию, которая получает два адреса IPv4 и возвращает
количество адресов между ними (включая первый, исключая последний).

Все входные данные будут действительными адресами IPv4 в виде строк.
Последний адрес всегда будет больше первого.
"""

from operator import sub
from functools import reduce


def ips_between1(start: str, end: str) -> int:
    """
    Вычисляет кол-во ip-адресов в указанном диапазоне.
    """
    return sub(*[reduce(lambda a, b: (a << 8) + b, map(int, x.split('.'))) for x in (end, start)])


def ips_between2(start: str, end: str) -> int:
    """
    Вычисляет кол-во ip-адресов в указанном диапазоне.
    """
    return sub(*[sum(int(v) * (256 ** i) for i, v in enumerate(x.split('.')[::-1])) for x in (end, start)])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (('10.0.0.0', '10.0.0.50'), 50),
        (('20.0.0.10', '20.0.1.0'), 246),
        (('13.219.145.218', '13.229.60.34'), 633416),
    )
    for key, val in data:
        assert ips_between1(*key) == val
        assert ips_between2(*key) == val


if __name__ == '__main__':
    test()
