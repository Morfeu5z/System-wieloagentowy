import multiprocessing
import random
import threading
import time
from multiprocessing import Pool
from shop import realy_shop, printme

from flask import Blueprint, request, jsonify

from static.source.blueprint.fake_shop import Faker_Shop
from static.source.blueprint.rmChar import rmChar
from static.source.blueprint.class_agent import AgentC

data = Blueprint('gatData', __name__, template_folder='templates')


def testMulti(num):
    print('Proces: {}'.format(num))


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

    # print('Przechwycono: ' + butt)
    # print('Przechwycono: ' + prio)
    # print('Przechwycono: ' + pric)

    butt = rmChar(butt, ['[', ']'])
    butt = butt.split(',')

    prio = rmChar(prio, ['[', ']', '\"'])
    prio = prio.split(',')

    # print('Przetworzono: ' + butt[0] + ' - ' + prio[0] + ' - ' + pric)

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
    # lekki [0, 1.5], do 3 [0, 3], obojetnie [0, 100]
    if butt[0] == 'true':
        weight = [0, 1.5, prio[0]]
    if butt[1] == 'true':
        weight = [0, 3, prio[0]]
    if butt[2] == 'true':
        weight = [0, 100, prio[0]]

    # 2. use = [min CPU Benchmark, max CPU Benchmark, min GPU Benchmark, max GPU Benchmark, priorytet]
    # CPU kiepski [0, 3000], uniwersalny [3000, 7000], predator[5000, 100000]
    # GPU kiepski [0, 3000], uniwersalny [3000, 6000], predator[5000, 100000]
    if butt[3] == 'true':
        used = 'office'
        use = [0, 3000, 0, 3000, prio[1]]
    if butt[4] == 'true':
        used = 'universal'
        use = [3000, 7000, 3000, 6000, prio[1]]
    if butt[5] == 'true':
        used = 'game'
        use = [5000, 100000, 5000, 100000, prio[1]]

    # 3. battery = [min, priorytet]
    # jeden film [2], duża [5], obojętnie [0]
    if butt[6] == 'true':
        battery = [4, prio[2]]
    if butt[7] == 'true':
        battery = [2, prio[2]]
    if butt[8] == 'true':
        battery = [0, prio[2]]

    # 4. dB = [max, priorytet]
    # ninja [20], wariat [100], obojętnie [100]
    if butt[9] == 'true':
        dB = [15, prio[3]]
    if butt[10] == 'true':
        dB = [100, prio[3]]
    if butt[11] == 'true':
        dB = [100, prio[3]]

    # 5. price = [min, max]
    # [price-15%, price+15%]
    pric = float(pric)
    price = [pric - (15 / 100) * pric, pric + (15 / 100) * pric]

    # print(weight)
    # print(use)
    # print(battery)
    # print(dB)
    # print(price)

    dane = {
        'weight': str(weight),
        'use': str(use),
        'battery': str(battery),
        'dB': str(dB),
        'price': str(price),
        'used': str(used)
    }

    deviceTable = []

    print('Uruchomienie sklepikarza')
    faker = []
    fakerCount = 1
    for x in range(0, fakerCount):
        faker.append(Faker_Shop(x))
    fake = 0

    print('Uruchomienie agenta')
    agents = []
    agentsCount = 25
    for x in range(0, agentsCount):
        agents.append(AgentC(dane, faker[random.randint(0, fakerCount - 1)], used, x))

    # Eliminacja powtórzeń
    # Wybranie lepszej ceny
    canBe = 1
    time0 = time.time()

    tmp = ''
    xyz = []
    # Wielowątkowe wypuszczenie agentów
    # Uzupełniają listę parametrami
    # lub empty jeśli nic agent nie znajdzie
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    p = Pool(processes=4)
    for x in range(0, agentsCount):
        run = p.map_async(agents[x].run(return_dict, x), range(4))
        xyz.append(return_dict.values())
    p.close()

    # Eliminacja powtórzeń
    for elem in xyz:
        tmp = elem[0].split('|')
        print('=== {} ==='.format(tmp))
        if tmp[0] != 'empty':
            num = -1
            for y in deviceTable:
                num += 1
                if y[1] == tmp[1]:
                    print('? {} == {} ?'.format(y[1], tmp[1]))
                    if y[9] > tmp[9]:
                        # print('? {} > {} ?'.format(y[9], tmp[9]))
                        deviceTable[num] = tmp
                    canBe = 0
                else:
                    canBe = 1
            if canBe == 1:
                deviceTable.append(tmp)
    print(time.time() - time0)
    return jsonify({'response': deviceTable})
