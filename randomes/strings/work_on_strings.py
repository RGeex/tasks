"""
Ваша задача – Объединить две строки . Но учтите правило...

Кстати, не надо проверять ошибки или неверные входные значения, все ок, без подвохов, всего две
входные строки и как следствие одна выходная ;-)...

И вот правило:
Входные строки a и b: для каждого символа в строке a поменять регистр каждого вхождения одного и
того же символа в строке b. Затем выполните ту же замену регистра с обратными входами. Вернуть
одну строку, состоящую из измененной версии a за которым следует измененная версия b. Символ a
находится в b независимо от того, в верхнем или нижнем регистре — см. также тестовые примеры.
Думаю, это всё ;-)...

Несколько простых примеров:

Input: "abc" and "cde"      => Output: "abCCde" 
Input: "ab" and "aba"       => Output: "aBABA"
Input: "abab" and "bababa"  => Output: "ABABbababa"

Еще раз для последнего примера - описание от KenKamau, см. дискурс ;-):

а) поменять регистр символов в строке b для каждого появления этого символа в строке a
голец 'a' встречается дважды в строке a, поэтому мы меняем все местами 'a' в строке b дважды.
Это означает, что мы начинаем с "bababa" затем "bAbAbA" => "bababa"
голец 'b' встречается дважды в строке a и так строка b движется следующим образом: начните с
"bababa" затем "BaBaBa" => "bababa"

б) затем поменяйте регистр символов в строке a для каждого вхождения в строку b
голец 'a' происходит 3 раз в строке b. Итак, строка a меняет местами случаи следующим образом:
начните с "abab" тогда => "AbAb" => "abab" => "AbAb"
голец 'b' происходит 3 раз в строке b. Итак, строка a меняет местами следующим образом: начните
с "AbAb" тогда => "ABAB" => "AbAb" => "ABAB".

в) объединить новые строки a и b
возвращаться "ABABbababa"
"""
import typing
from collections import Counter


def work_on_strings(a: str, b: str) -> str:
    """
    Объединяет слова, производя замены регистра букв, если это необходимо.
    """
    res, tmp = '', (a, b)
    for i, x in enumerate(tmp):
        for k, v in Counter(tmp[not i].lower()).items():
            if v % 2:
                x = [[w, w.swapcase()][k == w.lower()] for w in x]
        res += ''.join(x)
    return res


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""
    import unittest

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(work_on_strings, (
        (("abc", "cde"), "abCCde"),
        (("abcdeFgtrzw", "defgGgfhjkwqe"), "abcDeFGtrzWDEFGgGFhjkWqE"),
        (("abcdeFg", "defgG"), "abcDEfgDEFGg"),
        (("abab", "bababa"), "ABABbababa"),
    ))
