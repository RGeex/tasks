"""
Вам нужно написать функцию, которая принимает строку в качестве первого параметра.
Эта строка будет строкой слов.

Затем ожидается, что вы используете второй параметр, который будет целым числом,
чтобы найти соответствующее слово в данной строке. Первое слово будет представлено 0.

После того, как вы нашли строку, вы, наконец, умножаете на нее третий предоставленный
параметр, который также будет целым числом. Вам также необходимо добавить дефис между каждым словом.

Пример

modify_multiply ("This is a string", 3 ,5)

"""
import typing
import unittest


def modify_multiply(st: str, loc: int, num: int) -> str:
    """
    Создает новую строку из заданной по указанным параметрам.
    """
    return '-'.join([st.split()[loc]] * num)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(modify_multiply, (
        (("This is a string",3 ,5), "string-string-string-string-string"),
        (("Creativity is the process of having original ideas that have value. It is a process; it's not random.",8 ,10), "that-that-that-that-that-that-that-that-that-that"),
        (("Self-control means wanting to be effective at some random point in the infinite radiations of my spiritual existence",1 ,1), "means"),
        (("Is sloppiness in code caused by ignorance or apathy? I don't know and I don't care.",6 ,8), "ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance"),
        (("Everything happening around me is very random. I am enjoying the phase, as the journey is far more enjoyable than the destination.",2 ,5), "around-around-around-around-around"),
    ))
