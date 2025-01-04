"""
Введение

Идет война и никто не знает - война алфавита!
Есть две группы враждебных писем. Напряжение между левыми и правыми буквами было слишком велико, и началась война. В письмах обнаружен новый юнит - жрец с силой Wo lo looooooo.
Задача

Напишите функцию, которая принимает fight строка состоит только из маленьких букв и возвращает, кто выиграет бой. Когда левая сторона побеждает, возвращение Left side wins!, когда правая сторона победит, возвращение Right side wins!, в противном случае возврат Let's fight again!.

Левые буквы и их сила:

 w - 4
 p - 3 
 b - 2
 s - 1
 t - 0 (but it's priest with Wo lo loooooooo power)

Правые буквы и их сила:

 m - 4
 q - 3 
 d - 2
 z - 1
 j - 0 (but it's priest with Wo lo loooooooo power)

Остальные буквы не имеют силы и являются лишь жертвами.
Священники t и j измените соседние буквы с враждебных на дружественные буквы той же силы.

mtq => wtp
wjs => mjz

Письмо с соседними буквами j и t не конвертируется, т.е.:

tmj => tmj
jzt => jzt

Священники ( j и t) не обращайте других священников ( jt => jt ).
Пример

alphabet_war("z")         #=>  "z"  => "Right side wins!"
alphabet_war("tz")        #=>  "ts" => "Left side wins!"
alphabet_war("jz")        #=>  "jz" => "Right side wins!"
alphabet_war("zt")        #=>  "st" => "Left side wins!"
alphabet_war("azt")       #=> "ast" => "Left side wins!"
alphabet_war("tzj")       #=> "tzj" => "Right side wins!"
"""
import typing


def alphabet_war(st: str) -> str:
    """
    Определяет сторону победителя в войне алфавита.
    """
    db, res = {x: (5 <= i, i % 5) for i, x in enumerate('tsbpwjzdqm')}, [0, 0]

    for io in range(len(st)):
        el = [db.get(w, (None, 1)) for w in f' {st} '[io:io + 3]]
        if (key := el[1][0]) is not None:
            if len(t := {a for a, b in el[::2] if not b}) == 1:
                key = [not key, key][t.pop() == key]

            res[key] += el[1][1]

    return [f"{['Left', 'Right'][res[0] < res[1]]} side wins!", "Let's fight again!"][res[0] == res[1]]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""
    import unittest

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(alphabet_war, (
        ("z", "Right side wins!"),
        ("tz", "Left side wins!"),
        ("jbdt", "Let's fight again!"),
        ("jz", "Right side wins!"),
        ("zt", "Left side wins!"),
        ("sj", "Right side wins!"),
        ("azt", "Left side wins!"),
        ("tzj", "Right side wins!"),
        ("wololooooo", "Left side wins!"),
        ("zdqmwpbs", "Let's fight again!"),
        ("ztztztzs", "Left side wins!"),
    ))
