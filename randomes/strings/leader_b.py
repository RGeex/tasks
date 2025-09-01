"""
Мы все хотим подняться в таблице лидеров. Даже учитывая внушительные
результаты, приятно знать, насколько ты близок к этому...

В этом ката вам будет предоставлено имя пользователя и его счет, ваш
счет (не ваш настоящий счет), и вам нужно подсчитать, сколько ката вам
нужно выполнить, чтобы превзойти его счет, ровно на 1 балл.

Поскольку это простая версия (которую в будущем станет сложнее освоить),
предположим, что доступны только ката Бета и ката 8 кю. Стоимость 3 и 1
балл соответственно.

Возвращает строку в следующем формате: "To beat <user>'s score, I must
complete <x> Beta kata and <y> 8kyu kata."

Если общее количество ката, которые вам нужно выполнить, >1000, добавьте
"Dammit!"до конца строки, вот так: "To beat <user>'s score, I must complete
<x> Beta kata and <y> 8kyu kata. Dammit!"

Если ваш рейтинг выше, чем у пользователя, верните "Winning!"и если они
равны, вернуть "Only need one!"
"""
import typing
import unittest


def leader_b(user: str, user_score: int, your_score: int) -> str:
    """
    Определяет разницу в очках достижений 2-х пользователей.
    """
    if your_score < user_score:
        x, y = divmod(user_score - your_score, 3)
        return f"To beat {user}'s score, I must complete {x} Beta kata and {y} 8kyu kata.{['', ' Dammit!'][x + y > 1000]}"
    return "Winning!" if your_score > user_score else "Only need one!"


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(leader_b, (
        (('g964', 36097, 20000), "To beat g964's score, I must complete 5365 Beta kata and 2 8kyu kata. Dammit!"),
        (('GiacomoSorbi', 23914, 23867), "To beat GiacomoSorbi's score, I must complete 15 Beta kata and 2 8kyu kata."),
        (('ZozoFouchtra', 15991, 12000), "To beat ZozoFouchtra's score, I must complete 1330 Beta kata and 1 8kyu kata. Dammit!"),
        (('webtechalex', 884, 900), 'Winning!'),
        (('petegarvin1', 3307, 100), "To beat petegarvin1's score, I must complete 1069 Beta kata and 0 8kyu kata. Dammit!"),
        (('myjinxin2015', 15720, 15720), 'Only need one!'),
        (('AcesOfGlory', 2255, 1563), "To beat AcesOfGlory's score, I must complete 230 Beta kata and 2 8kyu kata."),
    ))
