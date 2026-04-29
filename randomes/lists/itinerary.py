"""
Маршрут путешествия

Путешествуя по миру, вы проезжаете через разные аэропорты.

TRN -> FCO -> JFK

А затем вернуться домой.

JFK - TRN

Для того чтобы предложить уникальный список аэропортов, которые будут использоваться для вашей
поездки, нам необходимо создать itineraryФункция, позволяющая сжать список аэропортов, включив
в него только уникальные комбинации въезда/выезда.

Например, поездка с:

[TRN-FCO] [FCO-JFK] [JFK-TRN]

Должно быть представлено следующим образом:

TRN-FCO-JFK-TRN

Это уникальный список ступенек аэропорта.

Теперь в нашей базе данных мы сохраняем информацию о поездках в виде списка объектов со свойствами
"прибытие/отъезд", и вы всегда будете получать этот список, отсортированный должным образом.

[
  {'in': "TRN", 'out': "FCO"},
  {'in': "FCO", 'out': "JFK"},
  {'in': "JFK", 'out': "FCO"}
]

Теперь нам нужно создать вспомогательную функцию. itineraryДля JavaScript, извлекающего уникальный
список аэропортов:

travel = itinerary([
  {'in': "TRN", 'out': "FCO"},
  {'in': "FCO", 'out': "JFK"},
  {'in': "JFK", 'out': "FCO"}
]); # TRN-FCO-JFK-FCO

Или класс помощников Routeдля C#/C++:
"""
import unittest
from typing import Any, Callable, Dict, List, Tuple


def itinerary1(travel: List[Dict[str, str]]) -> str:
    """
    Создает маршрут путешествия.
    """
    return '-'.join((f'{x["in"]}-' if not i or i and t != x["in"] else '') + f'{(t := x["out"])}' for i, x in enumerate(travel))


def itinerary2(travel: List[Dict[str, str]]) -> str:
    """
    Создает маршрут путешествия.
    """
    return '-'.join('-'.join(list(x.values())[i and x['in'] == travel[i - 1]['out']:]) for i, x in enumerate(travel))


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(itinerary1, (
        ([{'in': "TRN", 'out': "FCO"}], "TRN-FCO"),
        ([{'in': "TRN", 'out': "FCO"}, {'in': "CIA", 'out': "JFK"}], "TRN-FCO-CIA-JFK"),
        ([{'in': "TRN", 'out': "FCO"}, {'in': "FCO", 'out': "JFK"}], "TRN-FCO-JFK"),
        ([{'in': "TRN", 'out': "FCO"}, {'in': "CIA", 'out': "TRN"}], "TRN-FCO-CIA-TRN"),
        ([{'in': "TRN", 'out': "FCO"}, {'in': "FCO", 'out': "TRN"}], "TRN-FCO-TRN"),
    ))
    test(itinerary2, (
        ([{'in': "TRN", 'out': "FCO"}], "TRN-FCO"),
        ([{'in': "TRN", 'out': "FCO"}, {'in': "CIA", 'out': "JFK"}], "TRN-FCO-CIA-JFK"),
        ([{'in': "TRN", 'out': "FCO"}, {'in': "FCO", 'out': "JFK"}], "TRN-FCO-JFK"),
        ([{'in': "TRN", 'out': "FCO"}, {'in': "CIA", 'out': "TRN"}], "TRN-FCO-CIA-TRN"),
        ([{'in': "TRN", 'out': "FCO"}, {'in': "FCO", 'out': "TRN"}], "TRN-FCO-TRN"),
    ))
