"""
Вы устраиваетесь на новую работу в компанию Eggman Movers. Ваша первая задача — написать метод,
который позволит административному персоналу вводить имя человека и возвращать информацию
о его должности в компании.

Вам будет предоставлен массив литералов объектов, содержащих текущих сотрудников компании.
Ваш код должен найти сотрудника с совпадающими именем и фамилией, а затем вернуть роль для
этого сотрудника, или, если сотрудник не найден, вернуть сообщение "Здесь не работает!".

Массив предварительно загружен и может быть использован в качестве источника данных с помощью
переменной. employees( $employees(в Ruby). Используется следующая структура.

employees = [ {'first_name': "Dipper", 'last_name': "Pines", 'role': "Boss"}, ...... ]

В массиве нет повторяющихся имен, и передаваемое имя будет представлять собой одну строку с
пробелом между именем и фамилией, например, Jane Doe или просто имя.
"""
import unittest
from typing import Any, Callable, Tuple


employees = [
    {'first_name': 'Ollie', 'last_name': 'Hepburn', 'role': 'Boss'},
    {'first_name': 'Morty', 'last_name': 'Smith', 'role': 'Truck Driver'},
    {'first_name': 'Peter', 'last_name': 'Ross', 'role': 'Warehouse Manager'},
    {'first_name': 'Cal', 'last_name': 'Neil', 'role': 'Sales Assistant'},
    {'first_name': 'Jesse', 'last_name': 'Saunders', 'role': 'Admin'},
    {'first_name': 'Anna', 'last_name': 'Jones', 'role': 'Sales Assistant'},
    {'first_name': 'Carmel', 'last_name': 'Hamm', 'role': 'Admin'},
    {'first_name': 'Tori', 'last_name': 'Sparks', 'role': 'Sales Manager'},
    {'first_name': 'Peter', 'last_name': 'Jones', 'role': 'Warehouse Picker'},
    {'first_name': 'Mort', 'last_name': 'Smith', 'role': 'Warehouse Picker'},
    {'first_name': 'Anna', 'last_name': 'Bell', 'role': 'Admin'},
    {'first_name': 'Jewel', 'last_name': 'Bell', 'role': 'Receptionist'},
    {'first_name': 'Colin', 'last_name': 'Brown', 'role': 'Trainee'},
]


def find_employees_role(name: str) -> str:
    """
    Поиск должности сотрудника по его имени.
    """
    return next((x['role'] for x in employees if f"{x['first_name']} {x['last_name']}" == name), "Does not work here!")


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(find_employees_role, (
        ("Dipper Pines", "Does not work here!"),
        ("Morty Smith", "Truck Driver"),
        ("Anna Bell", "Admin"),
        ("Anna", "Does not work here!"),
        ("Bell Anna", "Does not work here!"),
        ("Jewel Bell", "Receptionist"),
        ("Bell Jewel", "Does not work here!"),
    ))
