"""
Создание пользовательских ссылок

Ваша задача — создать пользовательские ссылки для URL-адреса. Вам будет присвоено имя пользователя,
и вы должны вернуть действительную ссылку.
Пример

generate_link('matt c')
http://www.codewars.com/users/matt%20c

"""

from urllib.parse import quote


def generate_link(user: str) -> str:
    """
    Преобразование строки (пользователя) в url адрес (ascii)
    """
    return f'http://www.codewars.com/users/{quote(user)}'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ('g964', 'http://www.codewars.com/users/g964'),
        ('matt c', 'http://www.codewars.com/users/matt%20c'),
        ('colbydauph', 'http://www.codewars.com/users/colbydauph'),
        ('GiacomoSorbi', 'http://www.codewars.com/users/GiacomoSorbi'),
        ('ZozoFouchtra', 'http://www.codewars.com/users/ZozoFouchtra'),
    )
    for key, val in data:
        assert generate_link(key) == val


if __name__ == '__main__':
    test()
