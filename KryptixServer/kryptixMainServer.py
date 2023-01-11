import socket
import kryptixAuthServer, kryptixKeyServer

def listen(ip, port):
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind((ip, port))
    listener.listen(0)
    print("[+]Waiting for connections")
    connection, address = listener.accept()
    print("[+]Got a connection from " + str(address[0]) + ' at port ' + str(port))
    # kryptixAuthServer.data(str(address[0]), str(port))
    recvData = connection.recv(4096).decode()
    print(recvData)
    if recvData == 'generate':
        publicKey = connection.recv(4096).decode()
        kryptixAuthServer.generate(publicKey)
    elif recvData == 'create':
        publicKey = connection.recv(4096).decode()
        kryptixAuthServer.sessionPage(publicKey, str(address[0]), port)


try:
    while True:
        listen('10.0.2.15', 4444)
except KeyboardInterrupt:
    print('Keyboard Interrupt found.\n\nClosing Kryptix Server...\n')