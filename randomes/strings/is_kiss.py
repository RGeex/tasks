"""
Аббревиатура KISS расшифровывается как Keep It Simple Stupid (Держись простоты, глупец).
Это принцип проектирования, направленный на упрощение, а не усложнение.

Вы — начальник Джо.

Джо присылает вам текст для публикации в блоге. Он любит всё усложнять.

Определите функцию, которая определяет, является ли работа Джо простой или сложной.

Входными данными будут непустые строки без знаков препинания.

Это просто, если: Длина каждого слова не превышает количество слов в строке.

В противном случае это сложно.

Если это сложный случай:

return "Keep It Simple Stupid"

или если бы все было просто:

return "Good work Joe!"

Примечание: Случайные тесты случайны и бессмысленны. Вот нелепый пример случайного теста:

"jump always mostly is touchy dancing choice is pineapples mostly"

"""
import unittest
from typing import Any, Callable, Tuple


def is_kiss(words: str) -> str:
    """
    Определяет, является ли работа Джо простой или сложной.
    """
    return next(("Keep It Simple Stupid" for w in words.split() if len(w) > len(words.split())), "Good work Joe!")


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(is_kiss, (
        ('Joe had a bad day', "Good work Joe!"),
        ('Joe had some bad days', "Good work Joe!"),
        ('Joe is having no fun', "Keep It Simple Stupid"),
        ('Sometimes joe cries for hours', "Keep It Simple Stupid"),
        ('Joe is having lots of fun', "Good work Joe!"),
        ('Joe is working hard a lot', "Keep It Simple Stupid"),
        ('Joe listened to the noise and it was an onamonapia', "Good work Joe!"),
        ('Joe listened to the noises and there were some onamonapias', "Keep It Simple Stupid"),
    ))
