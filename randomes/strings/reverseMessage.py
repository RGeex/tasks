"""
Переверните сообщение так, чтобы слова и буквы, переданные в него,
были переведены в нижний регистр и перевернуты. Кроме того,
сделайте заглавной первую букву перевернутых слов.
Если в первой позиции слова теперь находится цифра или символ (!#,>),
то заглавная буква не требуется.

Пример:

reverseMessage('This is an example of a Reversed Message!')
Returns: '!egassem Desrever A Fo Elpmaxe Na Si Siht'


"""
import unittest
from typing import Any, Callable, Tuple


def reverseMessage(text: str) -> str:
    """
    Переворачивает сообщение.
    """
    return ' '.join(x[0].upper() + x[1:] for x in text[::-1].lower().split())


def reverseMessage_2(text: str) -> str:
    """
    Переворачивает сообщение.
    """
    return ' '.join(map(str.capitalize, text[::-1].split()))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(reverseMessage, (
        ('AaaaA', 'Aaaaa'),
        ('Hello there', 'Ereht Olleh'),
        ('Pl34k78j', 'J87k43lp'),
        ('Reverse this message!', '!egassem Siht Esrever'),
        ('Today is the 14th of January!', '!yraunaj Fo Ht41 Eht Si Yadot'),
        ('hty56hA T76#Td', 'Dt#67t Ah65yth'),
        ('', ''),
    ))
    test(reverseMessage_2, (
        ('AaaaA', 'Aaaaa'),
        ('Hello there', 'Ereht Olleh'),
        ('Pl34k78j', 'J87k43lp'),
        ('Reverse this message!', '!egassem Siht Esrever'),
        ('Today is the 14th of January!', '!yraunaj Fo Ht41 Eht Si Yadot'),
        ('hty56hA T76#Td', 'Dt#67t Ah65yth'),
        ('', ''),
    ))
