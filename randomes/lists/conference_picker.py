"""
Люси обожает путешествовать. К счастью, она — известный специалист в области компьютерных наук и
может ездить на международные конференции за счет бюджета своего отдела.

Каждый год Общество интересных исследований в области компьютерных наук (SECSR) организует
несколько конференций по всему миру. Люси всегда выбирает из этого списка одну конференцию,
которая проводится в городе, где она еще не была, и если у нее остается несколько вариантов,
она выбирает конференцию, которая, по ее мнению, наиболее актуальна для ее области исследований.

Напишите функцию выбора конференции, которая принимает два аргумента:

    Cities visitedСписок городов, которые Люси уже посещала, представленный в виде массива строк.
    Cities offeredСписок городов, которые примут конференции SECSR в этом году, представлен в виде
    массива строк. Cities offeredСписок конференций будет упорядочен по степени их значимости для
    исследований Люси (от наиболее значимых к наименее значимым).

Функция должна возвращать город, который Люси должна посетить, в виде строки.

Также обратите внимание:

    Следует учитывать возможность того, что Люси раньше не бывала ни в одном из этих городов.
    SECSR организует как минимум две конференции в год.
    Если все предлагаемые конференции проводятся в городах, которые Люси уже посещала, функция
    должна вернуться. "No worthwhile conferences this year!"( Nothing(на Haskell)

Пример:

Cities visited = ["Mexico City","Johannesburg","Stockholm","Osaka","Saint Petersburg","London"]
Cities offered = ["Stockholm","Paris","Melbourne"]
Expected solution ---> "Paris"
"""
import unittest
from typing import Any, Callable, List, Tuple


def conference_picker(cities_visited: List[str], cities_offered: List[str]) -> str:
    """
    Определяет слудующий город, который нужно посетить.
    """
    visited = {}.fromkeys(cities_visited, 0)
    return next((city for city in cities_offered if visited.get(city) is None), 'No worthwhile conferences this year!')


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(conference_picker, (
        (([], ['Philadelphia', 'Osaka', 'Tokyo', 'Melbourne']), 'Philadelphia'),
        (([], ['Brussels', 'Madrid', 'London']), 'Brussels'),
        (([], ['Sydney', 'Tokyo']), 'Sydney'),
        ((['London', 'Berlin', 'Mexico City', 'Melbourne', 'Buenos Aires', 'Hong Kong', 'Madrid', 'Paris'], ['Berlin', 'Melbourne']), 'No worthwhile conferences this year!'),
        ((['Beijing', 'Johannesburg', 'Sydney', 'Philadelphia', 'Hong Kong', 'Stockholm', 'Chicago', 'Seoul', 'Mexico City', 'Berlin'], ['Stockholm', 'Berlin', 'Chicago']), 'No worthwhile conferences this year!'),
        ((['Rome'], ['Rome']), 'No worthwhile conferences this year!'),
        ((['Milan'], ['London']), 'London'),
        ((['Mexico City', 'Dubai', 'Philadelphia', 'Madrid', 'Houston', 'Chicago', 'Delhi', 'Seoul', 'Mumbai', 'Lisbon', 'Hong Kong', 'Brisbane', 'Stockholm', 'Tokyo', 'San Francisco', 'Rio De Janeiro'], ['Lisbon', 'Mexico City']), 'No worthwhile conferences this year!'),
        ((["Gatlantis", "Baldur's Gate", "Gotham City", "Mystara", "Washinkyo", "Central City"], ["Mystara", "Gatlantis", "MegaTokyo", "Genosha", "Central City", "Washinkyo", "Gotham City", "King's Landing", "Waterdeep"]), 'MegaTokyo'),
        ((["Thay", "Camelot"], ["Waterdeep", "Washinkyo"]), 'Waterdeep'),
    ))
