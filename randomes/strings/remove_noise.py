"""
У нас сломан мессенджер, который вносит помехи во входящие сообщения.
Мы знаем, что наши сообщения нельзя написать с помощью... %$&/#·@|º\\ª
К сожалению, наша машина вносит помехи, из-за чего наше сообщение приходит с такими символами,
как: %$&/#·@|º\ªв нашем первоначальном сообщении.

Ваша задача — написать функцию, которая удалит этот «шум» из сообщения.

    Обратите внимание, что шум может быть только %$&/#·@|º\\ª другие персонажи не считаются шумом.

Например:

remove_noise("h%e&·%$·llo w&%or&$l·$%d")
# returns hello world

"""
import unittest
from typing import Any, Callable, Tuple


def remove_noise(st: str) -> str:
    """
    Удаляет шум из сообщения.
    """
    return st.translate(str.maketrans('', '', '%$&/#·@|º\\ª'))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(remove_noise, (
        ("%$&/#·@|º\\ª", ""),
        ("h%e&·%$·llo w&%or&$l·$%d", "hello world"),
        ("he%$·ll@o c$&%odi%&ng for ev|#·ery&$$#$on%$·e", "hello coding for everyone"),
        ("c|o@$%de%w@a·$r%s &rºocªks", "codewars rocks"),
    ))
