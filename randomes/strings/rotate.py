"""
Ваша семья владеет магазином и только что привезла с собой текстовую машину с
прокруткой, чтобы получить немного больше бизнеса.

Скроллер работает путем замены текущей текстовой строки на аналогичную
текстовую строку, но со смещенной в конец первой буквой; это имитирует
движение.

Твой отец слишком занят делами, чтобы беспокоиться о таких деталях, поэтому,
естественно, он заставляет тебя придумывать текстовые строки.

Создайте функцию с именем Rotate(), которая принимает строковый аргумент и
возвращает массив строк, в котором каждая буква входной строки поворачивается
до конца.

rotate("Hello") // => ["elloH", "lloHe", "loHel", "oHell", "Hello"]

Примечание: Исходная строка должна быть включена в выходной массив. Порядок
имеет значение. Каждый элемент выходного массива должен быть повернутой версией
предыдущего элемента. Выходной массив ДОЛЖЕН иметь ту же длину,
что и входная строка. Функция должна возвращать пустой массив со строкой
нулевой длины '' в качестве входных данных.
"""
import typing
import unittest


def rotate(s: str) -> list[str]:
    """
    Создает все возможные смещения символов заданной строки вперед.
    """
    return [s[i:] + s[:i] for i in range(1, len(s) + 1)]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(rotate, (
        ("", []),
        (" ", [" "]),
        ("123", ["231", "312", "123"]),
        ("Hello", ["elloH", "lloHe", "loHel", "oHell", "Hello"]),
    ))
