"""
Заемщики — крошечные, крошечные вымышленные люди. Как крошечные, крошечные люди, они должны
быть уверены, что их не заметят, или, что еще важнее, не наступят на них.

В результате заемщики говорят очень-очень тихо. Они обнаруживают, что capitals and
punctuationлюбого рода заставляют их повышать голос и подвергают их опасности.

Молодые заемщики умоляли своих родителей stop using caps and punctuation.

Измените вводимый текст sвыступление нового заемщика. Помогите спасти следующее поколение!
"""
import typing
import unittest


def borrow(st: str) -> str:
    """
    Спасение заемщиков.
    """
    return ''.join(x for x in st.lower() if x.isalpha())



def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(borrow, (
        ('WhAt! FiCK! DaMn CAke?', 'whatfickdamncake'),
        ('THE big PeOpLE Here!!', 'thebigpeoplehere'),
        ('i AM a TINY BoY!!', 'iamatinyboy'),

    ))
