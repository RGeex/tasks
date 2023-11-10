"""
Введение

Идет война и никто не знает - война алфавита!
Письма прячутся в своих ядерных убежищах. Ядерные удары поразили поле боя и убили многих из них.
Задача

Напишите функцию, которая принимает battlefieldстрока и возвращает буквы, пережившие ядерный удар.

    The battlefieldстрока состоит только из маленьких букв, #, [и ].
    Ядерное убежище представлено квадратными скобками. []. Буквы в квадратных скобках обозначают
    буквы внутри убежища.
    The #означает место, где ядерный удар пришелся на поле боя. Если есть хотя бы один #на поле боя
    все письма за пределами убежища погибают. Когда нет никакого #на поле боя все буквы сохраняются
    (но не ожидайте такого сценария слишком часто ;-P ).
    Убежища обладают некоторой прочностью. Когда 2 и более #удар близко к укрытию, укрытие
    разрушается и все буквы внутри испаряются. «Рядом с укрытием» означает место на земле между
    укрытием и следующим укрытием (или началом/концом поля боя). Приведенные ниже примеры прояснят
    вам ситуацию.

Пример

abde[fgh]ijk     => "abdefghijk"  (all letters survive because there is no # )
ab#de[fgh]ijk    => "fgh" (all letters outside die because there is a # )
ab#de[fgh]ij#k   => ""  (all letters dies, there are 2 # close to the shellter )
##abde[fgh]ijk   => ""  (all letters dies, there are 2 # close to the shellter )
##abde[fgh]ijk[mn]op => "mn" (letters from the second shelter survive, there is no # close)
#ab#de[fgh]ijk[mn]op => "mn" (letters from the second shelter survive, there is no # close)
#abde[fgh]i#jk[mn]op => "mn" (letters from the second shelter survive, there is only 1 # close)
[a]#[b]#[c]  => "ac"
[a]#b#[c][d] => "d"
[a][b][c]    => "abc"
##a[a]b[c]#  => "c"
"""


import re


def alphabet_war(battlefield: str) -> str:
    """
    Поиск выживших после падения бомбы.
    """
    x = re.split(r'\[(.*?)\]', battlefield)
    a = [x[i].count('#') for i in range(0, len(x), 2)]
    b = [sum(n) for n in zip(a, a[1:])]

    return ''.join([n for i, n in enumerate(x) if not i % 2 and not sum(a) or i % 2 and b[i // 2] < 2])


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('[a]#[b]#[c]', 'ac'),
        ('[a]#b#[c][d]', 'd'),
        ('[a][b][c]', 'abc'),
        ('##a[a]b[c]#', 'c'),
        ('abde[fgh]ijk', 'abdefghijk'),
        ('ab#de[fgh]ijk', 'fgh'),
        ('ab#de[fgh]ij#k', ''),
        ('##abde[fgh]ijk', ''),
        ('##abde[fgh]', ''),
        ('##abcde[fgh]', ''),
        ('abcde[fgh]', 'abcdefgh'),
        ('##abde[fgh]ijk[mn]op', 'mn'),
        ('#abde[fgh]i#jk[mn]op', 'mn'),
        ('[ab]adfd[dd]##[abe]dedf[ijk]d#d[h]#', 'abijk'),
    )
    for key, val in data:
        assert alphabet_war(key) == val


if __name__ == '__main__':
    test()
