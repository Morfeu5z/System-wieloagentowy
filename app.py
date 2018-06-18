from flask import Flask, render_template, redirect
from static.source.blueprint import question
from static.source.model.Items import Items
from static.source.model.Memory import Memory
from static.source.model import session

from static.source.blueprint.getData import data
from static.source.blueprint.randomGenerator import rG

app = Flask(__name__)

app.register_blueprint(data)


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
        session.add(Items(data[1], data[0], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9]))
    session.commit()


def memoTester():
    item = session.query(Memory).first()
    original = item.type
    print('Test memory 1/4: {} |Original|'.format(item.type))
    item.type = 'none'
    print('Test memory 2/4: {} |Change|'.format(item.type))
    session.add(item)
    session.commit()
    item = session.query(Memory).first()
    print('Test memory 3/4: {} |Updated|'.format(item.type))
    item.type = original
    session.add(item)
    session.commit()


@app.route('/testMemory')
def testMemory():
    item = session.query(Memory).first()
    if not item:
        print('Empty memory: id=1, type=game, sold=0 |Create|')
        session.add(Memory(1, 'game', 0))
        session.commit()
        memoTester()
        item = session.query(Memory).first()
        session.delete(item)
        session.commit()
        print('Test memory 4/4 |Callback|')
    else:
        memoTester()
        print('Test memory 4/4 |Callback|')
    return redirect('/')


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
