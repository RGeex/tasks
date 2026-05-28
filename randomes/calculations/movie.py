"""
Мой друг Джон любит ходить в кино. Он может выбирать между системой А и системой Б.

Система А: он покупает билет (15 долларов) каждый раз
Система Б: он покупает карту (500 долларов) и первый билет за 0,90 от стоимости билета.
Затем за каждый дополнительный билет он платит в 0,90 раза больше, чем цена,
уплаченная за предыдущий билет.

Пример:

Если Джон сходит в кино 3 раза:

System A : 15 * 3 = 45
System B : 500 + 15 * 0.90 + (15 * 0.90) * 0.90 + (15 * 0.90 * 0.90) * 0.90 ( = 536.5849999999999, no rounding for each ticket)

Джон хочет узнать, сколько раз ему нужно сходить в кино, чтобы конечный результат
применения Системы Б, округленный до ближайшего доллара, оказался дешевле,
чем при использовании Системы А.

Функция movieимеет 3 параметра: card(цена карты), ticket(обычная цена) билет),
perc(долю от того, что он заплатил за предыдущий билет) и возвращает первый nтаким образом, что

ceil(price of System B) < price of System A.

Ещё примеры:

movie(500, 15, 0.9) should return 43 
    (with card the total price is 634, with tickets 645)
movie(100, 10, 0.95) should return 24 
    (with card the total price is 235, with tickets 240)

"""
import unittest
from typing import Any, Callable, Tuple
from math import ceil


def movie(card: int, ticket: int, perc: float) -> int:
    """
    Определяет мин кол-во посещений для того что бы окупить систему Б.
    """
    n = 1
    while ceil(card := card + ticket * perc ** n) >= ticket * n:
        n += 1
    return n


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(movie, (
        ((500, 15, 0.9), 43),
        ((100, 10, 0.95), 24),
        ((0, 10, 0.95), 2),
    ))
