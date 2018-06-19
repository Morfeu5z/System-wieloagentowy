# search|office/universal/game, talk|yes/no, negotiate|toomuch/ok/nope, show|product_id
import random
import threading
import multiprocessing

from static.source.model import session
from static.source.model.Items import Items
from static.source.model.Memory import Memory


class Faker_Shop:
    def __init__(self, message, type, id):
        self.message = message # table
        self.device_type = type # np game
        self.newPrice = 0
        self.shopID = id
        self.sold = 0

    def search(self, message, box):
        # self.device_type = message
        back_message = 'Look'
        fromMemory = None
        jackie = session.query(Memory).filter(Memory.type == str(self.device_type)).order_by(Memory.sold.asc()).first()
        if jackie:
            jackie = int(jackie.sold) + 3
            print('=== Jackie: {}'.format(jackie))
            fromMemory = session.query(Memory).filter(Memory.type == str(self.device_type)).filter(Memory.sold < jackie).all()
        memoList = []
        memoTrue = False
        if fromMemory:
            if len(fromMemory)>10:
                memoTrue = True
                for x in fromMemory:
                    memoList.append(x.deviceID)

        itemsCount = session.query(Items).count() - 1

        for x in range(10):
            if memoTrue and x >= 7:
                # Traf z pamięci
                randID = random.choice(memoList)
            else:
                # Ślepy traf
                randID = random.randint(0, itemsCount)
            item = session.query(Items).filter(Items.id == randID).first()


            # Jeśli obiekt nie istnieje
            while not item:
                print('Item: {}'.format(item))
                randID = random.randint(0, itemsCount)
                item = session.query(Items).filter(Items.id == randID).first()

            # Generowanie odpowiedzi
            back_message += '&' + \
                           str(item.id) + '|' + \
                           str(item.name) + '|' + \
                           str(item.type) + '|' + \
                           str(item.weight) + '|' + \
                           str(item.cpu) + '|' + \
                           str(item.gpu) + '|' + \
                           str(item.battery) + '|' + \
                           str(item.dec) + '|' + \
                           str(item.price) + '|' + \
                           str(item.procesor) + '|' + \
                           str(item.grafika)
            # print(back_message)
        return back_message

    def talk(self, message, box):
        if message == 'no':
            print('Something else')
            # print('Last item id: {}'.format(box))
            newSearch = self.search(self.device_type, box)
        return newSearch

    def negotiation(self, message, box):
        # print('== Message: {} =='.format(message))
        messageZero = message
        message = message.split('$')
        # print('== MessageZero: {} =='.format(messageZero))
        # print('== Message: {} =='.format(message))
        if messageZero == 'end':
            return '2'
        elif message[0] == 'toomuch':
            humor = random.randint(1, 5)
            print('Shop ID: {}, Obniżka: {}%'.format(self.shopID, humor))
            item = session.query(Items).filter(Items.id == box).first()
            self.newPrice = item.price - ((item.price * humor) / 100)
            print('Shop ID: {}, Old price: {} | New price: {}'.format(self.shopID, item.price, self.newPrice))
            return 'negotiation|' + str(self.newPrice) + '$' + message[1] + '|' + box
        elif message[0] == 'ok':
            item = session.query(Items).filter(Items.id == box).first()
            memo = session.query(Memory).filter(Memory.deviceID == box).all()
            # print('=== {} ==='.format(len(memo)))
            if len(memo) == 0:
                print('=== {} ==='.format('Ot coś nowego'))
                session.add(Memory(box, self.device_type, 1))
                session.commit()
            alert = len(memo)
            for x in memo:
                if x.type != self.device_type and alert<3:
                    print('=== {} ==='.format('Inny typ inne użądzenie'))
                    session.add(Memory(box, self.device_type, 0))
                    session.commit()
                elif x.type == self.device_type and alert<3:
                    print('=== {} === {}'.format('+1 do sprzedarzy', box))
                    x.sold = int(x.sold) + 1
                    session.add(x)
                    session.commit()

            back_message = '1|' + \
                           str(item.id) + '|' + \
                           str(item.name) + '|' + \
                           str(item.type) + '|' + \
                           str(item.weight) + '|' + \
                           str(item.cpu) + '|' + \
                           str(item.gpu) + '|' + \
                           str(item.battery) + '|' + \
                           str(item.dec) + '|' + \
                           str(message[1]) + '|' + \
                           str(item.procesor) + '|' + \
                           str(item.grafika)
            return back_message


    def run(self):
        '''
        * Faker dla sklepu
        *
        :param message
        :return: propozycja produktu
        '''

        # print('Message decode: {}'.format(message))
        message = self.message

        # opcje dla typu rozmowy
        switchOption = {
            'search': self.search,
            'talk': self.talk,
            'negotiation': self.negotiation
        }

        # Wiadomość zwrotna
        back = switchOption[message[0]](message[1], message[2])
        # print('Back message: {}'.format(back))

        # return back.encode("unicode-escape")
        return back
