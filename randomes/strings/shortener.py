"""
SMS-сообщения ограничены 160 символами. Это может раздражать, особенно когда
длина только что написанного сообщения составляет 164 символа.

Ваша задача — сократить сообщение до 160 символов, начиная с конца, заменяя
пробелы на верблюжий регистр, насколько это необходимо.

Если все пробелы заменены, но длина полученного сообщения по-прежнему
превышает 160 символов, просто верните это полученное сообщение.

Пример 1:

Исходное сообщение (169 символов):

No one expects the Spanish Inquisition! Our chief weapon is surprise, fear
and surprise; two chief weapons, fear, surprise, and ruthless efficiency!
And that will be it.
 

Сокращенное сообщение (160 символов):

No one expects the Spanish Inquisition! Our chief weapon is surprise, fear
and surprise; two chief weapons, fear,Surprise,AndRuthlessEfficiency!AndThatWillBeIt.
 

Пример 2:

Исходное сообщение (269 символов):

SMS messages are limited to 160 characters. It tends to be irritating,
especially when freshly written message is 164 characters long. SMS messages
are limited to 160 characters. It tends to be irritating, especially when freshly
written message is 164 characters long.
 

Сокращенное сообщение (228 символов):

SMSMessagesAreLimitedTo160Characters.ItTendsToBeIrritating,EspeciallyWhenFreshly
WrittenMessageIs164CharactersLong.SMSMessagesAreLimitedTo160Characters.ItTendsTo
BeIrritating,EspeciallyWhenFreshlyWrittenMessageIs164CharactersLong.
"""


import re


def shortener(s: str) -> str:
    """
    Заменяет пробелы на CameCase начиная с конца предложения,
    до лимита предложения в 160 символов.
    """
    return re.sub(r'.\s', lambda x: x.group().upper().strip(), s[::-1], len(s) - 160)[::-1]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (('No one expects the Spanish Inquisition! Our chief weapon is surprise, '
        'fear and surprise; two chief weapons, fear, surprise, and ruthless efficiency! '
        'And that will be it.'),
        ('No one expects the Spanish Inquisition! Our chief weapon is surprise, '
        'fear and surprise; two chief weapons, fear,Surprise,AndRuthlessEfficiency!'
        'AndThatWillBeIt.')),

        (('ThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoon'
        'ThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoon'
        'ThereIsNoSpoonThereIsNoSpoonThereIsNoSpoon'),
        ('ThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoon'
        'ThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoonThereIsNoSpoon'
        'ThereIsNoSpoonThereIsNoSpoonThereIsNoSpoon')),

        (('SMS messages are limited to 160 characters. It tends to be irritating, '
        'especially when freshly written message is 164 characters long. '
        'SMS messages are limited to 160 characters. It tends to be irritating, '
        'especially when freshly written message is 164 characters long.'),
        ('SMSMessagesAreLimitedTo160Characters.ItTendsToBeIrritating,Especially'
        'WhenFreshlyWrittenMessageIs164CharactersLong.SMSMessagesAreLimitedTo160'
        'Characters.ItTendsToBeIrritating,EspeciallyWhenFreshlyWrittenMessageIs'
        '164CharactersLong.')),
    )
    for key, val in data:
        assert shortener(key) == val


if __name__ == '__main__':
    test()
