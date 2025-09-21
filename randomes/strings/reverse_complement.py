"""
В генетике обратное дополнение последовательности формируется путем обращения
последовательности и последующего взятия дополнения к каждому символу.

Четыре нуклеотида в ДНК — это аденин (А), цитозин (Ц), гуанин (Г) и тимин (Тимин).

    A является дополнением T
    C является дополнением G.

Это двунаправленная связь, поэтому:

    T является дополнением к A
    G является дополнением C.

Для этого ката вам необходимо выполнить функцию обратного дополнения, которая
берет строку ДНК и возвращает строку обратного дополнения.

Примечание : необходимо учитывать регистр букв. Если последовательность
содержит недопустимые символы, необходимо вернуть сообщение
«Недопустимая последовательность».
"""
import typing
import unittest


def reverse_complement(dna: str) -> str:
    """
    Обратное дополнение последовательности ДНК.
    """
    return set(dna) - set('ATCG') and 'Invalid sequence' or dna.translate(str.maketrans('ATCG', 'TAGC'))[::-1]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(reverse_complement, (
        ("TTCCGGAA", "TTCCGGAA"),
        ("GACTGACTGTA","TACAGTCAGTC"),
        ("", ""),
        ("XYZ", "Invalid sequence"),
    ))
