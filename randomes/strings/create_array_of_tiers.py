"""
Создайте функцию, которая принимает число и возвращает массив строк, содержащих число,
обрезанное до каждой цифры.
Примеры

    420должен вернуться ["4", "42", "420"]
    2017должен вернуться ["2", "20", "201", "2017"]
    2010должен вернуться ["2", "20", "201", "2010"]
    4020должен вернуться ["4", "40", "402", "4020"]
    80200должен вернуться ["8", "80", "802", "8020", "80200"]

PS: Входные данные гарантированно будут целым числом в диапазоне [0, 1000000]
"""
import typing
import unittest


def create_array_of_tiers(num: int) -> list[str]:
    """
    Создает из числа список строки до индекса.
    """
    return [str(num)[:i + 1] for i in range(len(str(num)))]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(create_array_of_tiers, (
        (420, ["4", "42", "420"]),
        (2017, ["2", "20", "201", "2017"]),
        (2010, ["2", "20", "201", "2010"]),
        (4020, ["4", "40", "402", "4020"]),
        (80200, ["8", "80", "802", "8020", "80200"]),
    ))
