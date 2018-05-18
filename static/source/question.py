'''Klasa dla pytań'''
class questionList:
    def __init__(self, q, a, b, c, d):
        self.question = q
        self.ans1 = a
        self.ans2 = b
        self.ans3 = c
        self.id = d

    '''Lista pytań przesłana do strony głównej'''
    def makeQuestion(self):
        qlist = [
            questionList(q="Jakiej wagi sprzęt?", a="Bardzo lekki", b="Do 3kg", c="Obojętnie", d="1"),
            questionList(q="Przeznaczenie?", a="Przeglądarka i dokumenty", b="Uniwersalny", c="PC Gaming Master Race", d="2"),
            questionList(q="Żywotność baterii?", a="Stawiam na długi czas pracy", b="Fajnie jakby na bateri wytrzymał co najmniej jeden film", c="Obojętnie", d="3"),
            questionList(q="Głośność pracy?", a="Cichy jak ninja", b="Niech mruczy aż miło", c="Obojętnie", d="4")
        ]
        return qlist