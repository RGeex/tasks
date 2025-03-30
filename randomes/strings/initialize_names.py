"""
У некоторых людей есть только имя, у некоторых — имя и фамилия,
а у некоторых — имя, отчество и фамилия.

Ваша задача — инициализировать отчества (если таковые имеются).
Примеры

'Jack Ryan'                   => 'Jack Ryan'
'Lois Mary Lane'              => 'Lois M. Lane'
'Dimitri'                     => 'Dimitri'
'Alice Betty Catherine Davis' => 'Alice B. C. Davis'


"""
import typing
import unittest


def initialize_names(st: str) -> str:
    """
    Сокращает отчества, если они есть.
    """
    return ' '.join(x if i in (0, len(st.split()) - 1) else f'{x[0]}.' for i, x in enumerate(st.split()))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(initialize_names, (
        ('Jack Ryan', 'Jack Ryan'),
        ('Lois Mary Lane', 'Lois M. Lane'),
        ('Dimitri', 'Dimitri'),
        ('Alice Betty Catherine Davis', 'Alice B. C. Davis'),
    ))
