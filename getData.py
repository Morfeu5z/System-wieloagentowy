import socket

from flask import Blueprint, request, jsonify

data = Blueprint('gatData', __name__, template_folder='templates')

def fakerSklep(message):
    print('-----FAKER_SKLEPIKARZ-----')

    print('-----------END------------')
    return b'Oto moje towary'

def sendAgent(w, u, b, d, p):
    '''
    * Agent
    :param w:
    :param u:
    :param b:
    :param d:
    :param p:
    :return:
    '''
    print('Agant in action')
    ''' host and port connetction '''
    target_host = "0.0.0.0"
    target_port = 9999

    ''' towżymy objekt socket-u z typem translacji AF_INET
        co znaczy, że ten dzila dla ipv4 adressow. 
        SOCK_STREAM - typ używny dla TCP protokolów
    '''
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))

    '''ID:Nr_Spotkania:Wiadomosc'''

    message = str(w) + '|' + str(u) + '|' + str(b) + '|' + str(d) + '|' + str(p)
    print('Message: {}'.format(message))
    # client.send(message.encode("unicode-escape"))

    '''
      naprawde tu dziala pętla w odrębnym wątku która czeka na 
      dane od servera.
    '''
    # reponse = client.recv(4096)

    respo = fakerSklep(message)
    respo = respo.decode("unicode-escape")
    print("Odpowiedz sprzedawcy: ", respo)
    return respo



@data.route('/getData', methods=['POST'])
def getData():
    '''
    * Odbiera dane za pomocą ajax'a
    * Przetwarza odebrane dane na listy
    * Ustala parametry dla agentów
    :return: ajax response
    '''
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
    # jeden film [2], duża [5], obojętnie [0]
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

    # 5. price = [min, max]
    # [price-15%, price+15%]
    pric = float(pric)
    price = [pric - (15/100)*pric, pric + (15/100)*pric]

    print(weight)
    print(use)
    print(battery)
    print(dB)
    print(price)

    propozycja = sendAgent(weight, use, battery,dB, price)

    return jsonify({'response' : propozycja})