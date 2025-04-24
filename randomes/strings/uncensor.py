"""
Мой ПК заразился странным вирусом. Он заражает только мои текстовые файлы
и заменяет случайные буквы на *, li*e th*s (like this).

К счастью, я обнаружил, что вирус прячет мои отцензурированные письма в корневом каталоге.

Будет очень утомительно восстанавливать все эти файлы вручную, поэтому ваша цель —
реализовать uncensorфункция, которая автоматически выполняет всю сложную работу.
Примеры

uncensor("*h*s *s v*ry *tr*ng*", "Tiiesae") ➜ "This is very strange"

uncensor("A**Z*N*", "MAIG") ➜ "AMAZING"

uncensor("xyz", "") ➜ "xyz"

Примечания

    Ожидайте, что все обнаруженные буквы будут даны в правильном порядке.
    Количество обнаруженных букв будет соответствовать количеству отцензурированных.
    Любой персонаж может быть подвергнут цензуре.
"""
import typing
import unittest


def uncensor(infected: str, discovered: str) -> str:
    """
    Возвращает текст в изначальное состояние.
    """
    ds = list(discovered)
    return ''.join(ds.pop(0) if x == '*' and ds else x for x in infected)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(uncensor, (
        (('*h*s *s v*ry *tr*ng*', 'Tiiesae'), 'This is very strange'),
        (('A**Z*N*', 'MAIG'), 'AMAZING'),
        (('xyz', ''), 'xyz'),
        (('', ''), ''),
        (('***', 'abc'), 'abc')
    ))
