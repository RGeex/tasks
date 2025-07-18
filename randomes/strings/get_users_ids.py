"""
Привет, CodeWarrior,

Сегодня нам предстоит много кодить!

Надеюсь, вы знакомы с основными приемами работы с тетивами, потому что это ката
будет посвящено именно им.

Вот так...
Фон

У нас есть очень длинная строка, содержащая множество идентификаторов пользователей.
Эта строка представляет собой список, в котором каждый идентификатор пользователя
разделён запятой и пробелом ("'"). Иногда пробелов больше одного. Имейте это в виду!
Более того, некоторые идентификаторы пользователей пишутся только строчными буквами,
другие — вперемешку строчными и заглавными. Каждый идентификатор пользователя
начинается с одного и того же трёхбуквенного «uid», например, «uid345edj».
Но это ещё не всё! Какой-то глупый студент отредактировал строку и добавил
несколько хэштегов (#). Идентификаторы пользователей, содержащие хэштеги,
недействительны, поэтому эти хэштеги следует удалить!
Задача

    Удалить все хэштеги
    Удалить начальный «uid» из каждого идентификатора пользователя.
    Вернуть массив строк -> разбить строку
    Каждый идентификатор пользователя должен быть написан только строчными буквами.
    Удалить начальные и конечные пробелы

"""
import re
import typing
import unittest


def get_users_ids(st: str) -> list[str]:
    """
    Поиск в строке по заданному шаблону.
    """
    return [re.sub(r'.?uid *', '', x.strip(), 1) for x in st.lower().replace('#', '').split(', ')]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(get_users_ids, (
        ("uid12345", ["12345"]),
        ("   uidabc  ", ["abc"]),
        ("#uidswagger", ["swagger"]),
        ("uidone, uidtwo", ["one", "two"]),
        ("uidCAPSLOCK", ["capslock"]),
        ("uid##doublehashtag", ["doublehashtag"]),
        ("  uidin name whitespace", ["in name whitespace"]),
        ("uidMultipleuid", ["multipleuid"]),
        ("uid12 ab, uid#, uidMiXeDcHaRs", ["12 ab", "", "mixedchars"]),
        (" uidT#e#S#t# ", ["test"]),
    ))
