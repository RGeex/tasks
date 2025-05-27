"""
Введение

Идет война, и никто об этом не знает — война алфавитов!
Есть две группы враждебных букв. Напряжение между буквами левой и правой стороны было слишком 
велико, и началась война.
Задача

Напишите функцию, которая принимает fightСтрока состоит только из маленьких букв и вернитесь,
кто победит в бою. Когда левая сторона победит, вернитесь Left side wins!, когда правая сторона
побеждает, возвращается Right side wins!, в противном случае возврат Let's fight again!.

Буквы левой стороны и их сила:

 w - 4
 p - 3
 b - 2
 s - 1

Буквы правой стороны и их сила:

 m - 4
 q - 3
 d - 2
 z - 1

Другие буквы не имеют силы и являются лишь жертвами. Суммируйте значения силы букв каждой стороны,
чтобы определить, какая сторона побеждает.
Пример

AlphabetWar("z");        //=> Right side wins!
AlphabetWar("zdqmwpbs"); //=> Let's fight again!
AlphabetWar("zzzzs");    //=> Right side wins!
AlphabetWar("wwwwwwz");  //=> Left side wins!
"""
import typing
import unittest


def alphabet_war(st: str) -> str:
    """
    Алфавитные войны, определяет сторону победителя.
    """
    weight = {x: abs(i) for i, x in enumerate('wpbs zdqm', -4) if i}
    a, b = map(sum, zip(*[[weight[x], 0][::x in 'wpbs' or -1] for x in st if x in weight]))
    return "Let's fight again!" if a == b else f"{['Left', 'Right'][a < b]} side wins!"


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(alphabet_war, (
        ("z", "Right side wins!"),
        ("zdqmwpbs", "Let's fight again!"),
        ("wq", "Left side wins!"),
        ("zzzzs", "Right side wins!"),
        ("wwwwww", "Left side wins!"),
    ))
