"""
Даны 2 числа, не изменяя последовательность цифр в числах,
составить из них максимальное и минимальные значения.

Например:
123, 321 => 323
91, 123 => 193
"""


class NumberComparison:
    """Использует переденные числа в одно число, не изменяя последовательность
    цифр в числах.
    min - минимальное число
    max - максимальное число
    """

    def __init__(self, *args: int) -> None:
        # преобразование чисел в строки
        self._args = tuple(map(str, args))

    def _calc(self, option: str) -> int:
        """Согласно условию сравнивает цифры чисел, возвращает новое число."""
        result = ''
        # добавачная цифра вместо пустой, если длины чисел разные
        default = {'min': '9', 'max': '0'}.get(option)
        for i in range(1, max(map(len, self._args)) + 1):
            temp = []
            for values in self._args:
                # если числа разной длины, замена на значение по умолчанию пустой
                temp.append(values[-i] if i <= len(values) else default)
                # сравнение цифр чисел по условию, добавление к результату
            result = {'min': min, 'max': max}.get(option)(temp) + result

        return int(result)

    @property
    def min(self) -> int:
        """Минимальное значение из цифр заданных чисел,
        не меняя последовательности цифр."""
        return self._calc('min')

    @property
    def max(self) -> int:
        """Максимальное значение из цифр заданных чисел,
        не меняя последовательности цифр."""
        return self._calc('max')


def test() -> None:
    """Тестирование работы алгоритмов."""
    data = [
        ((123, 4321), 4121, 4323),
        ((4321, 123), 4121, 4323),
        ((123, 321), 121, 323),
        ((123, 0), 120, 123),
        ((0, 0), 0, 0),
    ]

    for nums, mins, maxs in data:
        nc = NumberComparison(*nums)
        assert nc.min == mins
        assert nc.max == maxs


if __name__ == '__main__':
    test()
