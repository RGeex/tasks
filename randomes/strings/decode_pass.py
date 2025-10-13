"""
Проверка пароля — преобразование двоичного кода в строку

Состоятельный клиент забыл пароль к своему бизнес-сайту, но у него есть список возможных паролей.
Его предыдущий разработчик оставил на сервере файл с именем password.txt. Вы открываете файл и обнаруживаете, что он в двоичном формате.

Напишите скрипт, который принимает массив возможных паролей и строку двоичного кода, представляющую возможный пароль.
Преобразуйте двоичный код в строку и сравните его с массивом паролей. Если пароль найден, верните строку пароля, иначе верните false.

decode_pass(['password123', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011');    => 'password123'
decode_pass(['password321', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011');    => False
decode_pass(['password456', 'pass1', 'test12'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011');    => False


"""
import typing
import unittest


def decode_pass(pass_list: list[str], bits: str) -> str | bool:
    """
    Поиск пароля.
    """
    return (x := ''.join(chr(int(x, 2)) for x in bits.split())) in pass_list and x


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(*key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(decode_pass, (
        ((['password123', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'), 'password123'),
        ((['password321', 'admin', 'admin1'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'), False),
        ((['password456', 'pass1', 'test12'], '01110000 01100001 01110011 01110011 01110111 01101111 01110010 01100100 00110001 00110010 00110011'), False),
    ))
