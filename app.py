from flask import Flask, render_template, jsonify, request, redirect
from static.source import question
from flask_sqlalchemy import SQLAlchemy
from getData import data
from randomGenerator import rG

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://morfeu5z:KarmazynowaBroda69>@trashpanda.pwsz.nysa.pl/sklep_agentowy_1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.register_blueprint(data)


class Items(db.Model):
    '''
    * Model dla tabeli items
    '''
    __tablename__ = 'items'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(250))
    type = db.Column('type', db.String(50))
    weight = db.Column('weight', db.Float)
    cpu = db.Column('cpu', db.Integer)
    gpu = db.Column('gpu', db.Integer)
    battery = db.Column('battery', db.Integer)
    dec = db.Column('dec', db.Integer)
    price = db.Column('price', db.Float)
    procesor = db.Column('procesor', db.String(50))
    grafika = db.Column('grafika', db.String(50))

    def __init__(self, name, type, weight, cpu, gpu, battery, dec, price, procesor, grafika):
        self.name = name
        self.type = type
        self.weight = weight
        self.cpu = cpu
        self.gpu = gpu
        self.battery = battery
        self.dec = dec
        self.price = price
        self.procesor = procesor
        self.grafika = grafika


def renderRecords(howMany):
    '''
    * Tworzenie losowych wartosci do bazy danych
    :param howMany:
    :return:
    '''
    for i in range(1, int(howMany)):
        print('Rendering: {0} records'.format(howMany))
        data = rG()
        print("Rand: {0} {1} {2}kg {3}CPU {4}GPU {5}h {6}dB {7}PLN {8} {9}".format(data[0], data[1], data[2], data[3],
                                                                                   data[4], data[5], data[6], data[7],
                                                                                   data[8], data[9]))
        db.session.add(Items(data[1], data[0], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
    db.session.commit()


def connect_test():
    '''
    * sprawdza czy w bazie sa jakies wartosci
    :return:
    '''
    item = Items.query.first()
    if item:
        print("Nawiązano połączenie z bazą.")

    else:
        print("Baza jest pusta. Rozpoczynam generację testowych danych.")
        renderRecords(10)


''' 
    * Tworzenie listy pytań 
'''
qlist = question.questionList.makeQuestion(question.questionList)


def showList():
    '''
    * Wyświetlenie w terminalu listy pytań
    '''
    for quest in qlist:
        print("Pytanie: {0} \n Odp 1: {1} \n Odp 2: {2} \n Odp 3: {3}".format(quest.question, quest.ans1, quest.ans2,
                                                                              quest.ans3))


@app.route('/renderRecords/<howMany>')
def letsGo(howMany):
    '''
    * Wywoanie generatora losowych danych
    :param howMany:
    :return:
    '''
    print('Render: {0}'.format(howMany))
    renderRecords(howMany)
    return redirect('/')


@app.route('/')
def index():
    '''
    * Renderowanie strony głównej
    '''
    print('Start web.')
    connect_test()
    return render_template('index.html', qList=qlist)


'''
    * Start apki
'''
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)
