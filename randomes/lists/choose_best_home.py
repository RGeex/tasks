"""
Выберите лучший новый дом
Обзор

Вы ищете идеальное место для переезда! У вас есть список доступных вариантов жилья,
словарь ваших предпочтений и приоритетный рейтинг. Ваша задача — рассчитать рейтинг
соответствия для каждого дома и указать название наиболее подходящего варианта.
Входные данные

    places(словарь): Коллекция доступных домов. Каждый дом представляет собой словарь,
    содержащий различные характеристики (например, {"type": "apartment", "ghosts": "none"}).
    preferences(словарь): Ваши идеальные значения для этих качеств
    (например, {"type": "apartment", "ghosts": "friendly_casper"}).
    priorities(список): Список названий признаков, упорядоченных от наиболее важных
    к наименее важным.

Правила подсчета очков

Баллы начисляются в зависимости от положения соответствующего признака внутри priorities список:

    Первый если пункт в вашем списке приоритетов оценивается в 6 баллов, характеристика дома
    соответствует вашим предпочтениям.
    Второй предмета , предмет стоит 5 баллов , третий — 4 балла , и так далее до шестого который
    стоит 1 балл .
    Любая характеристика, присутствующая в доме или предпочтениях, но не указанная в списке
    приоритетов, оценивается в 0 баллов . Отсутствующие или несовпадающие характеристики
    также оцениваются в 0 баллов .

Правило определения победителя при ничьей

Если два или более домов получили абсолютно одинаковый наивысший балл,
верните название дома, которое стоит первым в алфавитном порядке
(например, "MansionA"ритмы "MansionB"Если ничья при 0 баллах, правило
алфавитного порядка по-прежнему применяется!
Пошаговый пример

places = {
    "Apartment_A": {"type": "apartment", "cats": "zero_cats"},
    "House_B":     {"type": "house",     "cats": "many_cats_to_pet"}
}
preferences = {"type": "apartment", "cats": "many_cats_to_pet"}
priorities = ["type", "cats"]

# --- Scoring Apartment_A ---
# 'type' is 1st in priorities (6 pts). Apartment_A has 'apartment' (Matches preference!) -> +6 pts
# 'cats' is 2nd in priorities (5 pts). Apartment_A has 'zero_cats' (Mismatches 'many_cats_to_pet') -> +0 pts
# Total Score = 6

# --- Scoring House_B ---
# 'type' (6 pts). House_B has 'house' (Mismatches 'apartment') -> +0 pts
# 'cats' (5 pts). House_B has 'many_cats_to_pet' (Matches preference!) -> +5 pts
# Total Score = 5

# Winner: "Apartment_A"

Напишите функцию choose_best_home(places, preferences, priorities)Это вычисляет наиболее подходящее место назначения!

"""
import unittest
from typing import Any, Callable, Dict, List, Tuple


def choose_best_home(places: List[Dict[str, Dict[str, str]]], preferences: Dict[str, str], priorities: List[str]) -> str:
    """
    Определяет апартаменты учитывая приоритет.
    """
    return min(places.items(), key=lambda x: (sum(x[1].get(p) == preferences.get(p) and i for i, p in enumerate(priorities, -6)), x[0]))[0]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(choose_best_home, (
        (
            (
                {
                    "Apartment_A": {"type": "apartment", "cats": "zero_cats"},
                    "House_B":     {"type": "house",     "cats": "many_cats_to_pet"},
                },
                {"type": "apartment", "cats": "many_cats_to_pet"},
                ["type", "cats"],
            ),
            "Apartment_A",
        ),
        (
            (
                {
                    "Mansion_B": {"type": "mansion"},
                    "Apartment_A": {"type": "mansion"},
                },
                {"type": "mansion"},
                ["type"],
            ),
            "Apartment_A",
        ),
    ))
