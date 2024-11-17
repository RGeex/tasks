"""
Задача:

Ваша функция должна возвращать допустимое регулярное выражение.
Это шаблон, который обычно используется для сопоставления частей
строки. В этом случае будет использоваться для проверки того,
все ли символы, указанные во входных данных, присутствуют в строке.
Вход

Непустая строка уникальных символов алфавита в верхнем и нижнем регистре.
Выход

Строка шаблона регулярного выражения.
Примеры

Ваша функция должна возвращать строку.

# Function example
def regex_contains_all(st): 
  return r"abc"

Этот шаблон регулярного выражения будет проверен следующим образом.

# Test
abc = 'abc'
pattern = regex_contains_all(abc)
st = 'zzzaaacccbbbzzz'
bool(re.match(pattern, st), f"Testing if {st} contains all characters in {abc}
with your pattern {pattern}") -> True
"""


import re


def regex_contains_all(st: str) -> str:
    """
    Создает регулярное выражения для поиска в строке всех
    значений.
    """
    return ''.join(f'(?=.*{x})' for x in st)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('bca', True),
        ('baczzz', True),
        ('ac', False),
        ('bc', False),
        ('cb', False),
    )
    for key, val in data:
        assert bool(re.match(regex_contains_all('abc'), key)) == val


if __name__ == '__main__':
    test()
