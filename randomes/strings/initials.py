"""
Полное имя человека обычно состоит из имени, отчества и фамилии; однако в некоторых культурах
(например, в Южной Индии) может быть более одного отчества.

Напишите функцию, которая принимает полное имя человека и возвращает инициалы, разделенные точками
( '.'). Инициалы должны быть заглавными. Фамилия человека должна быть указана полностью,
причем ее первая буква также должна быть заглавной.

Смотрите образец ниже:

"code wars"            ---> "C.Wars"
"Barack hussein obama" ---> "B.H.Obama"

Имена в полном имени разделяются ровно одним пробелом ( ' ') ; без начальных и конечных пробелов.
Имена всегда будут написаны строчными буквами, за исключением, по желанию, первой буквы.
"""
import typing
import unittest


def initials(st: str) -> str:
    """
    Создание сокращения из имени человека.
    """
    return '.'.join([x.capitalize()[:bool(i) or None] for i, x in enumerate(st.split()[::-1])][::-1])
    

def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(initials, (
        ('code wars', 'C.Wars'),
        ('Barack hussein obama', 'B.H.Obama'),
        ('barack hussein Obama', 'B.H.Obama'),
    ))
