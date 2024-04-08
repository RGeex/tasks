"""
Напишите функцию, которая при задании URL-адреса в виде строки анализирует
только имя домена и возвращает его в виде строки. Например:

* url = "http://github.com/carbonfive/raygun" -> domain name = "github"
* url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
* url = "https://www.cnet.com"                -> domain name = cnet"

"""


def domain_name(url: str):
    """
    Получение доменного иени из строки URL.
    """
    return max(url.split('//')[-1].split('.', 2)[:2], key=lambda x: ('/' not in x, len(x)))


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        ("http://google.com", "google"),
        ("http://google.co.jp", "google"),
        ("https://123.net", "123"),
        ("https://hyphen-site.org", "hyphen-site"),
        ("http://codewars.com", "codewars"),
        ("www.xakep.ru", "xakep"),
        ("https://youtube.com", "youtube"),
        ("http://www.codewars.com/kata/", "codewars"),
        ("icann.org", "icann"),
        ("https://5fftl.info/index.php", "5fftl"),
    )
    for key, val in data:
        assert domain_name(key) == val


if __name__ == '__main__':
    test()
