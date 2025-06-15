"""
Дано 2 строки, ваша задача — выяснить, есть ли подстрока, которая появляется в обеих строках.
Вы вернете true, если найдете подстроку, которая появляется в обеих строках, или false, если нет.
Нас интересуют только подстроки, длина которых превышает одну букву.

#Примеры:

*Example 1*
SubstringTest("Something","Fun"); //Returns false

*Example 2*
SubstringTest("Something","Home"); //Returns true

В приведенном выше примере пример 2 возвращает true, поскольку оба ввода содержат подстроку «me».
(so ME thing и ho ME )
В примере 1 метод вернет false, поскольку something и fun не содержат общих подстрок.
(Мы не считаем «n» подстрокой в ​​этом Kata, поскольку она состоит всего из 1 символа)

#Правила: Строчные и заглавные буквы одинаковы. Так что 'A' == 'a'.
Мы учитываем только подстроки, длина которых > 1.

#Вход: Две строки с заглавными и строчными буквами. #Выход: Логическое значение, определяющее,
# есть ли общая подстрока между двумя входами.
"""
import typing
import unittest


def substring_test(s1: str, s2: str) -> bool:
    """
    Поиск в 2-х строках общих подстрок более 1 символа, не учитывая регистр.
    """
    return not next((0 for i in range(len(s1) - len(s1) % 2) if len(x := s1.lower()[i:i+2]) > 1 and x in s2.lower()), 1)


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(substring_test, (
        (("Something","Home"), True),
        (("Something","Fun"), False),
        (("Something",""), False),
        (("","Something"), False),
        (("BANANA","banana"), True),
        (("test","lllt"), False),
        (("",""), False),
        (("1234567","541265"), True),
        (("supercalifragilisticexpialidocious","SoundOfItIsAtrocious"), True),
    ))
