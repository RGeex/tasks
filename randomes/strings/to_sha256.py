"""
Создайте функцию, которая преобразует заданную строку ASCII в ее
шестнадцатеричный хэш SHA-256.

sha256("Hello World!") =>
"7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069"

"""


from hashlib import sha256


def to_sha256(s: str) -> str:
    """
    Конвертирует ascii в sha256
    """
    return sha256(s.encode()).hexdigest()


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("Hello World!", "7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069"),
        ("Codewars", "aeb7c211fae7fff7546d87886a7d3ace8e9ebc30bb36062dfec7c92c78a3e1db"),
    )
    for key, val in data:
        assert to_sha256(key) == val


if __name__ == '__main__':
    test()
