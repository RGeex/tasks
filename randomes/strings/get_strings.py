"""
Вы получаете имя города как строку, и вам нужно вернуть строку, которая показывает, сколько раз каждая буква отображается в строке с помощью звездочек ( *).

Например:

"Chicago"  -->  "c:**,h:*,i:*,a:*,g:*,o:*"

Как видите, буква c показан только один раз, но с 2 звездочками.

Строка возврата должна включать только буквы (не тире, пространства, апострофы и т. Д.). В выводе не должно быть места, а различные буквы разделены запятыми ( ,) как видно в примере выше.

Обратите внимание, что обратная строка должна перечислить буквы в порядке их первого появления в исходной строке.

Больше примеров:

"Bangkok"    -->  "b:*,a:*,n:*,g:*,k:**,o:*"
"Las Vegas"  -->  "l:*,a:**,s:**,v:*,e:*,g:*"
"""
import typing
import unittest


def get_strings(st: str) -> str:
    """
    Форматирует строку по заданному шаблону.
    """
    res = {}
    for w in st.lower().replace(' ', ''):
        res[w] = res.get(w, 0) + 1
    return ','.join([f'{a}:{"*" * b}' for a, b in res.items()])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(get_strings, (
        ("Chicago", "c:**,h:*,i:*,a:*,g:*,o:*"),
        ("Bangkok", "b:*,a:*,n:*,g:*,k:**,o:*"),
        ("Las Vegas", "l:*,a:**,s:**,v:*,e:*,g:*"),
    ))
