import socket
import threading

'''
   Parametry serwera nasluchiwania.

'''
bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print("[*] Nasluchiwanie na porcie %s:%d" % (bind_ip, bind_port))


def handle_client(client_socket):
    '''
    Obsluga odbioru requestow
    :param client_socket:
    :return:
    '''
    request = client_socket.recv(1024)
    print("[*] Odebrano: %s" % request)

    '''
    Odpowied na request
    '''

    client_socket.send(b"Oto moje towary.")
    client_socket.close()


while True:
    client, addr = server.accept()
    print("[*] Przyjęto polączenie od: %s:%d" % (addr[0], addr[1]))
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()

