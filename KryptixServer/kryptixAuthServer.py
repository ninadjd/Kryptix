import socket
import time
import threading
import kryptixKeyServer

# userIp1 = 0
# userPort1 = 0
def data(ip1, port1):
    userIp1 = ip1
    userPort1 = port1

def generate(userPublicKey):
    publicKeyFile = open('publicKeyList', 'a')
    publicKeyFile.write(userPublicKey + '\n')

def sessionPage(user1PublicKey, userIp1, userPort1):
    def countdown(s):
        global timer
        timer = int(s)
        for x in range(timer):
            timer = timer - 1
            time.sleep(1)

    def connect(ip, port, command, data):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((ip, port))
        connection.send(command.encode())
        time.sleep(1)
        connection.send(data.encode())


    def listen(ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print("[+]Waiting for User2 for Connection")
        connection, address = listener.accept()
        print("[+]Got a connection from " + str(address[0]) + ' at port ' + str(port))
        userIp2 = address[0]
        userPort2 = port
        recvData = connection.recv(4096).decode()
        if recvData == 'join':
            user2PublicKey = connection.recv(4096).decode()
            user2Auth = authenticate(user2PublicKey)
            if user2Auth:
                print('Authentication Successful')
                connection.close()
                kryptixKeyServer.server(userIp1, userIp2, userPort1, userPort2, user1PublicKey, user2PublicKey)


    def authenticate(publicKey):
        publicKeyFile = open('publicKeyList', 'r')
        publicKeyList = publicKeyFile.readlines()
        for key in publicKeyList:
            if publicKey in key:
                return True
            # timeUp = 0
            # timeThread = threading.Thread(target=countdown, args=(10,))
            # timeThread.start()
    user1Auth = authenticate(user1PublicKey)
    if user1Auth:
        listen('10.0.2.15', 5555)
            # if timeUp == 1:
            #     print('Time is up')


def keyGen():
    temp1 = 'temp1'
    temp2 = 'temp2'
    temp3 = 'temp3'
    return temp1,temp2,temp3

# def listen(ip, port):
#     listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     listener.bind((ip, port))
#     listener.listen(0)
#     print("[+]Waiting for connections")
#     connection, address = listener.accept()
#     print("[+]Got a connection from " + str(address[0]) + ' at port ' + str(port))
#     recvData = connection.recv(1024).decode()
#     print(recvData)
#     if recvData == 'generate':
#         publicKey = connection.recv(1024).decode()
#         generate(publicKey)
#     elif recvData == 'create':
#         publicKey = connection.recv(1024).decode()
#         print(publicKey)
#         sessionPage(publicKey)
#
#
# while True:
#     listen('10.0.2.15', 4444)


