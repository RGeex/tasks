"""
Введение

Идет война... между алфавитами!
Есть две группы враждебных писем. Напряжение между левыми и правыми буквами было слишком велико,
и началась война. Буквы призывали авиаудар помочь им в войне – тире и точки разбросаны по всему
полю боя. Кто победит?
Задача

Напишите функцию, которая принимает fightстрока, состоящая только из маленьких букв и *который
представляет собой место сброса бомбы. Вернитесь, кто выиграет бой после взрыва бомб.
Когда левая сторона побеждает, возвращение Left side wins!, и когда правая сторона победит,
вернитесь Right side wins!. В остальных случаях возврат Let's fight again!.

Левые буквы и их сила:

 w - 4
 p - 3 
 b - 2
 s - 1

Правые буквы и их сила:

 m - 4
 q - 3 
 d - 2
 z - 1

Остальные буквы не имеют силы и являются лишь жертвами.
The *бомбы убивают соседние буквы (т.е. aa*aa=> a___a, **aa**=> ______ );
Пример

AlphabetWar("s*zz");           //=> Right side wins!
AlphabetWar("*zd*qm*wp*bs*"); //=> Let's fight again!
AlphabetWar("zzzz*s*");       //=> Right side wins!
AlphabetWar("www*www****z");  //=> Left side wins!
"""


import re
from operator import eq, lt


def alphabet_war(fight: str) -> str:
    """
    Определяет кто победит в противостоянии букв.
    """
    k = {k: (v, 0)[::[-1, 1][3 < i]] for i, (k, v) in enumerate(zip('wpbsmqdz', [4, 3, 2, 1]*2))}
    x = list(map(sum, zip(*[k.get(x, (0, 0)) for x in re.sub(r'.?\*+.?', '', fight)])))
    return "Let's fight again!" if not x or eq(*x) else f'{["Right", "Left"][lt(*x)]} side wins!'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("z", "Right side wins!"),
        ("****", "Let's fight again!"),
        ("z*dq*mw*pb*s", "Let's fight again!"),
        ("zdqmwpbs", "Let's fight again!"),
        ("zz*zzs", "Right side wins!"),
        ("sz**z**zs", "Left side wins!"),
        ("z*z*z*zs", "Left side wins!"),
        ("*wwwwww*z*", "Left side wins!"),
        ("w****z", "Let's fight again!"),
        ("mb**qwwp**dm", "Let's fight again!"),
    )
    for key, val in data:
        assert alphabet_war(key) == val


if __name__ == '__main__':
    test()
