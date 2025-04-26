"""
Наличие двух стандартов раскладки клавиатуры неудобно!
Раскладка клавиатуры компьютера:
7 8 9 \н 4 5 6 \н 1 2 3 \н 0 \н

Раскладка клавиатуры сотового телефона:
1 2 3\н 4 5 6\н 7 8 9\н 0\н

Решите проблему нестандартных клавиатур, предоставив функцию, которая преобразует вводимые
с компьютера данные в числа, как если бы они были набраны на телефоне.

Пример:
"789" -> "123"

Примечания:
Вы получаете строку, содержащую только цифры.

"""
import typing
import unittest


def computer_to_phone(numbers: str) -> str:
    """
    Преобразует набор цифр на компьютере как на на телефоне.
    """
    return numbers.translate(str.maketrans('123789', '789123'))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(computer_to_phone, (
        ("0789456123", "0123456789"),
        ("000", "000"),
        ("94561", "34567"),
    ))
