"""
Если вы закончите это ката, вы можете попробовать «Безумные цветные треугольники» от Bubbler,
которое является гораздо более сложной версией этого.

Цветной треугольник создается из ряда цветов, каждый из которых красный, зеленый или синий.
Последовательные ряды, каждый из которых содержит на один цвет меньше, чем предыдущий, генерируются
путем рассмотрения двух соприкасающихся цветов в предыдущем ряду. Если эти цвета идентичны, тот же
цвет используется в новом ряду. Если они различны, отсутствующий цвет используется в новом ряду.
Это продолжается до тех пор, пока не будет сгенерирован последний ряд, содержащий только один цвет.

Возможны следующие варианты:

Colour here:        G G        B G        R G        B R
Becomes colour:      G          R          B          G

Более крупный пример:

R R G B R G B B
 R B R G B R B
  G G B R G G
   G R G B G
    B B R R
     B G R
      R B
       G

Вам будет предоставлена ​​первая строка треугольника в виде строки, и ваша задача — вернуть
окончательный цвет, который появится в нижней строке в виде строки. В случае примера выше,
вы бы дали RRGBRGBBты должен вернуться G.

    Входная строка будет содержать только заглавные буквы. R, G, Bи будет как минимум одна буква,
    поэтому вам не придется проверять ввод на недопустимость.
    Если на входе указан только один цвет, верните этот цвет.
"""
import typing
import unittest


def triangle(st: str) -> str:
    """
    Определяет последний цвет.
    """
    while 1 < len(st):
        st = ''.join([(set('RGB') - set(st[i:i+2])).pop() if 1 < len(set(st[i:i+2])) else st[i] for i in range(len(st) - 1)])
    return st


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(triangle, (
        ('GB', 'R'),
        ('RRR', 'R'),
        ('RGBG', 'B'),
        ('RBRGBRB', 'G'),
        ('RBRGBRBGGRRRBGBBBGG', 'G'),
        ('B', 'B'),
    ))
