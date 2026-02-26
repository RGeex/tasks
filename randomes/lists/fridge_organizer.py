"""
Задача

У вас беспорядок в холодильнике! Чтобы избежать пищевых отходов, нужно в первую очередь решить,
что съесть, исходя из двух факторов: срока годности и количества .

Напишите функцию, которая принимает список продуктов питания и возвращает их названия,
отсортированные по показателю срочности .
Формат данных

Каждый продукт питания представляет собой объект , обладающий следующими атрибутами:

    nameНазвание блюда. (строка)
    expiry_days: Количество дней до истечения срока действия.
    (целое число; может быть отрицательным)
    is_almost_empty: true, если у вас осталось совсем немного. (логическое значение)

Правила сортировки

    Отклонить испорченный товар : Если до истечения срока годности осталось меньше 0 дней,
    товар испорчен. Не включать его в выходные данные.
    Сначала пустые предметы : почти пустые предметы идут перед предметами, которые не пусты.
    Срок годности : В этих группах товары с наименьшим сроком годности идут первыми.
    Алфавитный порядок : Если статус и срок действия совпадают, отсортируйте по имени в алфавитном порядке.

Пример

При наличии следующего списка продуктов питания:
Имя 	Срок действия истекает 	Почти пусто?
Молоко 	3 	ЛОЖЬ
Время 	3 	истинный
Йогурт 	1 	ЛОЖЬ
Старое мясо 	-1 	истинный
Тофу на сегодня 	0 	ЛОЖЬ

Вам следует вернуть:

["Jam", "Today's Tofu", "Yogurt", "Milk"]

Именно в таком порядке.
"""
import unittest
from typing import Any, Callable, List, Tuple


class FoodItem:
    def __init__(self, name: str, expiry_days: int, is_almost_empty: bool) -> None:
        self.name = name
        self.expiry_days = expiry_days
        self.is_almost_empty = is_almost_empty


def fridge_organizer(items: FoodItem) -> List[str]:
    """
    Сортирует список продуктов по приоритетных к употреблению, исключая испорченные.
    """
    return [x.name for x in sorted(items, key=lambda x: (-x.is_almost_empty, x.expiry_days, x.name)) if x.expiry_days >= 0]


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(fridge_organizer, (
        ([
            FoodItem("Milk", 3, False),
            FoodItem("Jam", 3, True),
            FoodItem("Yogurt", 1, False),
            FoodItem("Old Meat", -1, True),
            FoodItem("Today's Tofu", 0, False)
        ], ["Jam", "Today's Tofu", "Yogurt", "Milk"]),

        ([
            FoodItem("Zucchini", 5, False),
            FoodItem("Apples", 5, False)
        ], ["Apples", "Zucchini"]),
    ))
