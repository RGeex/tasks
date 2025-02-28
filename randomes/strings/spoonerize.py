"""
Спунеризм - это разговорная фраза, в которой первые буквы двух слов заменяются вокруг, часто с забавными результатами.

В своей самой основной форме спинеризм - это фраза с двумя словами, в которой заменяются только первые буквы каждого слова:

"not picking" --> "pot nicking"

Ваша задача состоит в том, чтобы создать функцию, которая принимает черту из двух слов, разделенных пространством: words и
возвращает ложку этих слов в строке, как в приведенном выше примере. «Слово» в контексте этой каты может содержать любую
буквы A через Z В верхнем или нижнем случае, а также числа 0 к 9Полем Хотя ложки посвящены буквам в области письменного
и разговорного языка, числа включены в входные данные для случайных тестовых случаев, и они не требуют особого обращения.

Примечание. Все входные строки будут содержать только два слова. Спунеризмы могут быть более сложными. Например, фразы из
трех слов, в которых заменяются первые буквы первых и последних слов: "pack of lies" --> "lack of pies" или более одной
буквы из слова заменяется: "flat battery --> "bat flattery" Вы не должны учитывать их или любые другие нюансы, связанные с ложками.
"""
import typing
import unittest


def spoonerize(st: str) -> str:
    """
    Создает из заданной строки спунеризм.
    """
    x = st.split()
    x[0], x[1] = x[-1][0] + x[0][1:], x[0][0] + x[-1][1:]
    return ' '.join(x)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(spoonerize, (
        ("nit picking", "pit nicking"),
        ("wedding bells", "bedding wells"),
        ("jelly beans", "belly jeans"),
        ("pop corn", "cop porn"),
    ))
