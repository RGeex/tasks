"""
Вам предоставляется строка из файла субтитров фильма в виде строки.
Строка состоит из интервала времени, когда отображается текст:

start(hh:mm:ss,ms) --> stop(hh:mm:ss,ms)

и сам текст, например:

01:09:02,684 --> 01:09:03,601 Run Forrest, run!

Ваша задача написать функцию subs_offset_apply который принимает такую
​строку и смещение
(целое число) в миллисекундах в качестве аргументов и возвращает строку
с примененным смещением.
Примеры:

string = "01:09:02,684 --> 01:09:03,601 Run Forrest, run!"  
subs_offset_apply(string, 3663655)
output: "02:10:06,339 --> 02:10:07,256 Run Forrest, run!"

"00:43:22,074 --> 00:43:24,159 No, I am your father."
subs_offset_apply(string, 1789)   
output: "00:43:23,863 --> 00:43:25,948 No, I am your father." 

"00:03:06,241 --> 00:03:07,618 I'll be back."
subs_offset_apply(string, -21789) 
output: "00:02:44,452 --> 00:02:45,829 I'll be back."

Ограничения по времени:

00:00:00,000 <= t <= 99:59:59,999

В случае слишком большого отрицательного или положительного смещения, что
приводит к превышению ограничений,
функция должна вернуть строку «Недопустимое смещение».
Вам будут предоставлены только действительные строки.
Веселиться!
"""


from datetime import timedelta


def subs_offset_apply(st: str, offset: int) -> str:
    """
    Изменяет время субтитров на указанное смещение, если это возможно или сообщает об ощибке.
    """
    res = []
    for x in st[:29].split(' --> '):
        c = dict(zip('hours minutes seconds'.split(), map(float, x.replace(',', '.').split(':'))))
        t = (timedelta(**c) + timedelta(milliseconds=offset)).total_seconds()
        res.append(f'{t // 3600:0>2.0f}:{t // 60 % 60:0>2.0f}:{t % 60:0>6.3f}'.replace('.', ','))
    return ['Invalid offset', ' --> '.join(res) + st[29:]][res[0][0] != '-' and all(len(res[i].split(':', 1)[0]) < 3 for i in range(2))]


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("01:09:02,684 --> 01:09:03,601 Run Forrest, run!", 3663655), "02:10:06,339 --> 02:10:07,256 Run Forrest, run!"),
        (("00:43:22,074 --> 00:43:24,159 No, I am your father.", 1789), "00:43:23,863 --> 00:43:25,948 No, I am your father."),
        (("00:03:06,241 --> 00:03:07,618 I'll be back.", -21789), "00:02:44,452 --> 00:02:45,829 I'll be back."),
        (("00:03:14,917 --> 00:03:16,001 My name is Bond. James Bond.", -195000), "Invalid offset"),
        (("01:00:00,000 --> 01:00:02,000 Let`s start with this.", -3600000), "00:00:00,000 --> 00:00:02,000 Let`s start with this."),
        (("01:00:00,000 --> 01:00:02,000 Let`s finish this.", 356397999), "99:59:57,999 --> 99:59:59,999 Let`s finish this."),
    )
    for key, val in data:
        assert subs_offset_apply(*key) == val


if __name__ == '__main__':
    test()
