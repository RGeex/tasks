"""
У Дэйва есть много данных, к которым ему необходимо применить фильтры,
которые достаточно просты, но ему нужен более короткий способ сделать это.

Он хочет, чтобы следующие функции работали должным образом:

even # list([1,2,3,4,5]).even() should return [2,4]
odd # list([1,2,3,4,5]).odd() should return [1,3,5]
under # list([1,2,3,4,5]).under(4) should return [1,2,3]
over # list([1,2,3,4,5]).over(4) should return [5]
in_range # list([1,2,3,4,5]).in_range(1, 3) should return [1,2,3]

Они также должны работать при совместном использовании, например:

list(list([1,2,3,4,5,6,7,8,9,10]).even()).under(5) # should return [2,4]

И, наконец, фильтры должны принимать только целочисленные значения из массива,
например:

list(["a", 1, "b", 300, "x", "q", 63, 122, 181, "z", 0.83, 0.11]).even()
should return [300, 122]

Примечание. Список, не содержащий чисел, также будет проверен.
"""


class list:
    """
    Преобразования для списков.
    """
    def __init__(self, lst: list) -> None:
        self.lst = [x for x in lst if isinstance(x, int)]

    def odd(self) -> list:
        """
        Выбирает все не четные.
        """
        return [x for x in self.lst if x % 2]
    
    def even(self) -> list:
        """
        Выбирает все четные.
        """
        return [x for x in self.lst if not x % 2]

    def under(self, n: int) -> list:
        """
        Выбирает все меньше N.
        """
        return [x for x in self.lst if x < n]
    
    def over(self, n: int) -> list:
        """
        Выбирает все больше N.
        """
        return [x for x in self.lst if n < x]
    
    def in_range(self, a: int, b: int) -> list:
        """
        Выбирает все в диапазоне между A и B.
        """
        return [x for x in self.lst if a <= x <= b]
    

def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (list([1,2,3,4,5]).even(), [2,4]),
        (list([1,2,3,4,5]).odd(), [1,3,5]),
    )
    for key, val in data:
        assert key == val

if __name__ == '__main__':
    test()
