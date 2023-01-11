import time, socket, multiprocessing, kryptixEnigma


def connect(ip, port, command, data):
    # while True:
    # print('4' + port)
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((str(ip), port))
    connection.send(command.encode())
    time.sleep(1)
    connection.send(data.encode())
    connection.close()

def cipherServer(msg, ip, port, key1, key2, keyServer):
    decryptedMsg = kryptixEnigma.decryptionFunction(keyServer, key1, msg)
    encryptedMsg = kryptixEnigma.encryptionFunction(keyServer, key2, decryptedMsg)
    if port == 8080:
        connect(ip, 8888, 'msg', encryptedMsg)
    if port == 8888:
        connect(ip, 8080, 'msg', encryptedMsg)

# def listener(ip, port, k1, k2, kS, ip1, ip2):
#     if port == 4444:
#         i = 1
#         while True:
#             listen(ip, 8080, k1, k2, kS, ip1, ip2)
#             i = i + 1
#
#     if port == 5555:
#         j = 1
#         while True:
#             listen(ip, 8888, k1, k2, kS, ip1, ip2)
#             j = j + 1


def listen(ip, port, k1, k2, kS, ip1, ip2):
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind((ip, port))
    listener.listen(0)
    connection, address = listener.accept()
    recvData = connection.recv(1024).decode()
    if recvData == 'msg':
        recvData = connection.recv(4096).decode()
        if port == 8080:
            if recvData == '/exit':
                print('\nDisconnecting...\n')
                # recvData = connection.recv(4096).decode()
                print(recvData)
                cipherServer(recvData, ip1, 8080, k1, k2, kS)
                time.sleep(0.5)
                return 1
            else:
                cipherServer(recvData, ip1, 8080, k1, k2, kS)
        elif port == 8888:
            cipherServer(recvData, ip2, port, k2, k2, kS)
        return 0
    if recvData == 'error':
        print('\nError at Client Side\n\nDisconnecting...\n')
        recvData = connection.recv(4096).decode()
        cipherServer(recvData, ip1, 8080, k1, k2, kS)
        return 1



def keys(user1Key, user2Key, serverKey, ip1, ip2, port1, port2):
    tempKeyFile = open('tempKeyList', 'a')
    tempKeyFile.write(user1Key + '\n')
    tempKeyFile.write(user2Key + '\n')
    tempKeyFile.write(serverKey + '\n')
    tempKeyFile.close()
    print('Connection Established Successfully')
    while True:
        try:
            # listen('10.0.2.15', 8080, user1Key, user2Key, serverKey, ip1, ip2)
            if (listen('10.0.2.15', 8080, user1Key, user2Key, serverKey, ip1, ip2)) > 0:
                with open('tempKeyList', 'r+') as tempKeyFile:
                    tempKeyFile.truncate()
                break
        except:
            with open('tempKeyList', 'r+') as tempKeyFile:
                tempKeyFile.truncate()
            break
        # print('hello')
        # serverIP = '10.0.2.15'
        # serverPort = 8080
        # listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # listener.bind((serverIP, serverPort))
        # listener.listen(0)
        # connection, address = listener.accept()
        # recvData = connection.recv(1024).decode()
        # if recvData == 'msg':
        #     recvData = connection.recv(4096).decode()
        #     if serverPort == 8080:
        #         cipherServer(recvData, ip1, 8080, user1Key, user2Key, serverKey)
        #     # elif serverPort == 8888:
        #     #     cipherServer(recvData, ip2, port, k2, k2, kS)
        # if recvData == 'exit':
        #     print('\nDisconnecting...\n')
        #     break
        # listen('10.0.2.15', 8888, user1Key, user2Key, serverKey, ip1, ip2)
    # command = listen('10.0.2.15', 4444)
    # p1 = multiprocessing.Process(target= listener, args= ('10.0.2.15', port1, user1Key, user2Key, serverKey, ip1, ip2))
    # p2 = multiprocessing.Process(target= listener, args= ('10.0.2.15', port2, user1Key, user2Key, serverKey, ip1, ip2))
    # p1.start()
    # p2.start()
    # while True:
    #     p1.join()
    #     p2.join()

