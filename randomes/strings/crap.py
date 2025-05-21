"""
Вы наткнулись на божественное удовольствие, которое заключается в владении собакой и садом.
Теперь время собрать весь х@рь! :D

Вам дан двумерный массив, представляющий ваш сад, и вы должны найти и собрать все собачьи предметы,
представленные '@'.

Вам также будет сообщено количество сумок, к которым у вас есть доступ ( bags), и вместимость сумки
( cap). Если нет bags тогда вы ничего не сможете подобрать, поэтому можете игнорировать cap.

Вам нужно выяснить, достаточно ли у вас возможностей собрать весь мусор и снова сделать свой
сад чистым.

Если вы это сделаете, верните 'Clean', иначе возврат 'Cr@p'.

Но будьте осторожны - если ваша собака где-то там ( 'D'), он становится очень чувствительным,
когда за ним наблюдают. Если он там, вам нужно вернуться 'Dog!!'.

Например:

bags = 2
cap = 2
x (or garden) =
[[ _ , _ , _ , _ , _ , _ ],
 [ _ , _ , _ , _ , @ , _ ],
 [ @ , _ , _ , _ , _ , _ ]]

возвращается 'Clean'

"""
import typing
import unittest


def crap(garden: list[list[str]], bags: int, cap: int) -> str:
    """
    Отчищает сад, если это возможно.
    """
    garden, slots = ''.join(a for b in garden for a in b), bags * cap
    return 'Dog!!' if 'D' in garden else ['Cr@p', 'Clean'][garden.count('@') <= slots]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(crap, (
        (([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 2, 2), "Clean"),
        (([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 1, 1), "Cr@p"),
        (([['_','_'], ['_','@'], ['D','_']], 2, 2), "Dog!!"),
        (([['_','_','_','_'], ['_','_','_','_'], ['_','_','_', '_']], 2, 2), "Clean"),
        (([['@','@'], ['@','@'], ['@','@']], 3, 2), "Clean"),
    ))
