"""
Наслаждаясь отпуском, вы отправляетесь на подводное плавание!

Катастрофа!! Лодка загорелась!!

Вам будет предоставлена ​​строка, в которой перечислены многие предметы, связанные с лодкой.
Если какой-либо из этих предметов — «Огонь», вы должны приступить к действию.
Измените любой экземпляр «Fire» на «~~». Затем верните строку.
"""
import typing
import unittest


def fire_fight(st: str) -> str:
    """
    Поиск и замена слова в строке.
    """
    return st.replace('Fire', '~~')
    

def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(fire_fight, (
        ("Boat Rudder Mast Boat Hull Water Fire Boat Deck Hull Fire Propeller Deck Fire Deck Boat Mast",
        "Boat Rudder Mast Boat Hull Water ~~ Boat Deck Hull ~~ Propeller Deck ~~ Deck Boat Mast"),
        ("Mast Deck Engine Water Fire",
        "Mast Deck Engine Water ~~"),
        ("Fire Deck Engine Sail Deck Fire Fire Fire Rudder Fire Boat Fire Fire Captain",
        "~~ Deck Engine Sail Deck ~~ ~~ ~~ Rudder ~~ Boat ~~ ~~ Captain"),
    ))
