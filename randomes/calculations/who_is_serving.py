"""
Ваши коллеги любят играть в настольный теннис, но часто забывают,
кто должен подавать в каждом раунде. Они просят вас создать программу,
которая будет определять подающего игрока в зависимости от номера текущего раунда.

Правила
Игра начинается с первого раунда, или currentRound=1.
Игрок 1 всегда начинает игру с подачи.
Подача переходит от одного игрока к другому каждые два раунда.
currentRoundне может быть отрицательным числом или нулем.
Оригинальные правила игры упрощены: нет исключения "равно" (подача не чередуется в каждом розыгрыше после "10-10").
Примеры
Подачи Player 1в 1-м раунде
Подача Player 1во втором раунде
Подача Player 2в 3-м раунде
Подача Player 2в 4-м раунде
Подача Player 1в 5-м раунде
Подачи Player 1в раунде 6tx
Подача Player 2в 7-м раунде
Подача Player 2в 8-м раунде
И так далее


"""
import unittest
from typing import Any, Callable, Tuple


def who_is_serving(current_round: int) -> int:
    """
    Определяет подающего в указанном раунде.
    """
    return [2, 1][current_round % 4 in (1, 2)]


def who_is_serving_2(current_round: int) -> int:
    """
    Определяет подающего в указанном раунде.
    """
    return current_round - 1 & 2 or 1


def test(func: Callable[[Any], Any], data: Tuple[Tuple[Any, Any], ...]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: Callable[[Any], Any], key: Any, val: Any) -> Callable[[Any], Any]:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(who_is_serving, (
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 1),
        (6, 1),
        (7, 2),
        (8, 2),
        (9, 1),
        (10, 1),
    ))
    test(who_is_serving_2, (
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 1),
        (6, 1),
        (7, 2),
        (8, 2),
        (9, 1),
        (10, 1),
    ))
