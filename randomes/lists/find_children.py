"""
Приближается Рождество, и у Санты длинный список, чтобы найти тех,
кто заслуживает подарков в этот знаменательный день. Пройдите по списку
детей и верните список, содержащий всех детей, которые были в списке Санты.
Не добавляйте ни одного ребенка более одного раза. Результат должен быть отсортирован.

Сравнение должно быть чувствительным к регистру, и возвращаемый список должен
содержать только одну копию каждого имени: "Sam" и "sam"Они разные, но "sAm" и "sAm"не являются.

"""
import unittest
from typing import Any, Callable, Tuple


def find_children(santas_list: list[str], children: list[str]) -> list[str]:
    """
    Сортирует список детей для санты, удяляя дубликаты.
    """
    return sorted([child for child in set(children) if child in santas_list])


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_children, (
        ((["Jason", "Jackson", "Jordan", "Johnny"], ["Jason", "Jordan", "Jennifer"]), ["Jason", "Jordan"]),
        ((["Jason", "Jackson", "Johnson", "JJ"], ["Jason", "James", "JJ"]), ["JJ", "Jason"]),
        ((["jASon", "JAsoN", "JaSON", "jasON"], ["JasoN", "jASOn", "JAsoN", "jASon", "JASON"]), ["JAsoN", "jASon"]),
    ))
