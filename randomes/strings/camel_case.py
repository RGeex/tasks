"""
Напишите метод (или функцию, в зависимости от языка), который преобразует строку в верблюжий
регистр, то есть первая буква всех слов должна быть заглавной, а пробелы должны быть удалены.
Примеры (ввод -> вывод):

"hello case" --> "HelloCase"
"camel case word" --> "CamelCaseWord"
"""

def camel_case(s: str) -> str:
    """
    Строку разделенную пробелами преобразует в CameCase.
    """
    return ''.join(s.title().split())


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = ( 
        ("", ""),
        ("test case", "TestCase"),
        ("say hello ", "SayHello"),
        (" camel case word", "CamelCaseWord"),
        ("camel case method", "CamelCaseMethod"),
    )
    for key, val in data:
        assert camel_case(key) == val


if __name__ == '__main__':
    test()
