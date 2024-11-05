"""
Задача:

В этом ката предлагается создать собственный интерпретатор эсоланга для языка
MiniBitMove . MiniBitMove имеет только две команды и работает с массивом
битов. Это работает следующим образом:

    1: перевернуть бит в текущей ячейке
    0: переместить селектор на 1.

Требуется два входа: программа и биты, с которыми нужно работать. Программа
возвращает измененные биты. Программа останавливается, когда селектор достигает
конца массива. В противном случае программа повторяется. Примечание. Это
означает, что если в программе нет нулей, это бесконечный цикл.

Пример программы, которая переворачивает все биты массива:

Code: 10
Bits: 11001001001010
Result: 00110110110101
"""


import re
from operator import add
from itertools import cycle


def interpreter_1(tape: str, arr: str) -> str:
    """
    Интерпретатор языка MiniBitMove.
    """
    lst = list(filter(bool, re.findall(r'1*0?', tape)))
    m, n = [(lst, lst), (lst[:-1], [lst[-1] + lst[0]] + lst[1:-1])][int(tape[-1])]
    return add(*map(''.join, [[[b, str(int(not int(b)))][a.count('1') % 2] for a, b in zip(*x)] for x in [(m, arr), (cycle(n), arr[len(m):])]]))


def interpreter_2(tape: str, arr: str) -> str:
    """
    Интерпретатор языка MiniBitMove.
    """
    i, (tap, lst) = 0, [[cycle, list][i](map(int, x)) for i, x in enumerate([tape, arr])]

    while i < len(arr):
        n = next(tap)
        lst[i], i = int([lst[i], not lst[i]][n]), i + (not n)

    return ''.join(map(str, lst))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (('10', '1100101'), '0011010'),
        (('100', '1111111111'), '0101010101'),
        (('110', '1010'), '1010'),
        (('0', '100010001'), '100010001'),
        (('101010', '111'), '000'),
    )
    for key, val in data:
        assert interpreter_1(*key) == val
        assert interpreter_2(*key) == val


if __name__ == '__main__':
    test()
