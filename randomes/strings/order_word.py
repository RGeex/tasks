"""
Описание:

Для данной строки вам необходимо написать метод, который упорядочит все буквы в этой строке в
порядке возрастания.

Также следует проверить, что данная строка не является пустой или нулевой. Если это так, метод
должен вернуть:

"Invalid String!"

Примечания
• данная строка может быть как строчной, так и заглавной.
• строка может включать пробелы или другие специальные символы, такие как '# ! или ,'.
Сортируйте их на основе их кодов ASCII
Примеры

"hello world" => " dehllloorw"
"bobby"       => "bbboy"
""            => "Invalid String!"
"!Hi You!"    => " !!HYiou"

"""
import typing
import unittest


def order_word(st: str | None) -> str:
    """
    Сортирует символы в строке по ASCI
    """
    return st and ''.join(sorted(st)) or 'Invalid String!'


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(order_word, (
        ("Hello, World!", " !,HWdellloor"),
        ("bobby", "bbboy"),
        ("", "Invalid String!"),
        ("completesolution", "ceeillmnooopsttu"),
        ("\"][@!#$*(^&%", "!\"#$%&(*@[]^"),
        ("i\"d][@z!#$r(^a&world%", "!\"#$%&(@[]^addilorrwz"),
        (None, "Invalid String!"),
    ))
