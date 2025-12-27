"""
Кто убийца?
Некоторые люди погибли!

Вам удалось сузить круг подозреваемых до нескольких человек. К счастью, вы знаете каждого человека,
которого эти подозреваемые видели в день убийств.
Задача.

Дан словарь со всеми именами подозреваемых и всех, кого они видели в тот день, который может
выглядеть следующим образом:

{'James': ['Jacob', 'Bill', 'Lucas'],
 'Johnny': ['David', 'Kyle', 'Lucas'],
 'Peter': ['Lucy', 'Kyle']}

а также список имен умерших:

['Lucas', 'Bill']

вернуть имя убийцы, в нашем случае. 'James'потому что он единственный, кто видел и то,
и другое 'Lucas' и 'Bill'
"""
import unittest
from typing import Any, Callable, Dict, List, Tuple


def killer(suspect_info: Dict[str, List[str]], dead: List[str]) -> str:
    """
    Поиск убийцы.
    """
    return next((name for name, val in suspect_info.items() if not set(dead) - set(val)), '')


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(killer, (
        (({'James': ['Jacob', 'Bill', 'Lucas'], 'Johnny': ['David', 'Kyle', 'Lucas'], 'Peter': ['Lucy', 'Kyle']}, ['Lucas', 'Bill']), 'James'),
        (({'Brad': [], 'Megan': ['Ben', 'Kevin'], 'Finn': []}, ['Ben']), 'Megan'),
    ))
