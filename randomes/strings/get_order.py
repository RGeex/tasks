"""
В вашем ресторане начали работать новые кассиры.

Они хорошо принимают заказы, но не умеют писать слова с заглавной буквы или использовать пробел!

Все создаваемые ими заказы выглядят примерно так:

"milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza"

Кухонные работники грозятся уволиться из-за того, что сложно читать заказы.

Они предпочитают получать заказы в виде красивой чистой строки с пробелами и заглавными буквами, например:

"Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke"

Кухонный персонал ожидает, что блюда будут расположены в том же порядке, в котором они указаны в меню.

Пункты меню достаточно простые, в названиях пунктов нет дублирования:

1. Burger
2. Fries
3. Chicken
4. Pizza
5. Sandwich
6. Onionrings
7. Milkshake
8. Coke
"""

import re


def get_order(order: str) -> str:
    """
    Форматирование текста: разделение на отдельные слова с заглавной буквы.
    """
    menu = 'burger fries chicken pizza sandwich onionrings milkshake coke'.split()
    return ' '.join(sorted(re.findall(rf"({'|'.join(menu)})", order), key=menu.index)).title()


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (
            "milkshakepizzachickenfriescokeburgerpizzasandwichmilkshakepizza",
            "Burger Fries Chicken Pizza Pizza Pizza Sandwich Milkshake Milkshake Coke",
        ),
        (
            "pizzachickenfriesburgercokemilkshakefriessandwich",
            "Burger Fries Fries Chicken Pizza Sandwich Milkshake Coke",
        ),
    )
    for key, val in data:
        assert get_order(key) == val


if __name__ == '__main__':
    test()
