"""
Последовательные гласные

Вам дана случайная строка строчных букв. Ваша задача — определить,
сколько гласных букв, расположенных последовательно и последовательно,
содержится в этой строке, начиная с 'a'. Имейте в виду, что последовательная
гласная 'u' является 'a'и цикл продолжается.

Возвращает целое число, равное длине найденных последовательных гласных.

Это лучше объяснить на паре примеров:

    Вам дана строка "agrtertyfikfmroyrntbvsukldkfa"Логика в том, что вы
    начинаете с 'a'И иди прямо. Следующая гласная — 'e'и это последовательная гласная,
    тогда 'i'и так далее, пока не дойдете до 'u'Если вы продолжите двигаться направо,
    вы найдете 'a'который, как оказалось, является последовательной гласной. Возврат 6.
    Это немного более сложный пример: вам дана строка "erfaiekjudhyfimngukduo".
    При движении вправо вы игнорируете все гласные, пока не дойдете до 'a',
    затем игнорируйте остальное, пока не дойдете до 'e', которая является
    последовательной гласной, и так далее, пока не дойдете до 'o'. Возвращаться 4.

Примечание

В этом ката гласные — это 'a', 'e', 'i', 'o', 'u', именно в таком порядке.
'y'в этой ката не считается гласной.
"""
import typing
import unittest


def get_the_vowels_1(word: str) -> int:
    """
    Поиск длины максимальной последовательности гласных баукв.
    """
    tmp, res = 'aeiou', []
    for s in word:
        if s in tmp:
            for i, x in enumerate(res):
                if tmp[tmp.index(s) - 1] == x[-1:]:
                    res[i] += s
            if s == tmp[:1]:
                res.append(s)
    return max(map(len, res), default=0)


def get_the_vowels_2(word: str) -> int:
    """
    Поиск длины максимальной последовательности гласных баукв.
    """
    count = 0
    for w in word:
        count += w == 'aeiou'[count % 5]
    return count


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val)
             for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(
        type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(get_the_vowels_1, (
        ("agrtertyfikfmroyrntbvsukldkfa", 6),
        ("akfheujfkgiaaaofmmfkdfuaiiie", 7),
        ("erfaiekjudhyfimngukduo", 4),
    ))
    test(get_the_vowels_2, (
        ("agrtertyfikfmroyrntbvsukldkfa", 6),
        ("akfheujfkgiaaaofmmfkdfuaiiie", 7),
        ("erfaiekjudhyfimngukduo", 4),
    ))
