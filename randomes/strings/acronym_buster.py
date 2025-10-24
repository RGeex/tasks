"""
Лаура очень ненавидит людей, использующих аббревиатуры в ее офисе, и хочет
заставить своих коллег удалить все аббревиатуры, прежде чем писать ей по
электронной почте. Она хочет, чтобы вы создали систему, которая будет
удалять все известные сокращения или уведомлять отправителя о наличии
неизвестных сокращений.

Любая комбинация трех и более букв в верхнем регистре будет считаться
аббревиатурой. Акронимы не будут сочетаться со строчными буквами, как,
например, в случае с «КПЭ». Они будут изолированы как слово/слова внутри
строки.

Для любой строки:
Все экземпляры «KPI» должны стать «key performance indicators».
Все случаи «EOD» должны стать «the end of the day».
Все случаи «TBD» должны стать «to be decided».
Все случаи «WAH» должны стать «work at home».
Все экземпляры IAM должны стать «in a meeting».
Все инстанции «ООО» должны стать «out of office»
Все экземпляры «NRN» должны стать «no reply necessary».
Все примеры призыва к действию должны стать «call to action».
Все случаи SWOT должны стать «strengths, weaknesses, opportunities and threats».

Если в строке есть неизвестные сокращения, Лаура хочет, чтобы вы вернули
только сообщение:
'[acronym] is an acronym. I do not like acronyms. Please remove them from your email.».

Итак, если бы рассматриваемая аббревиатура была «BRB», вы бы вернули строку:
«BRB is an acronym. I do not like acronyms. Please remove them from your email.».

Если в строке содержится более одной неизвестной аббревиатуры, верните только
первую. в ответ

Однако, если все сокращения можно заменить полными словами в соответствии с
вышеизложенным, верните только измененную строку.

В этом случае убедитесь, что предложения по-прежнему начинаются с заглавных букв.
'!' или '?' не будет использоваться.
"""
import typing
import unittest
import re


acr = {
    'KPI': 'key performance indicators',
    'EOD': 'the end of the day',
    'TBD': 'to be decided',
    'WAH': 'work at home',
    'IAM': 'in a meeting',
    'OOO': 'out of office',
    'NRN': 'no reply necessary',
    'CTA': 'call to action',
    'SWOT': 'strengths, weaknesses, opportunities and threats',
}


def acronym_buster(s: str) -> str:
    """
    Осуществляет поиск и замену известных акронимов.
    Задает каждое новое предлоежние с заглавной буквы.

    Если найден неизвестный акроним возвращает строку с сообщением об этом.
    """
    if x := next((x for x in re.findall(r'\b[A-Z]{3,}\b', s) if x not in acr), 0):
        return f'{x} is an acronym. I do not like acronyms. Please remove them from your email.'
    return re.sub(r'([.!?]\s|^)([a-z])', lambda x: x.group(1) + x.group(2).upper(), re.sub(r'\b[A-Z]{3,}\b', lambda x: acr[x.group()], s))


def test(func: typing.Callable, data: tuple[tuple[typing.Any, typing.Any]]) -> None:
    """Тестирование работы алгоритмов с помощью unittest."""

    def test_func(func: typing.Callable, key: typing.Any, val: typing.Any) -> typing.Callable:
        """Создает кейсы для тестирования."""
        return lambda self: self.assertEqual(func(key), val)

    funcs = {f'test_{i}': test_func(func, key, val) for i, (key, val) in enumerate(data, 1)}
    suite = unittest.TestLoader().loadTestsFromTestCase(type('Tests', (unittest.TestCase,), funcs))

    unittest.TextTestRunner().run(suite)


if __name__ == '__main__':
    test(acronym_buster, (
        ("BRB I need to go into a KPI meeting before EOD",
        "BRB is an acronym. I do not like acronyms. Please remove them from your email."),
        ("I am IAM so will be OOO until EOD",
        "I am in a meeting so will be out of office until the end of the day"),
        ("Going to WAH today. NRN. OOO",
        "Going to work at home today. No reply necessary. Out of office"),
        ("We're looking at SMB on SM DMs today",
        "SMB is an acronym. I do not like acronyms. Please remove them from your email."),
        ("OOO",
        "Out of office"),
        ("KPI",
        "Key performance indicators"),
        ("EOD",
        "The end of the day"),
        ("TBD",
        "To be decided"),
        ("TBD by EOD",
        "To be decided by the end of the day"),
        ("BRB I am OOO",
        "BRB is an acronym. I do not like acronyms. Please remove them from your email."),
        ("WAH",
        "Work at home"),
        ("IAM",
        "In a meeting"),
        ("NRN",
        "No reply necessary"),
        ("CTA",
        "Call to action"),
        ("Hi PAB",
        "PAB is an acronym. I do not like acronyms. Please remove them from your email."),
        ("HATDBEA",
        "HATDBEA is an acronym. I do not like acronyms. Please remove them from your email."),
        ("LDS",
        "LDS is an acronym. I do not like acronyms. Please remove them from your email."),
        ("PB",
        "PB"),
        ("FA",
        "FA"),
        ("CTA and HTTP",
        "HTTP is an acronym. I do not like acronyms. Please remove them from your email."),
        ("SWOT.",
        "Strengths, weaknesses, opportunities and threats."),
        ("HTTP",
        "HTTP is an acronym. I do not like acronyms. Please remove them from your email."),
        ("Please WAH today. KPI on track",
        "Please work at home today. Key performance indicators on track"),
        ("The advert needs a CTA. NRN before EOD.",
        "The advert needs a call to action. No reply necessary before the end of the day."),
        ("I sent you a RFP yesterday.",
        "RFP is an acronym. I do not like acronyms. Please remove them from your email."),
        ("My SM account needs some work.",
        "My SM account needs some work."),
    ))
