"""
Фон

Каждый раз, когда вы что-то фотокопируете, качество копии никогда не будет
таким же хорошим, как оригинал.
Но потом вы делаете копию копии, а затем копию этой копии и так далее...
И с каждым разом результаты становятся все хуже.
Этот вид деградации называется потерей поколения .
Вот забавный пример копирования кассет VHS с потерями.
Словесное задание

В этой Ката вам дадут 2 листа бумаги.
Первый — оригинал, а второй — результат многократного копирования. Назовем эти бумаги origи copy.
При каждой копии происходит лишь небольшой процент потерь генерации, но эффект накопительный,
и копии быстро становятся похожими на тарабарщину.

Ваша задача — вернуть true/false, если origявляется возможным предком copy.
Примечания

    The origдокумент может содержать любые символы
    Скопированные символы будут ухудшаться следующим образом: A- Z ⇒ a- z ⇒ # ⇒ + ⇒ : ⇒ . ⇒
    Любой другой символ, не упомянутый выше (например, цифры), не ухудшается.
    Для перехода от верхнего регистра к нижнему регистру буквы должны быть одинаковыми
    (т.е. A ⇒ a ... Z ⇒ z)

"""


def generation_loss(orig: str, copy: str) -> bool:
    """
    Проверяет, может ли являться "замыленная" копия оригиналом.
    """
    if len(orig) == len(copy):
        for a, b in zip(orig, copy):
            temp = dict(zip(a.lower() + '#+:. ', range(2, 8)))
            if not (a == b or (a.isalpha() or a in '#+:.') and temp.get(a, 0) < temp.get(b, 0)):
                break
        else:
            return True
    return False


def test() -> None:
    """
    Тестирование работы алгоритмов.
    """
    data = (
        (("""\
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.""",
          """\
        TH# Q+#Ck BRow# F+x J#MPS over A Laz# #+# 
        :He Qui#k #rO#n foX Ju#Ps oVer a la+y Do+ 
        THe QUiC# b:OWn #oX ##m#s #Ver + lAZ# D#G 
        ##E #uIcK BROWn Fox #UMPS o#Er A LaZY doG.
        #H+ Qui## BROW# +ox jUMPs OV#r a lAzy ###.
        ##e +UICK #ROWn fo# +#mPs #Ve+ a lazY dOg 
        ### ##IC+ Br### f#x Jump# oVE+ A La## dOg.
        th+ qUI#k bRO#n fOX #umP# o#ER A La+Y #O. 
        tH# #U:#k +r+## F+# +#mP+ #VeR A ###Y DOg.
        #H# QUIcK #ROwN #o+ juM#s #V#+ A #aZy dog """
          ), True),
        (("""\
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX JUMPS OVER A LAZY DOG.""",
          """\
        THE QUICK BROWN FOX xUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX xUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX xUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX xUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX xUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX xUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX xUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX xUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX xUMPS OVER A LAZY DOG.
        THE QUICK BROWN FOX xUMPS OVER A LAZY DOG."""
          ), False),
    )
    for key, val in data:
        assert generation_loss(*key) == val


if __name__ == '__main__':
    test()
