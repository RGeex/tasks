"""
Вы — воздушный пожарный (тот, кто сбрасывает воду на пожары сверху, чтобы потушить их),
и ваша цель — подсчитать минимальное количество бомб, которое нужно сбросить, чтобы
полностью потушить пожар (у пожарной службы есть бюджетные проблемы, и вы не можете
просто сбрасывать тонны бомб, им нужны деньги на ежегодную рождественскую вечеринку).

Данная строка представляет собой двумерную плоскость случайной длины, состоящую из двух символов:

    xпредставляющий огонь
    Yпредставляющие здания.

Сброшенная вами вода не может проникнуть сквозь здания, поэтому отдельные участки пожара
следует тушить отдельно.

Ваши водяные бомбы могут тушить только смежные участки пожара шириной до (параметр w).

Вам необходимо вернуть минимальное количество водяных бомб, необходимое для тушения
пожара в цепочке.

Примечание: все введенные данные будут действительными.
Примеры

"xxYxx" and w = 3      -->  2 waterbombs needed
"xxYxx" and w = 1      -->  4
"xxxxYxYx" and w = 5   -->  3
"xxxxxYxYx" and w = 2  -->  5
"""
import typing
import unittest


def waterbombs(fire: str, w: int) -> int:
    return sum(len(x) // w + bool(len(x) % w) for x in fire.split('Y'))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(waterbombs, (
        (("xxxxYxYx", 4), 3),
        (("xxYxx", 3), 2),
    ))
