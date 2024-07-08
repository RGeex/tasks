"""
Завершите метод, чтобы он выполнял следующее:

    Удаляет все повторяющиеся параметры строки запроса из URL-адреса
    (первое вхождение должно быть сохранено).
    Удаляет все параметры строки запроса, указанные во втором аргументе
    (необязательный массив).

Примеры:

strip_url_params('www.codewars.com?a=1&b=2&a=2') == 'www.codewars.com?a=1&b=2'
strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b']) == 'www.codewars.com?a=1'
strip_url_params('www.codewars.com', ['b']) == 'www.codewars.com'
"""


def strip_url_params(s: str, w: list=[]) -> str:
    """
    Убирает из строки url дубликаты аргументов, оставляя первый встречающийся,
    а так же убирает заданные аргументы.
    """
    return '?'.join(['&'.join([f'{a}={b}' for a, b in zip(*[x if i else sorted(set(x), key=x.index) for i, x in enumerate(zip(*[x.split('=') for x in x.split('&')]))]) if a not in w]) if i else x for i, x in enumerate(s.split('?'))]).strip('?')


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    url1 = 'www.codewars.com?a=1&b=2'
    url2 = 'www.codewars.com?a=1&b=2&a=1&b=3'
    url3 = 'www.codewars.com?a=1'
    url4 = 'www.codewars.com'

    data = (
        ((url1,), url1),
        ((url2,), url1),
        ((url2, ['b']), url3),
        ((url4, ['b']), url4),
        ((url1, ['a', 'b']), url4),
    )
    for key, val in data:
        assert strip_url_params(*key) == val


if __name__ == '__main__':
    test()
