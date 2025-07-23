"""
Я дам вам две строки. Я хочу, чтобы вы преобразовали stringOne в stringTwo по одной букве за раз.

Пример:

stringOne = 'bubble gum';
stringTwo = 'turtle ham';

Result:
bubble gum
tubble gum
turble gum
turtle gum
turtle hum
turtle ham
"""
import typing
import unittest


def mutate_my_strings(s1: str, s2: str) -> str:
    """
    Последовательная замена строки 1 строкой 2.
    """
    return '\n'.join({s2[:i] + s1[i:]: 0 for i in range(len(s1) + 1)}) + '\n'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(mutate_my_strings, (
        (("bubble gum", "turtle ham") , "bubble gum\ntubble gum\nturble gum\nturtle gum\nturtle hum\nturtle ham\n"),
        (("car door", "car bore") , "car door\ncar boor\ncar borr\ncar bore\n"),
        (("open source", "lean course") , "open source\nlpen source\nleen source\nlean source\nlean cource\nlean course\n"),
        (("right wrong", "wrong right") , "right wrong\nwight wrong\nwrght wrong\nwroht wrong\nwront wrong\nwrong wrong\nwrong rrong\nwrong riong\nwrong rigng\nwrong righg\nwrong right\n"),
        (("pythons best", "jscript bttr") , "pythons best\njythons best\njsthons best\njschons best\njscrons best\njscrins best\njscrips best\njscript best\njscript btst\njscript bttt\njscript bttr\n"),
        (("acvqwrtqwcasd", "lvqewnhuiypaf") , "acvqwrtqwcasd\nlcvqwrtqwcasd\nlvvqwrtqwcasd\nlvqqwrtqwcasd\nlvqewrtqwcasd\nlvqewntqwcasd\nlvqewnhqwcasd\nlvqewnhuwcasd\nlvqewnhuicasd\nlvqewnhuiyasd\nlvqewnhuiypsd\nlvqewnhuiypad\nlvqewnhuiypaf\n"),
        (("bubble gum crisis", "turtle ham creamy") ,"bubble gum crisis\ntubble gum crisis\nturble gum crisis\nturtle gum crisis\nturtle hum crisis\nturtle ham crisis\nturtle ham cresis\nturtle ham creais\nturtle ham creams\nturtle ham creamy\n"),
        (("bubble gum crisis tokyo 2040", "turtle ham creamy apple pies") , "bubble gum crisis tokyo 2040\ntubble gum crisis tokyo 2040\nturble gum crisis tokyo 2040\nturtle gum crisis tokyo 2040\nturtle hum crisis tokyo 2040\nturtle ham crisis tokyo 2040\nturtle ham cresis tokyo 2040\nturtle ham creais tokyo 2040\nturtle ham creams tokyo 2040\nturtle ham creamy tokyo 2040\nturtle ham creamy aokyo 2040\nturtle ham creamy apkyo 2040\nturtle ham creamy appyo 2040\nturtle ham creamy applo 2040\nturtle ham creamy apple 2040\nturtle ham creamy apple p040\nturtle ham creamy apple pi40\nturtle ham creamy apple pie0\nturtle ham creamy apple pies\n"),
        (("bubble gum", "bubble gum") , "bubble gum\n"),
        (("", "") , "\n"),
    ))
