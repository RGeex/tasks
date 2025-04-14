"""
У меня есть parценность каждой лунки на поле для гольфа и моего удара scoreна каждой лунке.
Я храню их в виде строк, потому что записал их на листе бумаги. Прямо сейчас я использую эти строки,
чтобы вручную подсчитать свой счет в гольфе: взять разницу между моим фактическим scoreи parлунки и
сложите результаты по всем 18 лункам.

Например:

    Если бы я сделал 7 ударов на лунке, где пар был 5, мой счет был бы: 7 - 5 = 2
    Если бы я сделал лунку с одного удара, где пар был бы 4, мой счет был бы: 1 - 4 = -3.

Делать все эти вычисления вручную очень сложно! Можете ли вы помочь облегчить мне жизнь?
Обзор задачи

Завершите функцию, которая принимает две строки и вычисляет счет игры в гольф. Обе строки будут
иметь длину 18, и каждый символ в строке будет числом от 1 до 9 включительно.
"""
import typing
import unittest


def golf_score_calculator(par_string, score_string):
    """
    Подсчитывает очки для игры в гольф.
    """
    return sum(int(a) - int(b) for a, b in zip(score_string, par_string))
    

def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(golf_score_calculator, (
        (('443454444344544443', '353445334534445344'), -1),
    ))
