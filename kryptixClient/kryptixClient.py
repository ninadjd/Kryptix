import socket
import subprocess
import time
import random, string, multiprocessing
import kryptixEnigma


def generationPage(ip, port):
    def tag():
        num = random.randint(1000, 9999)
        tag_string = str(num)
        return tag_string

    def key_append():
        pri_1 = key_gen()
        pri_2 = key_gen()
        pri_3 = key_gen()
        tag_num = tag()
        pri = pri_1 + username + pri_2 + tag_num + pri_3
        pub = public_key_converter(pri)
        return pri, pub, tag_num

    def key_gen():
        private_key_gen = ""
        # public_key_1_gen = ""
        # public_key_2_gen = ""
        # j = "1"
        for i in range(500):
            # for j in range(4):
            charachter = random.choice(string.ascii_letters + string.digits)
            private_key_gen = private_key_gen + charachter

        # public_key_gen = public_key_1_gen + public_key_2_gen
        return private_key_gen

    def public_key_converter(priv):
        public_key_1_gen = ""
        public_key_2_gen = ""
        j = "1"
        for char in priv:
            if j == "1":
                public_key_1_gen = public_key_1_gen + char
                j = "2"
                # j = j+1
            else:
                public_key_2_gen = public_key_2_gen + char
                j = "1"
                # j = j+1
        public_key_gen = public_key_1_gen + public_key_2_gen
        return public_key_gen
    def connect(ip, port, command, data):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((ip, port))
        # data = connection.recv(1024).decode()
        # print(data)
        connection.send(command.encode())
        time.sleep(1)
        connection.send(data.encode())
    username = input('Enter Username: ')
    privateKey, publicKey, tagNumber = key_append()
    connect(ip, port, 'generate', publicKey)
    print("-----------------------------------------------------------------------------")
    print("Your Username is >> " + username)
    print("Your Tag Number is >> " + tagNumber)
    print("Your Private Key is >>\n\n" + privateKey)
    print("\nYour Public Key is >>\n\n" + publicKey)
    print(
        "\nSave all these details somewhere! All these details will be required during the time of Encryption and Decryption!")
    print("\nYou can now go back to the Main Page for Encryption and Decryption!")
    print("\nDon't Worry! You can exit the program now and come back later. Just save these details!")
    gen_resp = input("\n\nDo you want to go back to the Main Page for Encryption and Decryption?[y/n]>> ")
    if gen_resp == "y" or gen_resp == "Y":
        main_func()
    elif gen_resp == "n" or gen_resp == "N":
        exit()
    else:
        print("\nENTER A VALID RESPONSE!\n")
        exit()

def cipherClient(key1, key2, ip, port, serverIP):
    def connect(ip, port, command, data):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((ip, port))
        # data = connection.recv(1024).decode()
        # print(data)
        connection.send(command.encode())
        time.sleep(1)
        connection.send(data.encode())
    #
    def listen(ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        connection, address = listener.accept()
        recvData = connection.recv(4096).decode()
        if recvData == 'msg':
            msg = connection.recv(4096).decode()
            msg = kryptixEnigma.decryptionFunction(key1, key2, msg)
            if msg == '/exit':
                print('\nExiting Kryptix...\n\n')
                exit()
            if msg == '/error':
                print('\nSomething went wrong!\n\nExiting Kryptix...\n')
                exit()
            print('-->' + msg)
    #
    subprocess.call('clear')
    if port == 4444:
        # p1 = multiprocessing.Process(target=listen, args=(ip, 8080))
        # p1.start()
        try:
            while True:
                msg = input('>> ')
                if msg == '/exit':
                    connect(serverIP, 8080, 'msg', msg)
                    break
                else:
                    msg = kryptixEnigma.encryptionFunction(key1, key2, msg)
                    connect(serverIP, 8080, 'msg', msg)
        except:
            connect(serverIP, 8080, 'error', '/error')
            # msg = kryptixEnigma.encryptionFunction(key1, key2, msg)
            # print(msg)
            # print(kryptixEnigma.decryptionFunction(key2, key1, msg))
            # connect(serverIP, 8080, 'msg', msg)
    #
    if port == 5555:
        # p2 = multiprocessing.Process(target=listen, args=(ip, 8888))
        # p2.start()
        # while True:
        #     msg = input('>> ')
        #     msg = kryptixEnigma.encryptionFunction(key1, key2, msg)
        #     print(msg)
        #     print(kryptixEnigma.decryptionFunction(key2, key1, msg))
        #     connect(serverIP, 8888, 'msg', msg)
        while True:
            listen(ip, 8888)

    # print('hello')

def createSessionPage(ip, port):
    def connect(ip, port, command, data):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((ip, port))
        # data = connection.recv(1024).decode()
        # print(data)
        connection.send(command.encode())
        time.sleep(1)
        connection.send(data.encode())

    def listen(ip, port, publicKey, serverIP):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        connection, address = listener.accept()
        recvData = connection.recv(4096).decode()
        tempKey1 = ''
        tempKey3 = ''
        if recvData == 'tempKey1':
            tempKey1 = kryptixEnigma.decryptionFunction(publicKey, publicKey, connection.recv(6114).decode())
            print('tempKey1 received[+]')
        print('Waiting for tempKey3[+]')
        listener.listen(0)
        connection, address = listener.accept()
        recvData = connection.recv(4096).decode()
        if recvData == 'tempKey3':
            tempKey3 = kryptixEnigma.decryptionFunction(publicKey, publicKey, connection.recv(6114).decode())
            print('tempKey3 received[+]')
        cipherClient(tempKey1, tempKey3, ip, port, serverIP)


    username = input('Enter Username: ')
    tagnumber = input('Enter Tagnumber: ')
    privateKey = input('Enter PrivateKey: ')
    publicKey = input('Enter PublicKey: ')
    userAuth = kryptixEnigma.userAuthFunction(username, tagnumber, privateKey, publicKey)
    if userAuth:
        connect(ip, port, 'create', publicKey)
        print('Waiting for tempKey1[+]')
        listen('10.0.2.8', 4444, publicKey, ip)
    else:
        print('\nInvalid Credentials\n')

    # connect(ip, port, 'create', publicKey)
    # print('Waiting for tempKey1[+]')
    # listen('10.0.2.19', 4444, publicKey, ip)

    # recvData = listen('10.0.2.18', 4444)
    # if recvData == 'tempKey':
    #     tempKey = listen('10.0.2.18', 4444)
    #     print(tempKey)

def joinSessionPage(ip, port):
    def connect(ip, port, command, data):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((ip, port))
        # data = connection.recv(1024).decode()
        # print(data)
        connection.send(command.encode())
        time.sleep(1)
        connection.send(data.encode())
    def listen(ip, port, serverIP):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)
        print('Waiting for tempKey2[+]')
        connection, address = listener.accept()
        recvData = connection.recv(1024).decode()
        tempKey2 = ''
        tempKey3 = ''
        if recvData == 'tempKey2':
            tempKey2 = kryptixEnigma.decryptionFunction(publicKey, publicKey, connection.recv(6114).decode())
            print('tempKey2 received[+]')
        print('Waiting for tempKey3[+]')
        listener.listen(0)
        connection, address = listener.accept()
        recvData = connection.recv(4096).decode()
        if recvData == 'tempKey3':
            tempKey3 = kryptixEnigma.decryptionFunction(publicKey, publicKey, connection.recv(6114).decode())
            print('tempKey3 received[+]')

        cipherClient(tempKey2, tempKey3, ip, port, serverIP)

    username = input('Enter Username: ')
    tagnumber = input('Enter Tagnumber: ')
    privateKey = input('Enter PrivateKey: ')
    publicKey = input('Enter PublicKey: ')
    userAuth = kryptixEnigma.userAuthFunction(username, tagnumber, privateKey, publicKey)
    if userAuth:
        connect(ip, port, 'join', publicKey)
        listen('10.0.2.8', 5555, ip)
    else:
        print('\nInvalid Credentials\n')
    # connect(ip, port, 'join', publicKey)
    # listen('10.0.2.5', 5555, ip)

def main_func():
    # data = 'sample_plain_text'
    subprocess.call('clear')
    serverIP = '10.0.2.15'

    print('Welcome to Kryptix\n')

    print('1. Generate')
    print('2. Create a session')
    print('3. Join a session')
    print('4. Exit')

    userResponse = input('Your Response: ')
    if userResponse == '1':
        generationPage(serverIP, 4444)
    elif userResponse == '2':
        createSessionPage(serverIP, 4444)
    elif userResponse == '3':
        joinSessionPage(serverIP, 5555)
    elif userResponse == '4':
        print('\nExiting Kryptix...\n')
    else:
        print('Something is wrong')

try:
    main_func()
except KeyboardInterrupt:
    print('Keyboard Interrupt found.\n\nExiting Kryptix...\n')
    exit()