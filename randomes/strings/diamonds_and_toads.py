"""
По мотивам сказки «Бриллианты и жабы» Шарля Перро . В этом ката вам нужно
будет выполнить функцию, которая принимает 2 аргумента:

    Строка, соответствующая тому, что говорит дочь.
    Веревочка, которая подскажет, какую фею встретила девушка.
    Это может быть good или evil.

Функция должна возвращать следующий счетчик в виде хеша:

    Если девушка встретила good сказочный:
        считать 1 ruby каждый раз, когда ты видишь r и 2 каждый раз, когда вы видите R
        считать 1 crystal каждый раз, когда ты видишь c и 2 каждый раз, когда вы видите C
    Если девушка встретила evil сказочный:
        считать 1 python каждый раз, когда ты видишь p и 2 каждый раз, когда ты видишь P
        считать 1 squirrel каждый раз, когда ты видишь s и 2 каждый раз, когда вы видите S

"""


import re
from collections import Counter


def diamonds_and_toads(s: tuple[str], z: str) -> dict:
    """
    Подсчитывает кол-во заданных букв в слове.
    """
    x, arr = (('python', 'squirrel'), ('ruby', 'crystal'))[z == 'good'], Counter(re.findall(rf'[{["PSps", "CRcr"][z == "good"]}]', s))
    return dict(zip(x, list(map(sum, zip(*[[[1, 2][a.isupper()] * b, 0][::a in 'RrPp' or -1] for a, b in arr.items()]))) or [0, 0]))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("Ruby and Crystal", "good"), {"ruby": 3, "crystal": 2 }),
        (("This string contain some Ruby and some Crystal in it", "good"), {"ruby": 4, "crystal": 3 }),
        (("Python and Squirrel", "evil"), {"python": 2, "squirrel": 2}),
        (("This string contain some Python and some Squirrel in it", "evil"), {"python": 2, "squirrel": 6 }),
    )
    for key, val in data:
        assert diamonds_and_toads(*key) == val


if __name__ == '__main__':
    test()
