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

    print('Przetworzono: ' + butt[0] + ' - ' + prio[0] + ' - ' + pric)

    # Przetworzenie 0-1 do default'owych true-false
    if butt[0] == '0':
        butt[0] = 'false'
        butt[1] = 'false'
        butt[2] = 'true'
    if butt[3] == '0':
        butt[3] = 'false'
        butt[4] = 'true'
        butt[5] = 'false'
    if butt[6] == '0':
        butt[6] = 'false'
        butt[7] = 'false'
        butt[8] = 'true'
    if butt[9] == '0':
        butt[9] = 'false'
        butt[10] = 'false'
        butt[11] = 'true'

    # 1. weight = [min, max, priorytet]
    # lekki [0, 1.5], do 3 [1.5, 3], obojetnie [0, 100]
    if butt[0] == 'true':
        weight = [0, 1.5, prio[0]]
    if butt[1] == 'true':
        weight = [1.5, 3, prio[0]]
    if butt[2] == 'true':
        weight = [0, 100, prio[0]]

    # 2. use = [min CPU Benchmark, max CPU Benchmark, min GPU Benchmark, max GPU Benchmark, priorytet]
    # CPU kiepski [0, 3000], uniwersalny [3000, 7000], predator[5000, 100000]
    # GPU kiepski [0, 3000], uniwersalny [3000, 6000], predator[5000, 100000]
    if butt[3] == 'true':
        use = [0, 3000, 0, 3000, prio[1]]
    if butt[4] == 'true':
        use = [3000, 7000, 3000, 6000, prio[1]]
    if butt[5] == 'true':
        use = [5000, 100000, 5000, 100000, prio[1]]

    # 3. battery = [min, priorytet]
    # jeden film [2], duża [4], obojętnie [0]
    if butt[6] =='true':
        battery = [4, prio[2]]
    if butt[7] =='true':
        battery = [2, prio[2]]
    if butt[8] =='true':
        battery = [0, prio[2]]

    # 4. dB = [max, priorytet]
    # ninja [30], wariat [100], obojętnie [100]
    if butt[9] =='true':
        dB = [30, prio[3]]
    if butt[10] =='true':
        dB = [100, prio[3]]
    if butt[11] =='true':
        dB = [100, prio[3]]

    # 5. price = [min, max, priorytet]
    # [price-15%, price+15%]
    pric = float(pric)
    price = [pric - (15/100)*pric, pric + (15/100)*pric, prio[4]]

    print(weight)
    print(use)
    print(battery)
    print(dB)
    print(price)

    return jsonify({'response' : 'Przetwarzanie danych.'})

'''Start apki'''
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
