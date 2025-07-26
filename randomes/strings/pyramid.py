"""
Задача очень простая.

Вам необходимо вернуть пирамиды. Дано число nвы печатаете пирамиду с nполы

Например, если дано n=4вам необходимо распечатать эту пирамиду:

   /\\
  /  \\
 /    \\
/______\\
   

Другой пример, учитывая n=6вам необходимо распечатать эту пирамиду:

     /\\
    /  \\
   /    \\ 
  /      \\ 
 /        \\ 
/__________\\ 

Другой пример, если n=10, вам необходимо распечатать эту пирамиду:

         /\\ 
        /  \\ 
       /    \\ 
      /      \\ 
     /        \\ 
    /          \\ 
   /            \\ 
  /              \\ 
 /                \\ 
/__________________\\ 

Примечание: в конце строки необходимо добавить символ перевода строки.
n=0следует так вернуться "\n".

"""
import typing
import unittest


def pyramid(n: int) -> str:
    """
    Рисует пирамиду.
    """
    return ''.join(f'{" " * (n - i - 1)}/{i * 2 * ["_", " "][i != n - 1]}\\\n' for i in range(n))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(pyramid, (
        (4,  "   /\\\n  /  \\\n /    \\\n/______\\\n"),
        (6,  "     /\\\n    /  \\\n   /    \\\n  /      \\\n /        \\\n/__________\\\n"),
        (10, "         /\\\n        /  \\\n       /    \\\n      /      \\\n     /        \\\n    /          \\\n   /            \\\n  /              \\\n /                \\\n/__________________\\\n"),
    ))
