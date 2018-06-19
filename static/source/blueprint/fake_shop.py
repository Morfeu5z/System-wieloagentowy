# search|office/universal/game, talk|yes/no, negotiate|toomuch/ok/nope, show|product_id
import random
import time


from static.source.model import session
from static.source.model.Items import Items
from static.source.model.Memory import Memory


class Faker_Shop:
    def __init__(self, message, orginalType, id):
        self.message = message # table
        self.device_type = orginalType # np game
        self.newPrice = 0
        self.shopID = id
        self.sold = 0

    def search(self, message, box):
        self.device_type = message
        back_message = 'Look'
        fromMemory = None
        jackie = None
        dead = 0
        while dead < 3:
            try:
                jackie = session.query(Memory).filter(Memory.type == str(self.device_type)).order_by(Memory.sold.asc()).first()
                dead = 3
            except:
                dead += 1
                time.sleep(.100)
                if dead > 2:
                    return '2'
        if jackie:
            jackie = int(jackie.sold) + 3
            print('=== Jackie: {}'.format(jackie))
            dead = 0
            while dead < 3:
                try:
                    fromMemory = session.query(Memory).filter(Memory.type == str(self.device_type)).filter(Memory.sold < jackie).all()
                    dead = 3
                except:
                    dead += 1
                    time.sleep(.100)
                    if dead > 2:
                        return '2'

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
        # print('== MessageZero: {} =='.format(messageZero))
        # print('== Message: {} =='.format(message))
        if message == 'end':
            return '2'
        else:
            message = message.split('$')

        if message[0] == 'toomuch':
            humor = random.randint(1, 5)
            print('Shop ID: {}, Obniżka: {}%'.format(self.shopID, humor))
            dead = 0
            while dead < 3:
                try:
                    item = session.query(Items).filter(Items.id == box).first()
                    dead = 3
                except:
                    dead += 1
                    time.sleep(.100)
                    if dead > 2:
                        return '2'

            self.newPrice = item.price - ((item.price * humor) / 100)
            print('Shop ID: {}, Old price: {} | New price: {}'.format(self.shopID, item.price, self.newPrice))
            return 'negotiation|' + str(self.newPrice) + '$' + message[1] + '|' + box
        elif message[0] == 'ok':
            dead = 0
            while dead < 3:
                try:
                    item = session.query(Items).filter(Items.id == box).first()
                    dead = 3
                except:
                    dead += 1
                    time.sleep(.100)
                    if dead > 2:
                        return '2'

            item = session.query(Items).filter(Items.id == box).first()
            memo = session.query(Memory).filter(Memory.deviceID == box).all()
            # print('=== {} ==='.format(len(memo)))
            alert = len(memo)
            if len(memo) == 0:
                print('=== {} ==='.format('Ot coś nowego'))
                self.device_type = message[2]
                # print('=== sdt: {}'.format(message[2]))
                session.add(Memory(box, message[2], 1))
                session.commit()
            else:
                for x in memo:
                    if x.type != message[2] and alert<3:
                        print('=== {} ==='.format('Inny typ inne użądzenie'))
                        session.add(Memory(box, message[2], 0))
                        session.commit()
                    elif x.type == message[2] and alert<3:
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
        return 'none'


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
