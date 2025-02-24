"""
back·ro·nym

    Аббревиатура, намеренно сформированная из фразы, чьи начальные буквы изложены конкретное слово или слова, либо для создания запоминающегося имени, либо как причудливое объяснение происхождения слова.

    «Биоразнообразие, служащее нашей нации», или бизон

(от https://en.oxforddictionary.com/definition/backronym )

Заполните функцию, чтобы создать Backronyms. Преобразовать заданную строку (без пробелов) в Backronym, используя предварительно загруженный словарь и верните цепочку слов, разделенную одним пространством (но без пробелов).

Ключи предварительно загруженного словаря - это прописные буквы A-Z и значения являются предопределенными словами, например:

dictionary["P"] == "perfect"

Примеры

"dgm" ==> "disturbing gregarious mustache"

"lkj" ==> "literal klingon joke"
"""
import typing
import unittest


arr = {
    'A': 'awesome',
    'B': 'beautiful',
    'C': 'confident',
    'D': 'disturbing',
    'E': 'eager',
    'F': 'fantastic',
    'G': 'gregarious',
    'H': 'hippy',
    'I': 'ingestable',
    'J': 'joke',
    'K': 'klingon',
    'L': 'literal',
    'M': 'mustache',
    'N': 'newtonian',
    'O': 'oscillating',
    'P': 'perfect',
    'Q': 'queen',
    'R': 'rant',
    'S': 'stylish',
    'T': 'turn',
    'U': 'underlying',
    'V': 'volcano',
    'W': 'weird',
    'X': 'xylophone',
    'Y': 'yogic',
    'Z': 'zero'
}


def make_backronym(st: str) -> str:
    """
    Расшифровывает аббревиатуры по словарю.
    """
    return ' '.join(map(arr.get, st.upper()))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(make_backronym, (
        ('adh','awesome disturbing hippy'),
        ('lmnop','literal mustache newtonian oscillating perfect'),
        ('wyv','weird yogic volcano'),
        ('interesting','ingestable newtonian turn eager rant eager stylish turn ingestable newtonian gregarious'),
        ('codewars','confident oscillating disturbing eager weird awesome rant stylish'),
        ('privet','perfect rant ingestable volcano eager turn'),
        ('paka','perfect awesome klingon awesome'),
        ('',''),
        ('ppp','perfect perfect perfect'),
    ))
