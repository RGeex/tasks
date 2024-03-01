"""
Задача

Вам дана строка s.

Давайте вызовем подстроку sс двумя или более соседними одинаковыми буквами в группе
(например, "aa", "bbb", "cccc"...).

Давайте вызовем подстроку sс двумя или более соседними группами большая группа
(например, "aabb","bbccc"...).

Ваша задача – посчитать количество big groupsв данной строке.
Примеры

    "ccccoodeffffiiighhhhhhhhhhttttttts"=> 3

    Группы: «cccc», «oo», «ffff», «iii», «hhhhhhhhhhh», «ttttttt».

    Большие группы — это «ccccoo», «ffffiii», «hhhhhhhhhhttttttt».

    "gztxxxxxggggggggggggsssssssbbbbbeeeeeeehhhmmmmmmmitttttttlllllhkppppp"=> 2

    Большие группы:

    "xxxxxxxggggggggggggsssssssbbbbbeeeeeehhhmmmmmmm" и "ттттттлллл"

    "soooooldieeeeeer"=> 0

    Здесь нет big group.

Ввод, вывод

    [input]нить s

    Строка строчных латинских букв.

    [output]целое число

    Количество больших групп.
"""

from itertools import groupby as gb


def repeat_adjacent(s: str) -> int:
    """
    Вычисляет кол-во больших групп.
    """
    return sum(1 < len(list(v)) for k, v in gb([len(list(v)) for _, v in gb(s)], lambda x: x == 1) if not k)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("ccccoodeffffiiighhhhhhhhhhttttttts", 3),
        ("soooooldieeeeeer", 0),
        ("ccccoooooooooooooooooooooooddee", 1),
        ("wwwwaaaarrioooorrrrr", 2),
        ("gztxxxxxggggggggggggsssssssbbbbbeeeeeeehhhmmmmmmmitttttttlllllhkppppp", 2),
    )
    for key, val in data:
        assert repeat_adjacent(key) == val


if __name__ == '__main__':
    test()
