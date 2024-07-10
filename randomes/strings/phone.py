"""
Джон хранит резервную копию своей старой личной телефонной книги в виде текстового файла. В каждой строке файла он может найти номер телефона (в формате +X-abc-def-ghijгде X обозначает одну или две цифры), соответствующее имя между < и > и адрес.

К сожалению, все перемешано, не всегда все в одном порядке; части строк
загромождены небуквенно-цифровыми символами (кроме внутреннего номера
телефона и имени).

Примеры строк телефонной книги Джона:

"/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"

" 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"

"<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"

Не могли бы вы помочь Джону с программой, которая, учитывая строки его
телефонной книги и номер телефона num возвращает строку для этого числа:
"Phone => num, Name => name, Address => adress"
Примеры:

s = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur>
NY-56423 ;+1-541-914-3010!\n"

phone(s, "1-541-754-3010") should return "Phone => 1-541-754-3010, Name =>
J Steeve, Address => 156 Alphand St."

    Может случиться так, что на номер телефона придет много людей num, затем
    вернитесь: "Error => Too many people: num"

    или может случиться так, что число numего нет в телефонной книге, в таком
    случае возвращаться: "Error => Not found: num"

Примечания

    Стандартный вывод Codewars не печатает часть строки между < и >

    Другие примеры вы можете увидеть в тестовых примерах.

    Случайные тесты JavaScript, выполненные @matt c.
"""

import re


def phone(strng: str, num: str) -> str:
    """
    Парсит телефонную книгу в виде строки. Ищет строку с заданным номером телефона, собирает все данные
    относящиеся к этой строке, убирает все лишние символы и формирует строку по шаблону с полученными данными.
    """
    res, reg = dict(zip('Phone Name Address'.split(), [''] * 3)), (r'(\d+(?:-\d+)+\b)', r'<(.*)>', r'^(.*)$')
    for s in (n := strng.count(num)) == 1 and re.sub(r'[/:;,+\$\*!?]', '', strng).replace('_', ' ').split('\n') or '':
        if num in s:
            for i, (a, b) in enumerate(zip(res, reg)):
                res[a] = (x:=re.split(b, ' '.join(map(str.strip, x[::2])) if i else s))[1].strip().replace('  ', ' ')
    return ', '.join([f'{a} => {b}' for a, b in res.items() if b]) or f'Error => {["Too many people", "Not found"][not n]}: {num}'


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    dr = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
    "+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209\n"
    "+1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209\n"
    "+1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209\n"
    "<Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222!\n"
    "<Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,\n"
    "<Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209\n"
    "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver\n"
    "<C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado\n"
    "+1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071\n"
    "<P Salinge> Main Street, +1-098-512-2222, Denve\n")

    data = (
        ((dr, "48-421-674-8974"), "Phone => 48-421-674-8974, Name => Anastasia, Address => Via Quirinal Roma"),
        ((dr, "1-921-512-2222"), "Phone => 1-921-512-2222, Name => Wilfrid Stevens, Address => Wild Street AA-67209"),
        ((dr, "1-908-512-2222"), "Phone => 1-908-512-2222, Name => Peter O'Brien, Address => High Street CC-47209"),
        ((dr, "1-541-754-3010"), "Phone => 1-541-754-3010, Name => J Steeve, Address => 156 Alphand St."),
        ((dr, "1-121-504-8974"), "Phone => 1-121-504-8974, Name => Arthur Clarke, Address => San Antonio TT-45120"),
        ((dr, "1-498-512-2222"), "Phone => 1-498-512-2222, Name => Bernard Deltheil, Address => Mount Av. Eldorado"),
        ((dr, "1-098-512-2222"), "Error => Too many people: 1-098-512-2222"),
        ((dr, "5-555-555-5555"), "Error => Not found: 5-555-555-5555"),
    )
    for key, val in data:
        assert phone(*key) == val


if __name__ == '__main__':
    test()
