"""
О нет! Кто-то оставил сервер в вашем местном автосалоне слишком близко к блендеру, и теперь все данные зашифрованы.

Ваша задача — расшифровать данные и поместить их в удобный для чтения словарь.

Расшифруйте предоставленный вам список и верните значения в словарь, например, такой:

dictionary = {'make': make, 'model': model, 'year': year, 'new': new}

Вам будет предоставлен список, содержащий строку (марка автомобиля), кортеж, содержащий две строки (модель и подмодель),
целое число (год выпуска автомобиля) и логическое значение (является ли автомобиль новым или подержанным — «True» или «False»),
но вы не будете знать порядок в списке.

Верните словарь, где «make» — строка, «model» — строка, «year» — целое число, а «new» — логическое значение, указывающее,
является ли объект новым (True) или бывшим в употреблении (False).

PS Модель необходимо преобразовать в строку, разделяя значения одним пробелом.

"""
import typing
import unittest


def make_model_year(lst: list[typing.Any]) -> dict:
    """
    Упорядочивает элементы списка в словарь.
    """
    return dict(zip('make model year new'.split(), [' '.join(x) if isinstance(x, tuple) else x for x in sorted(lst, key=lambda x: (isinstance(x, bool), isinstance(x, int), isinstance(x, tuple)))]))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(make_model_year, (
        ([1998, 'ford', ('mustang', 'gt'), False], {'make': 'ford', 'model': 'mustang gt', 'year': 1998, 'new': False}),
        (['benz', ('motorwagen', 'basic'), False, 1886], {'make': 'benz', 'model': 'motorwagen basic', 'year': 1886, 'new': False}),
        ([('camry', 'basic'), True, 2020, 'toyo'], {'make': 'toyo', 'model': 'camry basic', 'year': 2020, 'new': True}),
    ))
