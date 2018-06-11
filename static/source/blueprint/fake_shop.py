# search|office/universal/game, talk|yes/no, negotiate|toomuch/ok/nope, show|product_id
import random
import threading

from static.source.model import session
from static.source.model.Items import Items

class Faker_Shop:
    def __init__(self):
        threading.Thread.__init__(self)
        self.message = []
        self.device_type = ''
        self.newPrice = 0

    def search(self, message, box):
        self.device_type = message
        print('No ja to szukam laptopa typu: {}'.format(self.device_type))
        randID = random.randint(0, session.query(Items).count() - 1)
        item = session.query(Items).filter(Items.id == randID).first()
        if not item:
            randID = random.randint(0, session.query(Items).count() - 1)
            item = session.query(Items).filter(Items.id == randID).first()
        print('Z bazy: {}'.format(item.name))
        # Generowanie odpowiedzi
        back_message = 'Look|' + \
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
            print('Remember {}'.format(box))
            newSearch = self.search(self.device_type, box)
        return newSearch


    def negotiation(self, message, box):
        if message == 'toomuch':
            humor = random.randint(1,5)
            print('Obniżka: {}%'.format(humor))
            item = session.query(Items).filter(Items.id == box).first()
            self.newPrice = item.price - ((item.price * humor)/100)
            print('Old price: {} | New price: {}'.format(item.price, self.newPrice))
            return 'negotiation|' + str(self.newPrice) + '|' + box
        if message == 'ok':
            item = session.query(Items).filter(Items.id == box).first()
            back_message = '1|' + \
                           str(item.id) + '|' + \
                           str(item.name) + '|' + \
                           str(item.type) + '|' + \
                           str(item.weight) + '|' + \
                           str(item.cpu) + '|' + \
                           str(item.gpu) + '|' + \
                           str(item.battery) + '|' + \
                           str(item.dec) + '|' + \
                           str(self.newPrice) + '|' + \
                           str(item.procesor) + '|' + \
                           str(item.grafika)
            return back_message


    def show(self, message, box):
        print('pid')


    def run(self):
        '''
        * Faker dla sklepu
        *
        :param message
        :return: propozycja produktu
        '''

        message = str(self.message.decode("unicode-escape"))
        print('Message decode: {}'.format(message))
        message = message.split('|')

        # opcje dla typu rozmowy
        switchOption = {
            'search': self.search,
            'talk': self.talk,
            'negotiation': self.negotiation,
            'show': self.show
        }

        # Wiadomość zwrotna
        back = switchOption[message[0]](message[1], message[2])
        print('Back message: {}'.format(back))

        return back.encode("unicode-escape")