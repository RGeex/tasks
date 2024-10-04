"""
Цель этого Kata — написать функцию, которая будет получать массив строк в
качестве единственного аргумента, затем каждая строка обрабатывается и
сортируется (в порядке убывания) на основе длины одной самой длинной
подстроки из смежных гласных ( aeiouAEIOU ), который может содержаться
в строке. Строки могут содержать буквы, цифры, специальные символы,
прописные и строчные буквы, пробелы, а также могут быть (часто будут)
несколько подстрок из смежных гласных. Нас интересует только одна самая
длинная подстрока гласных внутри каждой строки во входном массиве.

Пример:

str1 = "what a beautiful day today"
str2 = "it's okay, but very breezy"

Когда строки отсортированы, str1 будет первым, так как его самая длинная
подстрока из смежных гласных "eau" имеет длину 3, пока str2 имеет самую
длинную подстроку из смежных гласных "ee", длина которого 2.

Если две или более строк в массиве имеют максимальное количество подстрок
одинаковой длины, то строки должны оставаться в том порядке, в котором они
были найдены в исходном массиве.
"""


import re


def sort_strings_by_vowels(seq: list[str]) -> list[str]:
    """
    Сортирует список строк по кол-ву смежных гласных в порядке убывания.
    """ 
    return sorted(seq, key=lambda x: max(map(len, re.split(r'[^aeiouAEIOU]', x))), reverse=True)


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (["aa","eee","oo","iiii"], ["iiii","eee","aa","oo"]),
        (["a","e","ii","ooo","u"] ,["ooo","ii","a","e","u"]),
        (["ioue","ee","uoiea"], ["uoiea", "ioue","ee"]),
        (["high","day","boot"], ["boot","high","day"]),
        (["none","uuu","Yuuuge!!"], ["uuu","Yuuuge!!","none"])                                  ,
        (["AIBRH","","YOUNG","GREEEN"], ["GREEEN","AIBRH","YOUNG",""]),
        (["jyn","joan","jimmy","joey"], ["joan","joey","jimmy","jyn"]),
        (["uijijeoj","lkjlkjww2","iiutrqy"], ["iiutrqy","uijijeoj","lkjlkjww2"]),
        (["how about now","a beautiful trio of"], ["a beautiful trio of","how about now"]),
        (["every","bataux","is","waaaay","loose"], ["waaaay","bataux","loose","every","is"]),
    )
    for key, val in data:
        assert sort_strings_by_vowels(key) == val


if __name__ == '__main__':
    test()
