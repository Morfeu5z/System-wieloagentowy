from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

'''Klasa dla pytań'''
class questionList:
    def __init__(self, q, a, b, c, d):
        self.question = q
        self.ans1 = a
        self.ans2 = b
        self.ans3 = c
        self.id = d

'''Lista pytań przesłana do strony głównej'''
qlist = [
    questionList(q="Jakiej wagi sprzęt?", a="Bardzo lekki", b="Do 3kg", c="Obojętnie", d="1"),
    questionList(q="Przeznaczenie?", a="Przeglądarka i dokumenty", b="Uniwersalny", c="PC Gaming Master Race", d="2"),
    questionList(q="Żywotność baterii?", a="Stawiam na długi czas pracy", b="Fajnie jakby na bateri wytrzymał co najmniej jeden film", c="Obojętnie", d="3"),
    questionList(q="Głośność pracy?", a="Cichy jak ninja", b="Niech mruczy aż miło", c="Obojętnie", d="4")
]

'''Wyświetlenie w terminalu listy pytań'''
def showList():
    for quest in qlist:
        print("Pytanie: {0} \n Odp 1: {1} \n Odp 2: {2} \n Odp 3: {3}".format(quest.question, quest.ans1, quest.ans2, quest.ans3))

'''Render strony głównej'''
@app.route('/')
def index():
    return render_template('index.html', qList=qlist)

'''
* Odbiera dane za pomocą ajax'a
* Przetwarza odebrane dane na listy
* Ustala parametry dla agentów
'''
@app.route('/getData', methods=['POST'])
def getData():
    butt = request.form.get('butt')
    prio = request.form.get('prio')
    pric = request.form.get('pric')

    print('Przechwycono: ' + butt)
    print('Przechwycono: ' + prio)
    print('Przechwycono: ' + pric)

    butt = butt.replace("[", "")
    butt = butt.replace("]", "")
    butt = butt.split(',')

    prio = prio.replace('[', '')
    prio = prio.replace(']', '')
    prio = prio.replace('"', '')
    prio = prio.split(',')

    print('Przetworzono: ' + butt[1] + ' - ' + prio[1] + ' - ' + pric)

    return jsonify({'response' : 'Przetwarzanie danych.'})

'''Start apki'''
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
