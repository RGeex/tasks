"""
Ребенок Алана иногда может раздражать.

Когда Алан приходит домой и рассказывает своему ребенку,
чего он сегодня достиг, тот никогда ему не верит.

Будь этим ребенком.

Ваша функция AlanAnnoyingKid принимает на вход предложение,
произнесенное Аланом (строку). Предложение содержит следующую структуру:

"Today I " + [action_verb] + [object] + "."

(e.g.: "Today I played football.")

Ваша функция вернет ответ ребенка Алана, который представляет собой еще одно
предложение со следующей структурой:

"I don't think you " + [action_performed_by_alan] + " today, I think you " +
["did" OR "didn't"] + [verb_of _action_in_present_tense] + [" it!" OR " at all!"]

(e.g.:"I don't think you played football today, I think you didn't play at all!")

Обратите внимание на различную структуру в зависимости от наличия отрицания в
первом предложении Алана (например, говорит ли Алан: «Я не играю в футбол» или
«Я играл в футбол»).

! Также обратите внимание: ребенок Алана молод и использует только простые
правильные глаголы, в которых используется простое «ed» для образования прошедшего
времени. Есть случайные тестовые случаи.

Еще несколько примеров:

input  = "Today I played football."
output = "I don't think you played football today, I think you didn't play at all!"

input  = "Today I didn't attempt to hardcode this Kata."
output = "I don't think you didn't attempt to hardcode this Kata today, I think you did attempt it!"
      
input  = "Today I didn't play football."
output = "I don't think you didn't play football today, I think you did play it!"
      
input  = "Today I cleaned the kitchen."
output = "I don't think you cleaned the kitchen today, I think you didn't clean at all!"
"""
import typing
import unittest


def alan_annoying_kid(s: str) -> str:
    """
    Отрицает заданное высказывание.
    """
    a = s.replace('Today I ', '')[:-1]
    x = a.replace('didn\'t ', '')
    b = f'n\'t {w[:-2]} at all' if (w := x.split(' ', 1)[0]).endswith('ed') else f' {w} it'
    return f"I don't think you {a} today, I think you did{b}!"


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(alan_annoying_kid, (
        ("Today I played football.","I don't think you played football today, I think you didn't play at all!"),
        ("Today I didn't play football.","I don't think you didn't play football today, I think you did play it!"),
        ("Today I didn't attempt to hardcode this Kata.","I don't think you didn't attempt to hardcode this Kata today, I think you did attempt it!"),
        ("Today I cleaned the kitchen.","I don't think you cleaned the kitchen today, I think you didn't clean at all!"),
        ("Today I learned to code like a pro.","I don't think you learned to code like a pro today, I think you didn't learn at all!"),
    ))
