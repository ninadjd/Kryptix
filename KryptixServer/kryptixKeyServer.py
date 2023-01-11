# import kryptixAuthServer
import random, string, socket, time
import kryptixCipherServer, kryptixAuthServer, kryptixEnigma

def server(ip1, ip2, port1, port2, key1, key2):
    def connect(ip, port, command, data):
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((str(ip), port))
        connection.send(command.encode())
        time.sleep(1)
        connection.send(data.encode())
        connection.close()
    tempKey1 = keyGen()
    tempKey2 = keyGen()
    tempKey3 = keyGen()
    encTempKey1 = kryptixEnigma.encryptionFunction(key1, key1, tempKey1)
    connect(ip1, port1, 'tempKey1', encTempKey1)
    encTempKey2 = kryptixEnigma.encryptionFunction(key2, key2, tempKey2)
    connect(ip2, port2, 'tempKey2', encTempKey2)
    time.sleep(1)
    encTempKey3_1 = kryptixEnigma.encryptionFunction(key1, key1, tempKey3)
    connect(ip1, port1, 'tempKey3', encTempKey3_1)
    encTempKey3_2 = kryptixEnigma.encryptionFunction(key2, key2, tempKey3)
    connect(ip2, port2, 'tempKey3', encTempKey3_2)
    print('TempKey Generation Successfull')
    kryptixCipherServer.keys(tempKey1, tempKey2, tempKey3, ip1, ip2, port1, port2)

def keyGen():
    key = ""
    # public_key_1_gen = ""
    # public_key_2_gen = ""
    # j = "1"
    for i in range(1500):
        # for j in range(4):
        charachter = random.choice(string.ascii_letters + string.digits)
        key = key + charachter

    # public_key_gen = public_key_1_gen + public_key_2_gen
    return key

