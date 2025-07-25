"""
26 букв английского алфавита случайным образом делятся на 5 групп по 5 букв,
при этом оставшаяся буква игнорируется. Каждой группе присваивается оценка
больше 0. Игнорируемая буква всегда получает оценку 0.

Используя этот ката, напишите функцию для вычисления оценки имени, которая
передается в функцию.

Вывод должен быть возвращен как объект:

{'Mary Jane':20}

Только буквы имеют значение. Пробелы — нет.

Вы можете с уверенностью предположить, что nameне содержит знаков препинания и
символов. Также не будет empty string или null ценить.

Статичный alphaДля вашего удобства объект для тестирования был предварительно
загружен в следующем формате:

{'ABCDE':1, 'FGHIJ':2, 'KLMNO':3, 'PQRST':4, 'UVWXY':5}

'Z' is ignored

Пример

В соответствии с вышеизложенным alphaобъект, имя Mary Janeбудет иметь оценку
имени 20=> М=3 + а=1 + г=4 + у=5 + Ж=2 + а=1 + н=3 + е=1
"""
import typing
import unittest
from string import ascii_lowercase as abc


def name_score(name: str) -> dict[str, int]:
    """
    Расчитывает стоимость имени.
    """
    return {name:sum({st in abc[i * 5:i * 5 + 5]:i + 1 for i in range(len(abc) // 5)}.get(1, 0) for st in name.lower())}


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(name_score, (
        ('Mary Jane', {"Mary Jane":20}),
        ('Luke Skywalker', {"Luke Skywalker":41}),
        ('Zoe Andrews', {"Zoe Andrews":23}),
        ('Double  Space', {"Double  Space":25}),
        ('Greg Z MacDonald', {"Greg Z MacDonald":26}),
    ))
