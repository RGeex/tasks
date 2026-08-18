"""
В офисе стартапа возникла постоянная проблема с мусорным ведром. Из-за ограниченного бюджета они не нанимают уборщиков.
В результате сотрудники вынуждены добровольно опорожнять ведро. Выяснилось, что добровольная система не работает,
и ведро часто переполняется. Один из сотрудников предложил создать систему ротации, основанную на схеме рассадки персонала.

Создайте функцию, которая принимает двумерный массив имен. Функция должна возвращать один массив, содержащий имена
сотрудников в том порядке, в котором они должны очистить корзину.

Ситуацию усугубляет наличие в офисе временного персонала. Это означает, что схема рассадки меняется каждый месяц.
Могут меняться как имена сотрудников, так и количество рядов сидений. Убедитесь, что функция работает корректно
при тестировании с учетом этих изменений.

Примечания:

Все ряды всегда будут одинаковой длины.
В схеме рассадки не будет пустых мест.
Пустых массивов не будет.
Длина каждого ряда будет составлять не менее одного сиденья.
Примерная схема рассадки выглядит следующим образом:



Или в виде массива:

[ ["Stefan", "Raj",    "Marie"],
  ["Alexa",  "Amy",    "Edward"],
  ["Liz",    "Claire", "Juan"],
  ["Dee",    "Luke",   "Katie"] ]
График работы должен начинаться со Стефана и заканчиваться Ди, следуя зигзагообразному пути слева направо, как показано красной линией:


В этом случае вы ожидаете получить следующий результат:

["Stefan", "Raj", "Marie", "Edward", "Amy", "Alexa", "Liz", "Claire", "Juan", "Katie", "Luke", "Dee"])
"""
import unittest
from typing import Any, Callable, List, Tuple


def bin_rota(arr: List[List[str]]) -> List[str]:
    """
    Создает порядок сотрудников очередности отчистки корзины.
    """
    return [name for i, row in enumerate(arr) for name in (reversed(row) if i & 1 else row)]


def bin_rota_2(arr: List[List[str]]) -> List[str]:
    """
    Создает порядок сотрудников очередности отчистки корзины.
    """
    return sum([x[::(-1)**(i)] for i, x in enumerate(arr)], [])


def bin_rota_3(arr: List[List[str]]) -> List[str]:
    """
    Создает порядок сотрудников очередности отчистки корзины.
    """
    return [x for i, row in enumerate(arr) for x in (row[::-1] if i % 2 else row)]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(bin_rota, (
        ([
            ["Bob", "Nora"],
            ["Ruby", "Carl"],
        ],
        ["Bob", "Nora", "Carl", "Ruby"]),
        ([["Billy"]], ["Billy"]),
        ([["Billy", "Nancy"]], ["Billy", "Nancy"]),
        ([
            ["Billy"],
            ["Megan"],
            ["Aki"],
            ["Arun"],
            ["Joy"]],
        ["Billy", "Megan", "Aki", "Arun", "Joy"]),
        ([
            ["Sam", "Nina", "Tim", "Helen", "Gurpreet", "Edward", "Holly", "Eliza"],
            ["Billy", "Megan", "Aki", "Arun", "Joy", "Anish", "Lee", "Maryan"],
            ["Nick", "Josh", "Pete", "Kavita", "Daisy", "Francesca", "Alfie", "Macy"]], ["Sam", "Nina", "Tim", "Helen", "Gurpreet", "Edward", "Holly", "Eliza", "Maryan", "Lee", "Anish", "Joy", "Arun", "Aki", "Megan", "Billy", "Nick", "Josh", "Pete", "Kavita", "Daisy", "Francesca", "Alfie", "Macy"]),
        ([
            ["Stefan", "Raj", "Marie"],
            ["Alexa", "Amy", "Edward"],
            ["Liz", "Claire", "Juan"],
            ["Dee", "Luke", "Elle"]],
            ["Stefan", "Raj", "Marie", "Edward", "Amy", "Alexa", "Liz", "Claire", "Juan", "Elle", "Luke", "Dee"]),
    ))
    test(bin_rota_2, (
        ([
            ["Bob", "Nora"],
            ["Ruby", "Carl"],
        ],
        ["Bob", "Nora", "Carl", "Ruby"]),
        ([["Billy"]], ["Billy"]),
        ([["Billy", "Nancy"]], ["Billy", "Nancy"]),
        ([
            ["Billy"],
            ["Megan"],
            ["Aki"],
            ["Arun"],
            ["Joy"]],
        ["Billy", "Megan", "Aki", "Arun", "Joy"]),
        ([
            ["Sam", "Nina", "Tim", "Helen", "Gurpreet", "Edward", "Holly", "Eliza"],
            ["Billy", "Megan", "Aki", "Arun", "Joy", "Anish", "Lee", "Maryan"],
            ["Nick", "Josh", "Pete", "Kavita", "Daisy", "Francesca", "Alfie", "Macy"]], ["Sam", "Nina", "Tim", "Helen", "Gurpreet", "Edward", "Holly", "Eliza", "Maryan", "Lee", "Anish", "Joy", "Arun", "Aki", "Megan", "Billy", "Nick", "Josh", "Pete", "Kavita", "Daisy", "Francesca", "Alfie", "Macy"]),
        ([
            ["Stefan", "Raj", "Marie"],
            ["Alexa", "Amy", "Edward"],
            ["Liz", "Claire", "Juan"],
            ["Dee", "Luke", "Elle"]],
            ["Stefan", "Raj", "Marie", "Edward", "Amy", "Alexa", "Liz", "Claire", "Juan", "Elle", "Luke", "Dee"]),
    ))
    test(bin_rota_3, (
        ([
            ["Bob", "Nora"],
            ["Ruby", "Carl"],
        ],
        ["Bob", "Nora", "Carl", "Ruby"]),
        ([["Billy"]], ["Billy"]),
        ([["Billy", "Nancy"]], ["Billy", "Nancy"]),
        ([
            ["Billy"],
            ["Megan"],
            ["Aki"],
            ["Arun"],
            ["Joy"]],
        ["Billy", "Megan", "Aki", "Arun", "Joy"]),
        ([
            ["Sam", "Nina", "Tim", "Helen", "Gurpreet", "Edward", "Holly", "Eliza"],
            ["Billy", "Megan", "Aki", "Arun", "Joy", "Anish", "Lee", "Maryan"],
            ["Nick", "Josh", "Pete", "Kavita", "Daisy", "Francesca", "Alfie", "Macy"]], ["Sam", "Nina", "Tim", "Helen", "Gurpreet", "Edward", "Holly", "Eliza", "Maryan", "Lee", "Anish", "Joy", "Arun", "Aki", "Megan", "Billy", "Nick", "Josh", "Pete", "Kavita", "Daisy", "Francesca", "Alfie", "Macy"]),
        ([
            ["Stefan", "Raj", "Marie"],
            ["Alexa", "Amy", "Edward"],
            ["Liz", "Claire", "Juan"],
            ["Dee", "Luke", "Elle"]],
            ["Stefan", "Raj", "Marie", "Edward", "Amy", "Alexa", "Liz", "Claire", "Juan", "Elle", "Luke", "Dee"]),
    ))
