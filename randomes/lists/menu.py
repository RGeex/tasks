"""
Создайте класс, имитирующий экран выбора. Курсор может двигаться влево или вправо!

В методе отображения верните строковое представление списка, но с квадратными
скобками вокруг выбранного в данный момент элемента. Также создайте методы
to_the_rightи to_the_leftкоторый перемещает курсор.

Курсор должен начинаться с индекса 0.

Курсор должен вернуться к началу, как только он достигнет конца. 
"""


class Menu:
    """Имитация перемещения курсора выбора."""
    def __init__(self, data: list) -> None:
        self.data = data
        self.curr = 0

    def display(self, curr=None) -> None:
        self.curr = (self.curr + {'+': 1, '-': -
                     1}.get(curr, 0)) % len(self.data)
        return [[x] if self.curr % len(self.data) == i else x for i, x in enumerate(self.data)]

    def to_the_right(self) -> None:
        return self.display('+')

    def to_the_left(self) -> None:
        return self.display('-')


def test() -> None:
    """Тестирование работы алгоритмов."""

    menu = Menu([1, 2, 3])
    data = (
        (menu.display(), [[1], 2, 3]),
        (menu.to_the_right(), [1, [2], 3]),
        (menu.to_the_right(), [1, 2, [3]]),
        (menu.to_the_right(), [[1], 2, 3]),
        (menu.to_the_left(), [1, 2, [3]]),
        (menu.to_the_left(), [1, [2], 3]),
    )

    for key, val in data:
        assert key == val


if __name__ == '__main__':
    test()
