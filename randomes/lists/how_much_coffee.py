"""
Всем известно, что ты слишком много времени проводишь без сна по ночам...

Ваша задача — определить, сколько кофе вам нужно, чтобы не заснуть после ночи.
Вам нужно будет доработать функцию, которая принимает в качестве аргументов
массив событий. На основе этого списка вы должны вернуть количество кофе,
необходимое для того, чтобы не заснуть в течение дня. Примечание :
если количество превышает 3, верните сообщение «Вам нужен дополнительный сон».

Список событий может содержать следующее:

    Вы пришли сюда, чтобы решить несколько ката («cw»).
    У вас есть собака или кошка, которые просто решили проснуться слишком рано ('собака' | 'кошка').
    Вы просто смотрите фильм («фильм»).
    Могут присутствовать и другие события, которые будут представлены произвольной строкой,
    просто проигнорируйте это.

Каждое событие может быть написано строчными буквами или прописными. Если оно написано строчными
буквами, вам потребуется 1 чашка кофе на событие, а если прописными — 2 чашки кофе.

"""
import unittest
from typing import Any, Callable, List, Tuple


def how_much_coffee(events: List[str]) -> int | str:
    """
    Определяет кол-во чашек кофе.
    """
    return x if (x := sum(x.isupper() + 1 for x in events if x.lower() in ('cat', 'dog', 'cw', 'movie'))) < 4 else 'You need extra sleep'


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(how_much_coffee, (
        ([], 0),
        (['cw'], 1),
        (['CW'], 2),
        (['cw', 'CAT'], 3),
        (['cw', 'CAT', 'DOG'], 'You need extra sleep'),
        (['cw', 'CAT', 'cw=others'], 3),
    ))
