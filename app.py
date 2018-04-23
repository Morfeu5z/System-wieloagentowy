from flask import Flask, render_template

app = Flask(__name__)

class questionList:
    def __init__(self, q, a, b, c, d):
        self.question = q
        self.ans1 = a
        self.ans2 = b
        self.ans3 = c
        self.id = d

qlist = [
    questionList(q="Jakiej wagi sprzęt?", a="Bardzo lekki", b="Do 3kg", c="Obojętnie", d="1"),
    questionList(q="Orientacja cenowa?", a="Tani", b="Średniak", c="Mam hajsy", d="2"),
    questionList(q="Przeznaczenie?", a="Przeglądarka i dokumenty", b="Uniwersalny", c="PC Gaming Master Race", d="3"),
    questionList(q="Żywotność baterii?", a="Stawiam na długi czas pracy", b="Fajnie jakby na bateri wytrzymał co najmniej jeden film", c="Obojętnie", d="4"),
    questionList(q="Głośność pracy?", a="Cichy jak ninja", b="Niech mruczy aż miło", c="Obojętnie", d="5")
]

for quest in qlist:
    print("Pytanie: {0} \n Odp 1: {1} \n Odp 2: {2} \n Odp 3: {3}".format(quest.question, quest.ans1, quest.ans2, quest.ans3))

@app.route('/')
def index():

    return render_template('index.html', qList=qlist)

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
