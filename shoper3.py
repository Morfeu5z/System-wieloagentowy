from flask import Flask, request, jsonify

from static.source.blueprint.fake_shop import Faker_Shop
from static.source.model import session
from static.source.model.Items import Items

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Welcome to my Shop!'

def connect_test():
    '''
    * sprawdza czy w bazie sa jakies wartosci
    :return:
    '''
    item = session.query(Items).first()
    if item:
        print("Nawiązano połączenie z bazą.")

    else:
        print("Baza jest pusta. Rozpoczynam generację testowych danych.")

@app.route('/conversation', methods=['POST'])
def ShopMessage():
    respo = request.get_json(force=True)
    # connect_test()
    respo = respo['message']
    print('=== Got massage: {} ==='.format(respo))
    message = respo.split('|')
    shoper = Faker_Shop(message, str(message[1]), 1)
    backMessage = shoper.run()
    if not backMessage:
        backMessage = 'none'
    print('=== Resend: {} ==='.format(backMessage))
    print()
    print('============')
    print('===Shop 3===')
    print('============')
    print()
    return jsonify({'message': backMessage})


'''
    * Start apki
'''
if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=4003)
