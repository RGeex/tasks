"""
Завершите решение так, чтобы оно приняло входные данные n(целое число) и
возвращает строку, которая представляет собой десятичное представление
числа, сгруппированного запятыми после каждых трех цифр.

Предполагать: 0 <= n < 2147483647
Примеры

       1  ->           "1"
      10  ->          "10"
     100  ->         "100"
    1000  ->       "1,000"
   10000  ->      "10,000"
  100000  ->     "100,000"
 1000000  ->   "1,000,000"
35235235  ->  "35,235,235"
"""


def group_by_commas(n: int) -> str:
    """
    Форматирование числа в видес строки, разделенной
    по 3 символа.
    """
    return f'{n:,}'
    

def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (1, '1'),
        (10, '10'),
        (100, '100'),
        (1000, '1,000'),
        (10000, '10,000'),
        (100000, '100,000'),
        (1000000, '1,000,000'),
        (35235235, '35,235,235'),
    )
    for key, val in data:
        assert group_by_commas(key) == val


if __name__ == '__main__':
    test()
