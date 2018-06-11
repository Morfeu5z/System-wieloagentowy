import random
import socket
import threading

from static.source.blueprint.fake_shop import Faker_Shop
from static.source.blueprint.rmChar import rmChar


class AgentC():
    def __init__(self, data, faker, device):
        threading.Thread.__init__(self)
        self.dane = data
        self.faker = faker
        self.device = device
        self.oldPrice = 0

    def makeMessage(self, mm):
        '''
        * Budowanie wiadomości
        '''

        if mm != 'none':
            return self.buildMessage(mm)
        else:
            # search|office/universal/game,
            # talk|yes:65/no:65,
            # negotiation|toomuch/ok/nope,
            # show|product_id
            stan = 'search'

            # Dodatkowy parametr dla item_id
            box = 'none'

            # type|type_of_device|item_id
            # search|game|none
            # talk|yes/no|42
            # negotiate|toomuch|42
            # show|42|none
            message = stan + '|' + self.dane['used'] + '|' + box

            print('Start message: {}'.format(self.dane))
            return message

    def buildMessage(self, respo):
        r = respo.split('|')
        if r[0] == 'negotiation':
            humor = random.randint(1,10)
            print('Chce: -{}%'.format(humor))
            chcetyle = self.oldPrice - ((self.oldPrice * humor)/100)
            print('Nowa cena: {} vs {}'.format(r[1], chcetyle))
            if float(r[1]) <= chcetyle:
                return 'negotiation|ok|' + str(r[2])
            else:
                return 'negotiation|toomuch|' + str(r[2])
        else:
            rid = r[1]
            print('Dane r: {}'.format(r))
            option = r[0]
            r = [r[4], r[5], r[6], r[7], r[8], r[9]]
            o = [self.dane['weight'], self.dane['use'], self.dane['battery'], self.dane['dB'], self.dane['price']]
            if option == 'Look':
                print('Interpretacja r: {}'.format(r))
                print('Interpretacja o: {}'.format(o))
                thinking = []
                prio = []
                tmp = self.dane['weight']
                tmp = rmChar(tmp, ['[', ']', '\''])
                tmp = tmp.split(',')
                prio.append(tmp[2])
                if float(r[0]) >= float(tmp[0]) and float(r[0]) <= float(tmp[1]):
                    thinking.append('ok')
                else:
                    thinking.append('nope')

                tmp = self.dane['use']
                tmp = rmChar(tmp, ['[', ']', '\''])
                tmp = tmp.split(',')
                prio.append(tmp[4])
                if float(r[1]) >= float(tmp[0]) and float(r[1]) <= float(tmp[1]):
                    thinking.append('ok')
                else:
                    thinking.append('nope')
                if float(r[2]) >= float(tmp[2]) and float(r[2]) <= float(tmp[3]):
                    thinking.append('ok')
                else:
                    thinking.append('nope')

                tmp = self.dane['battery']
                tmp = rmChar(tmp, ['[', ']', '\''])
                tmp = tmp.split(',')
                prio.append(tmp[1])
                if float(r[3]) >= float(tmp[0]):
                    thinking.append('ok')
                else:
                    thinking.append('nope')

                tmp = self.dane['dB']
                tmp = rmChar(tmp, ['[', ']', '\''])
                tmp = tmp.split(',')
                prio.append(tmp[1])
                if float(r[4]) <= float(tmp[0]):
                    thinking.append('ok')
                else:
                    thinking.append('nope')

                tmp = self.dane['price']
                tmp = rmChar(tmp, ['[', ']', '\''])
                tmp = tmp.split(',')
                prio.append(3)
                if float(r[5]) >= float(tmp[0]) and float(r[5]) <= float(tmp[1]):
                    thinking.append('ok')
                else:
                    thinking.append('nope')
            if thinking[0] == 'nope' and int(prio[0]) < 2:
                thinking[0] = 'ok'
            if thinking[1] == 'nope' and int(prio[1]) < 2:
                thinking[1] = 'ok'
            if thinking[2] == 'nope' and int(prio[1]) < 2:
                thinking[2] = 'ok'
            if thinking[3] == 'nope' and int(prio[2]) < 2:
                thinking[3] = 'ok'
            if thinking[4] == 'nope' and int(prio[3]) < 2:
                thinking[4] = 'ok'
            if thinking[5] == 'nope' and int(prio[4]) < 2:
                thinking[5] = 'ok'
            ok=0
            for x in thinking:
                if x == 'ok':
                    ok += 1
            if ok >= 4:
                if thinking[0] == 'nope' and int(prio[0]) < 3:
                    thinking[0] = 'ok'
                if thinking[1] == 'nope' and int(prio[1]) < 3:
                    thinking[1] = 'ok'
                if thinking[2] == 'nope' and int(prio[1]) < 3:
                    thinking[2] = 'ok'
                if thinking[3] == 'nope' and int(prio[2]) < 3:
                    thinking[3] = 'ok'
                if thinking[4] == 'nope' and int(prio[3]) < 3:
                    thinking[4] = 'ok'
                if thinking[5] == 'nope' and int(prio[4]) < 3:
                    thinking[5] = 'ok'

            print('Myśliciel: {}'.format(thinking))
            print('Priorytet: {}'.format(prio))
            ok = 0
            for x in thinking:
                if x == 'ok':
                    ok += 1
            if ok == 6:
                self.oldPrice = float(r[5])
                message = 'negotiation|toomuch|' + str(rid)
            if ok < 6:
                message = 'talk|no|' + str(rid)

            return message

    def run(self):
        '''
                    * Nawiązuje połączenie wysyłając zapytanie i czekając na odpowiedź
                    :return: dorzuci produkt do listy produktów
                    '''
        print('Agent ruszył na poszukiwania')

        # Stworzony zostanie obiekt socket z typem translacji AF_INET
        # przeznaczony dla adresów IPv4
        # SOCK_STREAM - typ używny dla protokolow TCP
        ## client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # host i port (aktualnie lokalny)
        ## target_host = "0.0.0.0"
        ## target_port = 9999

        # Nawiązanie połączneia
        ## client.connect((target_host, target_port))

        # wysłanie wiadomości
        ## client.send(message.encode("unicode-escape"))

        ## reponse = client.recv(4096)

        mm ='none'
        tran = 0

        while tran != 1:
            message = self.makeMessage(mm)
            # Wysłanie wiadomości do sztucznego sklepiku
            self.faker.message = message.encode("unicode-escape")
            self.faker.device_type = self.device
            respo = self.faker.run()

            # Odebranie odpowiedzi
            respo = respo.decode("unicode-escape")
            if respo[0] == '1':
                tran = 1
            mm = respo

        respo = respo.split('|')
        print("Odpowiedz sprzedawcy: ", respo)
        return respo
