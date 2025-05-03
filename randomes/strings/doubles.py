"""
В этом Ката вы напишете функцию doublesкоторый удалит двухстрочные символы, расположенные рядом друг с другом.

Например:

doubles('abbcccdddda') = 'aca', потому что слева направо:

a) There is only one 'a' on the left hand side, so it stays.
b) The 2 b's disappear because we are removing double characters that are adjacent. 
c) Of the 3 c's, we remove two. We are only removing doubles. 
d) The 4 d's all disappear, because we first remove the first double, and again we remove the second double.
e) There is only one 'a' at the end, so it stays.

Еще два примера: doubles('abbbzz') = 'ab' и doubles('abba') = "". Во втором примере,
когда мы удаляем b в 'abba', двойной aэтот результат затем удаляется.

Строки будут содержать только строчные буквы. Больше примеров в тестовых случаях.

Удачи!

"""
import typing
import unittest
from itertools import groupby


def doubles(st: str) -> str:
    """
    Удаляет из строки парные символы стоящие рядом.
    """
    return x if len(x := ''.join([['', a][len(list(b)) % 2] for a, b in groupby(st)])) == len(st) else doubles(x)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(doubles, (
        ('abbbzz', 'ab'),
        ('zzzzykkkd', 'ykd'),
        ('abbcccdddda', 'aca'),
        ('vvvvvoiiiiin', 'voin'),
        ('rrrmooomqqqqj', 'rmomj'),
        ('xxbnnnnnyaaaaam', 'bnyam'),
        ('qqqqqqnpppgooooonpppppqmmmmmc', 'npgonpqmc'),
        ('qqqqqwwwx', 'qwx'),
        ('jjjfzzzzzzsddgrrrrru', 'jfsgru'),
        ('jjjjjfuuuutgggggqppdaaas', 'jftgqdas'),
        ('iiiiibllllllyqqqqqbiiiiiituuf', 'ibyqbtf'),
        ('mmmmmmuzzqllllmqqqp', 'uqmqp'),
        ('aaaaapwwwwptttmhhhhtpppnaaaaabhhlnnnxddpiiiif', 'atmtpnablnxpf'),
    ))
