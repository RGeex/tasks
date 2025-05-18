"""
Сузуки нужна помощь в подборе учеников!

Сегодня Судзуки будет проводить собеседования со своими учениками, чтобы убедиться,
что они продвигаются в обучении. Он решил запланировать собеседования на основе длины
имени ученика в порядке убывания. Ученики выстроятся в очередь и будут ждать своей очереди.

Вам будет предоставлена ​​строка имен студентов. Отсортируйте их и верните список имен
в порядке убывания.

Вот пример ввода:

string = 'Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi'

Вот пример возврата из вашей функции:

 lst = ['Takehiko',
        'Takayuki',
        'Takahiro',
        'Takeshi',
        'Takeshi',
        'Takashi',
        'Tadashi',
        'Takeo',
        'Takao']

Имена одинаковой длины будут возвращены в обратном алфавитном порядке (Я->А) таким образом:

string = "xxa xxb xxc xxd xa xb xc xd"

Возвраты

['xxd', 'xxc', 'xxb', 'xxa', 'xd', 'xc', 'xb', 'xa']

"""
import typing
import unittest


def lineup_students(st: str) -> list[str]:
    """
    Сортирует слова в строке по длине с конца, и по алфамиту с конца.
    """
    return sorted(st.split(), key=lambda x: (-len(x), [-ord(n) for n in x]))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(lineup_students, (
        (
            'Tadashi Takahiro Takao Takashi Takayuki Takehiko Takeo Takeshi Takeshi',
            ['Takehiko', 'Takayuki', 'Takahiro', 'Takeshi', 'Takeshi', 'Takashi', 'Tadashi', 'Takeo', 'Takao'],
        ),
    ))
