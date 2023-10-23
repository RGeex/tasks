"""
Напишите функцию deNico/ de_nico()который принимает два параметра:

    key/ $key- строка состоит из уникальных букв и цифр
    message/ $message- строка с закодированным сообщением

и декодирует messageиспользуя key.

Сначала создайте цифровой ключ на основе предоставленного keyназначая каждой
букве позицию, в которой она находится после установки букв из keyв алфавитном
порядке.

Например, для ключа crazyмы получим 23154из-за acryz(сортировка букв по ключу).
Давайте расшифровать cseerntiofarmit on  используя наш crazyключ.

1 2 3 4 5
---------
c s e e r
n t i o f
a r m i t
  o n

После использования ключа:

2 3 1 5 4
---------
s e c r e
t i n f o
r m a t i
o n

Примечания

    The messageникогда не бывает короче, чем key.
    Не забудьте удалить конечные пробелы после расшифровки сообщения.

Примеры

deNico("crazy", "cseerntiofarmit on  ") => "secretinformation"
deNico("abc", "abcd") => "abcd"
deNico("ba", "2143658709") => "1234567890"
deNico("key", "eky") => "key"

Проверьте тестовые примеры для получения дополнительных примеров.
"""


def de_nico(key: str, msg: str) -> str:
    """
    Дешировка сообщений по заданному ключу.
    """
    ln = len(key)
    tmp = [x[0] for x in sorted(enumerate(sorted(key), 1), key=lambda x: key.index(x[1]))]
    tmp = [sorted(enumerate(msg[ln*i:ln*i+ln], 1), key=lambda x: tmp.index(x[0])) for i in range(len(msg)//ln+1)]
    return ''.join([s[1] for x in tmp for s in x]).rstrip()


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("crazy", "cseerntiofarmit on  "), "secretinformation"),
        (("crazy", "cseerntiofarmit on"), "secretinformation"),
        (("abc", "abcd"), "abcd"),
        (("ba", "2143658709"), "1234567890"),
        (("a", "message"), "message"),
        (("key", "eky"), "key"),
    )
    for key, val in data:
        assert de_nico(*key) == val


if __name__ == '__main__':
    test()
