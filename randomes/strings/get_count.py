"""
Обработка ошибок очень важна в кодировании, но, похоже,
ее игнорируют или не реализуют должным образом.

#Задача

Ваша задача — реализовать функцию, которая принимает строку в качестве
входных данных и возвращает объект, содержащий свойства гласные и согласные.
Свойство vowels должно содержать общее количество гласных {a,e,i,o,u} и общее
количество согласных {a,..,z} - {a,e,i,o,u}. Обрабатывайте недопустимые входные
данные и не забывайте возвращать допустимые.

#Вход

Входные данные — любая случайная строка. Затем вы должны различить, что является гласными,
а что — согласными, и просуммировать для каждой категории их общее количество вхождений в
объект. Однако вы также можете получить входные данные, которые не являются строками.
Если это произойдет, то вы должны вернуть объект с общим количеством гласных и
согласных 0, поскольку входные данные НЕ были строкой. Обратитесь к разделу «Пример»
для более наглядного представления того, какие входные данные вы можете получить и
какие выходные данные ожидаются. :)
Пример:

Input: get_count('test')
Output: {vowels:1,consonants:3}

Input: get_count('tEst')
Output: {vowels:1,consonants:3}

Input get_count('    ')
Output: {vowels:0,consonants:0}

Input get_count()
Output: {vowels:0,consonants:0}


"""
import typing
import unittest


def get_count(st: str='') -> dict[str:int]:
    """
    Подсчитывает кол-во гласных и согласных в строке.
    """
    x = [[1, 0][::x in 'aeiou' or -1] for x in isinstance(st, str) and st.lower() or '' if x.isalpha()]
    return dict(zip(('vowels', 'consonants'), list(map(sum, zip(*x))) or (0, 0)))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(get_count, (
        ('Test', {"vowels": 1, "consonants": 3}),
        ('Here is some text', {"vowels": 6, "consonants": 8}),
        ('To be a Codewarrior or not to be', {"vowels": 12, "consonants": 13}),
        ('To Kata or not to Kata', {"vowels": 8, "consonants": 9}),
        ('aeiou', {"vowels": 5, "consonants": 0}),
        ('TEst', {"vowels": 1, "consonants": 3}),
        ('HEre Is sOme text', {"vowels": 6, "consonants": 8}),
        (['To Kata or not to Kata'], {"vowels": 0, "consonants": 0}),
        (None, {"vowels": 0, "consonants": 0}),
        ('Test               ', {"vowels": 1, "consonants": 3}),
        ('Here is some text  ', {"vowels": 6, "consonants": 8}),
        ('To be a Codewarrior or not to be', {"vowels": 12, "consonants": 13}),
        ('                         ', {"vowels": 0, "consonants": 0}),
        ({'jjjjj': 'jjjjj'}, {"vowels": 0, "consonants": 0}),
        ('TEst', {"vowels": 1, "consonants": 3}),
        ('HEre Is sOme text', {"vowels": 6, "consonants": 8}),
    ))
