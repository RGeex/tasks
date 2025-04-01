"""
Вам будет предоставлен массив объектов, представляющих данные о разработчиках, которые
зарегистрировались для участия в следующей встрече по программированию, которую вы организуете.

Дан следующий входной массив:

list1 = [
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 49, 'language': 'Ruby', 'githubAdmin': 'no' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript', 'githubAdmin': 'no' }
  ]

написать функцию, которая при выполнении будет findAdmin(list1, 'JavaScript')возвращает только
разработчиков JavaScript, являющихся администраторами GitHub:

[
  { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
  { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' }
]

Примечания:

    Первоначальный порядок должен быть сохранен.
    Если на данном языке нет разработчиков-администраторов GitHub, то возвращается пустой массив. [].
    Входной массив всегда будет допустимым и отформатированным, как в примере выше.
    Строки, указывающие, является ли кто-то администратором GitHub, всегда будут отформатированы
    следующим образом: 'yes' и 'no'(все строчные буквы).
    Строки, представляющие данный язык, всегда будут отформатированы одинаково
    (например, 'JavaScript'всегда будет отформатирован с использованием заглавных букв «J» и «S».
"""
import typing
import unittest


def find_admin(lst: list[dict], lang: str) -> list[dict]:
    """
    Среди списка разработчиков ищет администраторов по заданному языку.
    """
    return [x for x in lst if x['language'] == lang and x['githubAdmin'] == 'yes']


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    lst1 = [
        { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
        { 'firstName': 'Kseniya', 'lastName': 'T.', 'country': 'Belarus', 'continent': 'Europe', 'age': 49, 'language': 'Ruby', 'githubAdmin': 'no' },
        { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' },
        { 'firstName': 'Piotr', 'lastName': 'B.', 'country': 'Poland', 'continent': 'Europe', 'age': 128, 'language': 'JavaScript', 'githubAdmin': 'no' },
    ]
    lst2 = [
        { 'firstName': 'Harry', 'lastName': 'K.', 'country': 'Brazil', 'continent': 'Americas', 'age': 22, 'language': 'JavaScript', 'githubAdmin': 'yes' },
        { 'firstName': 'Jing', 'lastName': 'X.', 'country': 'China', 'continent': 'Asia', 'age': 34, 'language': 'JavaScript', 'githubAdmin': 'yes' },
    ]
    test(find_admin, (
        ((lst1, 'JavaScript'), lst2),
        ((lst1, 'Ruby'), []),
        ((lst1, 'Python'), []),
    ))
