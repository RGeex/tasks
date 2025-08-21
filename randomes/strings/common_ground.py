"""
Два генерала-самурая обсуждают планы на ужин после битвы, но, похоже,
не могут прийти к согласию.

Дискуссия накаляется, и вы не можете рисковать, отдавая предпочтение
ни одному из них, поскольку это может нанести ущерб вашему политическому
статусу в любом из двух кланов, к которым принадлежат самураи-генералы.
Остаётся только найти точки соприкосновения в их словах.

Сравните предложения со следующей функцией:

def common_ground(s1,s2)

Параметры s1 и s2Это строки, представляющие слова каждого из генералов.
Вы должны вывести строку, содержащую слова, s1которые также встречаются в s2.

Каждое слово в полученной строке должно встречаться один раз, а порядок
слов должен соответствовать порядку первого появления каждого слова в s2.

Если они не говорят ничего общего, убейте обоих самураев и обвините ниндзя.
(выведите «смерть»).
"""
import typing
import unittest


def common_ground(s1: str, s2: str) -> str:
    """
    Определяет общие слова в 2-х выражениях.
    """
    return ' '.join(sorted(set.intersection(*[set(x.split()) for x in (s1, s2)]), key=s2.split().index)) or 'death'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val)
             for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(
        type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(common_ground, (
        (("eat chicken", "eat chicken and rice"), 'eat chicken'),
        (("eat a burger and drink a coke", "drink a coke"), 'drink a coke'),
        (("i like turtles", "what are you talking about"), 'death'),
        (("aa bb", "aa bb cc"), "aa bb"),
        (("aa bb cc", "bb cc"), 'bb cc'),
        (("aa bb cc", "bb cc bb aa"), 'bb cc aa'),
        (("aa bb", "cc dd"), 'death'),
        (("aa bb", ""), 'death'),
        (("", "cc dd"), 'death'),
        (("", ""), 'death'),
    ))
