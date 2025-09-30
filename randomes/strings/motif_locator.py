"""
В генетике мотив последовательности — это структура последовательности нуклеотидов (или аминокислот).
Мотивы последовательности имеют биологическое значение. Подробнее см. здесь .

Для этого ката вам необходимо выполнить функцию motif_locatorЭта функция принимает два аргумента:
последовательность и мотив. Оба аргумента — строки.

Необходимо вернуть массив, содержащий все начальные позиции мотива (по порядку). Последовательность
может содержать 0 или более повторений заданного мотива. Обратите внимание, что номер
первой позиции — 1, а не 0.

Вот несколько примеров:

    Для sequence"ACGTGGGGACTAGGGG" и motif"GGGG" результат должен быть [5, 13].
    Для sequence"ACCGTACCAAGGGACC" и motif"AAT" результат должен быть []
    Для sequence"GGG" и мотив "GG" результат должен быть [1, 2]
"""
import typing
import unittest
import re


def motif_locator(sequence: str, motif: str) -> list[int]:
    """
    Поиск всех начальных позиций мотива.
    """
    return [m.start() + 1 for m in re.finditer(f'(?={re.escape(motif)})', sequence)]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(motif_locator, (
        (("TTCCGGAACC", "CC"), [3, 9]),
        (("ACGTTACAACGTTAG", "ACGT"),  [1, 9]),
        (("ACGTACGTACGT", "AAA"), []),
        (("ACGT","ACGTGAC"), []),
    ))
