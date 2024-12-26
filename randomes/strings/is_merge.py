"""
На собеседовании вам предстоит написать алгоритм, проверяющий,
соответствует ли заданная строка s, может быть сформирован из
двух других строк, part1 и part2.

Ограничение состоит в том, что символы в part1 и part2 должно
быть в том же порядке, что и в s.

Интервьюер приводит вам следующий пример и предлагает выяснить
остальное из данных тестовых случаев.

Например:

'codewars' is a merge from 'cdw' and 'oears':

    s:  c o d e w a r s   = codewars
part1:  c   d   w         = cdw
part2:    o   e   a r s   = oears
"""


import re


def is_merge(s: str, p1: str, p2: str):
    """
    Проверят возможно ли соединив 2 строки получить третье, не изменяя последовательности символов.
    """
    x, z = [p1, p2], '(.*)'
    for i in range(2):
        for j in range(2):
            r = f'(.*{["", "?"][j]})'.join([[f'\\{x}', x][x.isalpha() or x.isdigit()] for x in x[i]])
            if ''.join(re.split('%s%s%s' % (z, r, z), s)) == x[not i]:
                return True
    return False



def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (('codewars', 'code', 'wars'), True),
        (('codewars', 'cdw', 'oears'), True),
        (('codewars', 'cod', 'wars'), False),
    )
    for key, val in data:
        assert is_merge(*key) == val


if __name__ == '__main__':
    test()
