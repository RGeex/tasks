"""
Цветовая маркировка резисторов

Вы можете увидеть красочную диаграмму на этой странице Википедии , но основные цветовые коды
резисторов:

0: черный, 1: коричневый, 2: красный, 3: оранжевый, 4: желтый, 5: зеленый, 6: синий, 7: фиолетовый,
8: серый, 9: белый

Все резисторы имеют как минимум три полосы, при этом первая и вторая полосы обозначают первые две
цифры значения сопротивления, а третья указывает степень десяти, на которую их можно умножить,
например, резистор со значением 47 Ом, что равно 47 * 10^0 Ом, будет иметь три полосы «желтый,
фиолетовый, черный».

У большинства резисторов также есть четвертая полоса, обозначающая допуск — в таком комплекте
электроники, как ваш, допуск всегда будет составлять 5%, что обозначается золотой полосой. Итак,
в вашем комплекте резистор 47 Ом, указанный в приведенном выше абзаце, будет иметь четыре полосы
«желто-фиолетовое черное золото».
Ваша миссия

Ваша функция получит строку, содержащую необходимое вам значение Ом, за которым следует пробел
и слово «Ом» (чтобы избежать головной боли в Юникоде Codewars, я просто использую это слово
вместо символа Юникода Ом). Форматирование значения Ом зависит от величины значения:

    Для резисторов сопротивлением менее 1000 Ом значение Ом просто форматируется как простое
    число. Например, с резистором сопротивлением 47 Ом, указанным выше, ваша функция получит
    строку "47 ohms"и верните строку `"желтое фиолетовое черное золото".

    Для резисторов, сопротивление которых больше или равно 1000 Ом, но меньше 1000000 Ом, значение
    в Омах делится на 1000 и после него ставится строчная буква «k». Например, если ваша функция
    получила строку "4.7k ohms", ему нужно будет вернуть строку "yellow violet red gold".

    Для резисторов сопротивлением 1000000 Ом или более значение в Омах делится на 1000000 и после
    него ставится заглавная буква «М». Например, если ваша функция получила строку "1M ohms", ему
    нужно будет вернуть строку "brown black green gold".

Все значения резисторов тестового примера будут находиться в диапазоне от 10 Ом до 990 МОм.
Дополнительные примеры с некоторыми общими номиналами резисторов из вашего комплекта.

"10 ohms"        "brown black black gold"
"100 ohms"       "brown black brown gold"
"220 ohms"       "red red brown gold"
"330 ohms"       "orange orange brown gold"
"470 ohms"       "yellow violet brown gold"
"680 ohms"       "blue gray brown gold"
"1k ohms"        "brown black red gold"
"10k ohms"       "brown black orange gold"
"22k ohms"       "red red orange gold"
"47k ohms"       "yellow violet orange gold"
"100k ohms"      "brown black yellow gold"
"330k ohms"      "orange orange yellow gold"
"2M ohms"        "red black green gold"
"""
import typing
import unittest


def encode_resistor_colors(st: str) -> str:
    """
    По заданному сопротивлению определяет ветовую маркировку резистора.
    """
    x, n = dict(enumerate('black brown red orange yellow green blue violet gray white'.split())), st.split()[0]
    n = [f"{float(n[:-1]) * 10 ** {'k': 3, 'M': 6}.get(n[-1], 1):.0f}", n][n[-1].isdigit()]
    return ' '.join([x[int(c)] for c in n[:2]] + [x[n[2:].count('0')]] + ['gold'])


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(encode_resistor_colors, (
        ("10 ohms", "brown black black gold"),
        ("47 ohms", "yellow violet black gold"),
        ("100 ohms", "brown black brown gold"),
        ("220 ohms", "red red brown gold"),
        ("330 ohms", "orange orange brown gold"),
        ("470 ohms", "yellow violet brown gold"),
        ("680 ohms", "blue gray brown gold"),
        ("1k ohms", "brown black red gold"),
        ("4.7k ohms", "yellow violet red gold"),
        ("10k ohms", "brown black orange gold"),
        ("22k ohms", "red red orange gold"),
        ("47k ohms", "yellow violet orange gold"),
        ("100k ohms", "brown black yellow gold"),
        ("330k ohms", "orange orange yellow gold"),
        ("1M ohms", "brown black green gold"),
        ("2M ohms", "red black green gold"),
    ))
