"""
Состоящая из команды из пяти невероятно блестящих женщин, «дамы ENIAC»
были первыми «компьютерщиками», работавшими в Школе инженерии Мура
Пенсильванского университета (1945). Благодаря их вкладу мы получили
первое программное приложение и первые классы программирования! Дамы
ENIAC были включены в Зал славы WITI в 1997 году!

Напишите функцию, которая выявит имена «женщин ENIAC», чтобы вы тоже
могли добавить их в свой собственный зал технической славы!

Оставить: только буквенные символы, пробелы и восклицательные знаки.
Чтобы удалить: цифры и эти символы: %$&/£?@

Результат должен быть полностью в верхнем регистре.
"""
import typing
import unittest


def rad_ladies(name: str) -> str:
    """
    Удаляет "мусор" из строки.
    """
    return name.upper().translate(str.maketrans('', '', '1234567890%$&/£?@'))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(rad_ladies, (
        ("k?%35a&&/y@@@£5599 m93753&$$$c$n///79u??@@%l?975$t?%5y%&$3$1!", 'KAY MCNULTY!'),
        ("9?9?9?m335%$£@a791%&$r$$$l£@53$&y&n%$5@ $£5577w&7e931%s$£c$o%%%f351f??%!%%", 'MARLYN WESCOFF!'),
        ("%&$557f953//1/$£@%r%935$$£a@£3111$@???%n???5 $%157b%///$i%55&31£@l?%&$$a%@£$s5757!$$%%%%53", 'FRAN BILAS!'),
        ("///$%&£$553791£r357%??@$%u?$%@7993111£@$%t£$h3% 3$£l$311i3%@?&c3£h%&t&&?%11e%$?@11957r79%£&£m$$a55n1!111%%", 'RUTH LICHTERMAN!'),
        ("??£@%&a5d15??e599713%l%%e%75913 1£$%&@g@£%o&$@13l5d11s$%&t15i9n&5%%@%e@£$!£%$£", 'ADELE GOLDSTINE!'),
    ))
