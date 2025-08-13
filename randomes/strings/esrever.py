"""
В этом ката вам необходимо взять входную строку, поменять местами
слова и буквы в словах.

Но, в качестве бонуса, каждый тестовый ввод будет заканчиваться знаком
препинания (! ? .), а вывод должен быть возвращен со знаком препинания
в конце.

Несколько примеров помогут прояснить ситуацию:

esrever("hello world.") == "dlrow olleh."

esrever("Much l33t?") == "t33l hcuM?"

esrever("tacocat!") == "tacocat!"

Краткое замечание: строка всегда будет передана (хотя она может быть пустой),
поэтому нет необходимости в проверке ошибок других типов.

"""
import typing
import unittest


def esrever(st: str) -> str:
    """
    Разворачивает слова в предлжении а так же порядк слов.
    """
    return st[:-1][::-1] + st[-1:]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':

    test(esrever, (
        ('an Easy one?', 'eno ysaE na?'),
        ('a small lOan OF 1,000,000 $!', '$ 000,000,1 FO naOl llams a!'),
        ('<?> &!.".', '".!& >?<.'),
        ('b3tTer p4ss thIS 0ne.', 'en0 SIht ss4p reTt3b.'),
        ('', ''),
    ))
