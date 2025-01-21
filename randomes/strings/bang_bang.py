"""
Все пользователи Unix знают командную строку history. Он поставляется с набором полезных команд,
известных как bang команда.

Для получения дополнительной информации о командной строке истории вы можете посмотреть:

    Страница руководства -> просто введите man history в вашем терминале.
    Онлайн-страница руководства здесь .
    И для получения дополнительной информации о bang команда, вы можете прочитать эту статью

В этой первой ката мы изучим !! команда, согласно странице руководства, эта относится к предыдущей
команде. Это синоним слова !-1.

В этой ката вы должны выполнить функцию, которая принимает в качестве аргумента history со
следующим форматом:

  1  cd /pub
  2  more beer
  3  lost
  4  ls
  5  touch me
  6  chmod 000 me
  7  more me
  8  history

и это должно вернуть последнюю выполненную командную строку, в этом случае это будет history.
"""
import typing
import unittest


def bang_bang(history: str) -> str:
    """
    Возвращает последнюю команду из истории командной строки.
    """
    return history.split('\n')[-1][5:]


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(bang_bang, (
        ("   1  cd /pub\n  2  more beer\n  3  lost\n  4  ls \n  5  touch me \n  6  chmod 000 me \n  7  more me\n  8  history", "history"),
        ("   1  cd /pub\n  2  more beer\n  3  lost\n  4  ls \n  5  touch me \n  6  chmod 000 me \n  7  history\n  8  more me" , "more me"),
    ))
