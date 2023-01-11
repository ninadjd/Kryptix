
def encryptionFunction(key1, key2, msg):
    def supported_chars(char):
        upper_case_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
                            "T", "U", "V", "W", "X", "Y", "Z"]
        lower_case_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
                            "t", "u", "v", "w", "x", "y", "z"]
        numerics = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        symbols = [" ", ".", ",", "?", "!", "/", "<", ">", ";", ":", "[", "]", "{", "}", "(", ")", "@", "#", "~", "^", "$",
                   "%", "&", "*", "+", "-", "_", "|", "="]
        if char in upper_case_chars:
            return char
        elif char in lower_case_chars:
            return char
        elif char in numerics:
            return char
        elif char in symbols:
            return char
        else:
            print("The charachter - " + char + " is not supported!")
            exit()

    def message(msg):
        msg_list = []
        for char in msg:
            supported_character = supported_chars(char)
            msg_list.append(supported_character)
        counter = len(msg_list)
        return msg_list, counter

    def encryption(user1_key, user2_key, msg):
        user1_key_list = []
        user2_key_list = []
        key_list = []
        msg, count = message(msg)
        i = 0
        for char in user1_key:
            user1_key_list.append(char)
        for char in user2_key:
            user2_key_list.append(char)
        for j in range(count):
            if i == 0:
                key_list.append(user1_key_list[j])
                i = 1
            if i == 1:
                key_list.append(user2_key_list[j])
                i = 0
        encrypted_string = ""
        encrypted_string_list = []
        encrypted_char_list = []
        for i in range(count):
            # print(i)
            real_bin = dec_to_bin(msg[i])
            key_bin = dec_to_bin(key_list[i])
            encrypted_binary = binary_add(real_bin, key_bin)
            # print(encrypted_binary)
            encrypted_char = bin_to_char(encrypted_binary)
            encrypted_char_list.append(encrypted_char)
            # print(encrypted_string)
            enc_two = encrypt_2(encrypted_char)
            # enc_two = enc_two + carry
            encrypted_string_list.append(enc_two)
        # print(encrypted_string_list)
        shuffled_string = encrypt_3(encrypted_string_list)
        # print(shuffled_string)
        for char in shuffled_string:
            encrypted_string = encrypted_string + char
        return encrypted_string

    def encrypt_2(char):
        encrypted_char = ""
        if char == "A":
            encrypted_char = "AYOB"
        if char == "B":
            encrypted_char = "j8Sq"
        if char == "C":
            encrypted_char = "eLVV"
        if char == "D":
            encrypted_char = "XoIV"
        if char == "E":
                encrypted_char = "WPia"
        if char == "F":
                encrypted_char = "5SAM"
        if char == "G":
            encrypted_char = "blH0"
        if char == "H":
            encrypted_char = "H7WH"
        if char == "I":
            encrypted_char = "Lile"
        if char == "J":
            encrypted_char = "IZ6k"
        if char == "K":
            encrypted_char = "JhKP"
        if char == "L":
            encrypted_char = "p9Yk"
        if char == "M":
            encrypted_char = "EZ9z"
        if char == "N":
            encrypted_char = "Az2s"
        if char == "O":
            encrypted_char = "R03M"
        if char == "P":
            encrypted_char = "N9Uh"
        if char == "Q":
            encrypted_char = "7EHz"
        if char == "R":
            encrypted_char = "EcV1"
        if char == "S":
            encrypted_char = "71EK"
        if char == "T":
            encrypted_char = "YVX6"
        if char == "U":
            encrypted_char = "kxuc"
        if char == "V":
            encrypted_char = "bGRa"
        if char == "W":
            encrypted_char = "Cn2Q"
        if char == "X":
            encrypted_char = "yaNV"
        if char == "Y":
            encrypted_char = "AWd5"
        if char == "Z":
            encrypted_char = "naYd"
        if char == "a":
            encrypted_char = "yPEC"
        if char == "b":
            encrypted_char = "ObTr"
        if char == "c":
            encrypted_char = "kFnR"
        if char == "d":
            encrypted_char = "kHgk"
        if char == "e":
            encrypted_char = "bXCU"
        if char == "f":
            encrypted_char = "HySi"
        if char == "g":
            encrypted_char = "48pX"
        if char == "h":
            encrypted_char = "uh16"
        if char == "i":
            encrypted_char = "G7uq"
        if char == "j":
            encrypted_char = "y1h6"
        if char == "k":
            encrypted_char = "A2K3"
        if char == "l":
            encrypted_char = "pzwj"
        if char == "m":
            encrypted_char = "kqKK"
        if char == "n":
            encrypted_char = "NWpp"
        if char == "o":
            encrypted_char = "6Pi8"
        if char == "p":
            encrypted_char = "M0qD"
        if char == "q":
            encrypted_char = "quFW"
        if char == "r":
            encrypted_char = "GbJu"
        if char == "s":
            encrypted_char = "xdhc"
        if char == "t":
            encrypted_char = "3BEO"
        if char == "u":
            encrypted_char = "CHIC"
        if char == "v":
            encrypted_char = "tro7"
        if char == "w":
            encrypted_char = "usBx"
        if char == "x":
            encrypted_char = "ci6O"
        if char == "y":
            encrypted_char = "js5K"
        if char == "z":
            encrypted_char = "3fwl"
        if char == "0":
            encrypted_char = "5Er2"
        if char == "1":
            encrypted_char = "e4Lq"
        if char == "2":
            encrypted_char = "05Pt"
        if char == "3":
            encrypted_char = "zlgP"
        if char == "4":
            encrypted_char = "aj91"
        if char == "5":
            encrypted_char = "N1IS"
        if char == "6":
            encrypted_char = "yyBo"
        if char == "7":
            encrypted_char = "2b7K"
        if char == "8":
            encrypted_char = "7jgA"
        if char == "9":
            encrypted_char = "2hyA"
        if char == " ":
            encrypted_char = "XO2i"
        if char == ".":
            encrypted_char = "tkaJ"
        if char == ",":
            encrypted_char = "3CGd"
        if char == "?":
            encrypted_char = "Yr6A"
        if char == "!":
            encrypted_char = "azHc"
        if char == "/":
            encrypted_char = "t6BZ"
        if char == "<":
            encrypted_char = "2VoN"
        if char == ">":
            encrypted_char = "5vgc"
        if char == ";":
            encrypted_char = "exHy"
        if char == ":":
            encrypted_char = "9UtT"
        if char == "[":
            encrypted_char = "EIll"
        if char == "]":
            encrypted_char = "ViBJ"
        if char == "{":
            encrypted_char = "59st"
        if char == "}":
            encrypted_char = "oJ7l"
        if char == "(":
            encrypted_char = "3i5q"
        if char == ")":
            encrypted_char = "x7qW"
        if char == "@":
            encrypted_char = "WBBd"
        if char == "#":
            encrypted_char = "TGrI"
        if char == "~":
            encrypted_char = "tzyT"
        if char == "$":
            encrypted_char = "xErm"
        if char == "%":
            encrypted_char = "rKxO"
        if char == "^":
            encrypted_char = "ATvC"
        if char == "&":
            encrypted_char = "kvAt"
        if char == "*":
            encrypted_char = "EVm4"
        if char == "+":
            encrypted_char = "uTEe"
        if char == "-":
            encrypted_char = "VgFI"
        if char == "_":
            encrypted_char = "GKwg"
        if char == "|":
            encrypted_char = "h2gZ"
        if char == "=":
            encrypted_char = "fyOa"

        return encrypted_char

    def encrypt_3(list):
        #list = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h"]
        list_1 = []
        list_2 = []
        i = 0
        for char in list:
            if i == 0:
                #print(i)
                #print(char)
                list_1.append(char)
                i = 1
            elif i == 1:
                #print(i)
                #print(char)
                list_2.append(char)
                i = 0
        #print(list_1)
        #print(list_2)
        final = list_1 + list_2
        return final

    def bin_to_char(enc_num):
        char = ""
        if enc_num == 1:
            char = "a"
        elif enc_num == 2:
            char = "b"
        elif enc_num == 3:
            char = "c"
        elif enc_num == 4:
            char = "d"
        elif enc_num == 5:
            char = "e"
        elif enc_num == 6:
            char = "f"
        elif enc_num == 7:
            char = "g"
        elif enc_num == 8:
            char = "h"
        elif enc_num == 9:
            char = "i"
        elif enc_num == 10:
            char = "j"
        elif enc_num == 11:
            char = "k"
        elif enc_num == 12:
            char = "l"
        elif enc_num == 13:
            char = "m"
        elif enc_num == 14:
            char = "n"
        elif enc_num == 15:
            char = "o"
        elif enc_num == 16:
            char = "p"
        elif enc_num == 17:
            char = "q"
        elif enc_num == 18:
            char = "r"
        elif enc_num == 19:
            char = "s"
        elif enc_num == 20:
            char = "t"
        elif enc_num == 21:
            char = "u"
        elif enc_num == 22:
            char = "v"
        elif enc_num == 23:
            char = "w"
        elif enc_num == 24:
            char = "x"
        elif enc_num == 25:
            char = "y"
        elif enc_num == 26:
            char = "z"
        elif enc_num == 27:
            char = "A"
        elif enc_num == 28:
            char = "B"
        elif enc_num == 29:
            char = "C"
        elif enc_num == 30:
            char = "D"
        elif enc_num == 31:
            char = "E"
        elif enc_num == 32:
            char = "F"
        elif enc_num == 33:
            char = "G"
        elif enc_num == 34:
            char = "H"
        elif enc_num == 35:
            char = "I"
        elif enc_num == 36:
            char = "J"
        elif enc_num == 37:
            char = "K"
        elif enc_num == 38:
            char = "L"
        elif enc_num == 39:
            char = "M"
        elif enc_num == 40:
            char = "N"
        elif enc_num == 41:
            char = "O"
        elif enc_num == 42:
            char = "P"
        elif enc_num == 43:
            char = "Q"
        elif enc_num == 44:
            char = "R"
        elif enc_num == 45:
            char = "S"
        elif enc_num == 46:
            char = "T"
        elif enc_num == 47:
            char = "U"
        elif enc_num == 48:
            char = "V"
        elif enc_num == 49:
            char = "W"
        elif enc_num == 50:
            char = "X"
        elif enc_num == 51:
            char = "Y"
        elif enc_num == 52:
            char = "Z"
        elif enc_num == 53:
            char = "0"
        elif enc_num == 54:
            char = "1"
        elif enc_num == 55:
            char = "2"
        elif enc_num == 56:
            char = "3"
        elif enc_num == 57:
            char = "4"
        elif enc_num == 58:
            char = "5"
        elif enc_num == 59:
            char = "6"
        elif enc_num == 60:
            char = "7"
        elif enc_num == 61:
            char = "8"
        elif enc_num == 62:
            char = "9"
        elif enc_num == 63:
            char = " "
        elif enc_num == 64:
            char = "."
        elif enc_num == 65:
            char = ","
        elif enc_num == 66:
            char = "?"
        elif enc_num == 67:
            char = "!"
        elif enc_num == 68:
            char = "/"
        elif enc_num == 69:
            char = "<"
        elif enc_num == 70:
            char = ">"
        elif enc_num == 71:
            char = ";"
        elif enc_num == 72:
            char = ":"
        elif enc_num == 73:
            char = "["
        elif enc_num == 74:
            char = "]"
        elif enc_num == 75:
            char = "{"
        elif enc_num == 76:
            char = "}"
        elif enc_num == 77:
            char = "("
        elif enc_num == 78:
            char = ")"
        elif enc_num == 79:
            char = "@"
        elif enc_num == 80:
            char = "#"
        elif enc_num == 81:
            char = "~"
        elif enc_num == 82:
            char = "^"
        elif enc_num == 83:
            char = "$"
        elif enc_num == 84:
            char = "%"
        elif enc_num == 85:
            char = "&"
        elif enc_num == 86:
            char = "*"
        elif enc_num == 87:
            char = "+"
        elif enc_num == 88:
            char = "-"
        elif enc_num == 89:
            char = "_"
        elif enc_num == 90:
            char = "|"
        elif enc_num == 91:
            char = "="
        else:
            char = ""
        return char

    def dec_to_bin(char):
        value = 0
        if char == "a":
            value = 1
        elif char == "b":
            value = 2
        elif char == "c":
            value = 3
        elif char == "d":
            value = 4
        elif char == "e":
            value = 5
        elif char == "f":
            value = 6
        elif char == "g":
            value = 7
        elif char == "h":
            value = 8
        elif char == "i":
            value = 9
        elif char == "j":
            value = 10
        elif char == "k":
            value = 11
        elif char == "l":
            value = 12
        elif char == "m":
            value = 13
        elif char == "n":
            value = 14
        elif char == "o":
            value = 15
        elif char == "p":
            value = 16
        elif char == "q":
            value = 17
        elif char == "r":
            value = 18
        elif char == "s":
            value = 19
        elif char == "t":
            value = 20
        elif char == "u":
            value = 21
        elif char == "v":
            value = 22
        elif char == "w":
            value = 23
        elif char == "x":
            value = 24
        elif char == "y":
            value = 25
        elif char == "z":
            value = 26
        elif char == "A":
            value = 27
        elif char == "B":
            value = 28
        elif char == "C":
            value = 29
        elif char == "D":
            value = 30
        elif char == "E":
            value = 31
        elif char == "F":
            value = 32
        elif char == "G":
            value = 33
        elif char == "H":
            value = 34
        elif char == "I":
            value = 35
        elif char == "J":
            value = 36
        elif char == "K":
            value = 37
        elif char == "L":
            value = 38
        elif char == "M":
            value = 39
        elif char == "N":
            value = 40
        elif char == "O":
            value = 41
        elif char == "P":
            value = 42
        elif char == "Q":
            value = 43
        elif char == "R":
            value = 44
        elif char == "S":
            value = 45
        elif char == "T":
            value = 46
        elif char == "U":
            value = 47
        elif char == "V":
            value = 48
        elif char == "W":
            value = 49
        elif char == "X":
            value = 50
        elif char == "Y":
            value = 51
        elif char == "Z":
            value = 52
        elif char == "0":
            value = 53
        elif char == "1":
            value = 54
        elif char == "2":
            value = 55
        elif char == "3":
            value = 56
        elif char == "4":
            value = 57
        elif char == "5":
            value = 58
        elif char == "6":
            value = 59
        elif char == "7":
            value = 60
        elif char == "8":
            value = 61
        elif char == "9":
            value = 62
        elif char == " ":
            value = 63
        elif char == ".":
            value = 64
        elif char == ",":
            value = 65
        elif char == "?":
            value = 66
        elif char == "!":
            value = 67
        elif char == "/":
            value = 68
        elif char == "<":
            value = 69
        elif char == ">":
            value = 70
        elif char == ";":
            value = 71
        elif char == ":":
            value = 72
        elif char == "[":
            value = 73
        elif char == "]":
            value = 74
        elif char == "{":
            value = 75
        elif char == "}":
            value = 76
        elif char == "(":
            value = 77
        elif char == ")":
            value = 78
        elif char == "@":
            value = 79
        elif char == "#":
            value = 80
        elif char == "~":
            value = 81
        elif char == "^":
            value = 82
        elif char == "$":
            value = 83
        elif char == "%":
            value = 84
        elif char == "&":
            value = 85
        elif char == "*":
            value = 86
        elif char == "+":
            value = 87
        elif char == "-":
            value = 88
        elif char == "_":
            value = 89
        elif char == "|":
            value = 90
        elif char == "=":
            value = 91
        else:
            value = 0
        return value

    def binary_add(char_1, char_2):
        new_value = char_1 + char_2
        if new_value > 91:
            new_value = new_value - 91
        return new_value

    encString = encryption(key1, key2, msg)
    return encString

def decryptionFunction(key1, key2, msg):
    def message(msg):
        msg_list = []
        msg_string = ""
        i = 0
        for char in msg:
            if i == 0:
                msg_string = msg_string + char
                i = 1
            elif i == 1:
                msg_string = msg_string + char
                i = 2
            elif i == 2:
                msg_string = msg_string + char
                i = 3
            elif i == 3:
                msg_string = msg_string + char
                msg_list.append(msg_string)
                msg_string = ""
                i = 0
        counter = len(msg_list)
        return msg_list, counter

    def encrypt_3_breaker(list):
        list.reverse()
        rev_list = []
        list_1 = []
        list_2 = []
        end_list = []
        list_count = len(list)
        for i in range(list_count):
            rev_list.append(list[i])
        list.reverse()
        div_by_2 = int(list_count / 2)
        list_1_elem = list_count - div_by_2
        for i in range(div_by_2):
            list_2.append(rev_list[i])
        list_2.reverse()
        for i in range(list_1_elem):
            list_1.append(list[i])
        try:
            for j in range(list_count):
                end_list.append(list_1[j])
                end_list.append(list_2[j])
        except IndexError:
            pass
        return end_list

    def encrypt_2_breaker(encrypted_char):
        char = ""
        if encrypted_char == "AYOB":
            char = "A"
        if encrypted_char == "j8Sq":
            char = "B"
        if encrypted_char == "eLVV":
            char = "C"
        if encrypted_char == "XoIV":
            char = "D"
        if encrypted_char == "WPia":
            char = "E"
        if encrypted_char == "5SAM":
            char = "F"
        if encrypted_char == "blH0":
            char = "G"
        if encrypted_char == "H7WH":
            char = "H"
        if encrypted_char == "Lile":
            char = "I"
        if encrypted_char == "IZ6k":
            char = "J"
        if encrypted_char == "JhKP":
            char = "K"
        if encrypted_char == "p9Yk":
            char = "L"
        if encrypted_char == "EZ9z":
            char = "M"
        if encrypted_char == "Az2s":
            char = "N"
        if encrypted_char == "R03M":
            char = "O"
        if encrypted_char == "N9Uh":
            char = "P"
        if encrypted_char == "7EHz":
            char = "Q"
        if encrypted_char == "EcV1":
            char = "R"
        if encrypted_char == "71EK":
            char = "S"
        if encrypted_char == "YVX6":
            char = "T"
        if encrypted_char == "kxuc":
            char = "U"
        if encrypted_char == "bGRa":
            char = "V"
        if encrypted_char == "Cn2Q":
            char = "W"
        if encrypted_char == "yaNV":
            char = "X"
        if encrypted_char == "AWd5":
            char = "Y"
        if encrypted_char == "naYd":
            char = "Z"
        if encrypted_char == "yPEC":
            char = "a"
        if encrypted_char == "ObTr":
            char = "b"
        if encrypted_char == "kFnR":
            char = "c"
        if encrypted_char == "kHgk":
            char = "d"
        if encrypted_char == "bXCU":
            char = "e"
        if encrypted_char == "HySi":
            char = "f"
        if encrypted_char == "48pX":
            char = "g"
        if encrypted_char == "uh16":
            char = "h"
        if encrypted_char == "G7uq":
            char = "i"
        if encrypted_char == "y1h6":
            char = "j"
        if encrypted_char == "A2K3":
            char = "k"
        if encrypted_char == "pzwj":
            char = "l"
        if encrypted_char == "kqKK":
            char = "m"
        if encrypted_char == "NWpp":
            char = "n"
        if encrypted_char == "6Pi8":
            char = "o"
        if encrypted_char == "M0qD":
            char = "p"
        if encrypted_char == "quFW":
            char = "q"
        if encrypted_char == "GbJu":
            char = "r"
        if encrypted_char == "xdhc":
            char = "s"
        if encrypted_char == "3BEO":
            char = "t"
        if encrypted_char == "CHIC":
            char = "u"
        if encrypted_char == "tro7":
            char = "v"
        if encrypted_char == "usBx":
            char = "w"
        if encrypted_char == "ci6O":
            char = "x"
        if encrypted_char == "js5K":
            char = "y"
        if encrypted_char == "3fwl":
            char = "z"
        if encrypted_char == "5Er2":
            char = "0"
        if encrypted_char == "e4Lq":
            char = "1"
        if encrypted_char == "05Pt":
            char = "2"
        if encrypted_char == "zlgP":
            char = "3"
        if encrypted_char == "aj91":
            char = "4"
        if encrypted_char == "N1IS":
            char = "5"
        if encrypted_char == "yyBo":
            char = "6"
        if encrypted_char == "2b7K":
            char = "7"
        if encrypted_char == "7jgA":
            char = "8"
        if encrypted_char == "2hyA":
            char = "9"
        if encrypted_char == "XO2i":
            char = " "
        if encrypted_char == "tkaJ":
            char = "."
        if encrypted_char == "3CGd":
            char = ","
        if encrypted_char == "Yr6A":
            char = "?"
        if encrypted_char == "azHc":
            char = "!"
        if encrypted_char == "t6BZ":
            char = "/"
        if encrypted_char == "2VoN":
            char = "<"
        if encrypted_char == "5vgc":
            char = ">"
        if encrypted_char == "exHy":
            char = ";"
        if encrypted_char == "9UtT":
            char = ":"
        if encrypted_char == "EIll":
            char = "["
        if encrypted_char == "ViBJ":
            char = "]"
        if encrypted_char == "59st":
            char = "{"
        if encrypted_char == "oJ7l":
            char = "}"
        if encrypted_char == "3i5q":
            char = "("
        if encrypted_char == "x7qW":
            char = ")"
        if encrypted_char == "WBBd":
            char = "@"
        if encrypted_char == "TGrI":
            char = "#"
        if encrypted_char == "tzyT":
            char = "~"
        if encrypted_char == "xErm":
            char = "$"
        if encrypted_char == "rKxO":
            char = "%"
        if encrypted_char == "ATvC":
            char = "^"
        if encrypted_char == "kvAt":
            char = "&"
        if encrypted_char == "EVm4":
            char = "*"
        if encrypted_char == "uTEe":
            char = "+"
        if encrypted_char == "VgFI":
            char = "-"
        if encrypted_char == "GKwg":
            char = "_"
        if encrypted_char == "h2gZ":
            char = "|"
        if encrypted_char == "fyOa":
            char = "="

        return char

    def dec_to_bin(char):
        value = 0
        if char == "a":
            value = 1
        elif char == "b":
            value = 2
        elif char == "c":
            value = 3
        elif char == "d":
            value = 4
        elif char == "e":
            value = 5
        elif char == "f":
            value = 6
        elif char == "g":
            value = 7
        elif char == "h":
            value = 8
        elif char == "i":
            value = 9
        elif char == "j":
            value = 10
        elif char == "k":
            value = 11
        elif char == "l":
            value = 12
        elif char == "m":
            value = 13
        elif char == "n":
            value = 14
        elif char == "o":
            value = 15
        elif char == "p":
            value = 16
        elif char == "q":
            value = 17
        elif char == "r":
            value = 18
        elif char == "s":
            value = 19
        elif char == "t":
            value = 20
        elif char == "u":
            value = 21
        elif char == "v":
            value = 22
        elif char == "w":
            value = 23
        elif char == "x":
            value = 24
        elif char == "y":
            value = 25
        elif char == "z":
            value = 26
        elif char == "A":
            value = 27
        elif char == "B":
            value = 28
        elif char == "C":
            value = 29
        elif char == "D":
            value = 30
        elif char == "E":
            value = 31
        elif char == "F":
            value = 32
        elif char == "G":
            value = 33
        elif char == "H":
            value = 34
        elif char == "I":
            value = 35
        elif char == "J":
            value = 36
        elif char == "K":
            value = 37
        elif char == "L":
            value = 38
        elif char == "M":
            value = 39
        elif char == "N":
            value = 40
        elif char == "O":
            value = 41
        elif char == "P":
            value = 42
        elif char == "Q":
            value = 43
        elif char == "R":
            value = 44
        elif char == "S":
            value = 45
        elif char == "T":
            value = 46
        elif char == "U":
            value = 47
        elif char == "V":
            value = 48
        elif char == "W":
            value = 49
        elif char == "X":
            value = 50
        elif char == "Y":
            value = 51
        elif char == "Z":
            value = 52
        elif char == "0":
            value = 53
        elif char == "1":
            value = 54
        elif char == "2":
            value = 55
        elif char == "3":
            value = 56
        elif char == "4":
            value = 57
        elif char == "5":
            value = 58
        elif char == "6":
            value = 59
        elif char == "7":
            value = 60
        elif char == "8":
            value = 61
        elif char == "9":
            value = 62
        elif char == " ":
            value = 63
        elif char == ".":
            value = 64
        elif char == ",":
            value = 65
        elif char == "?":
            value = 66
        elif char == "!":
            value = 67
        elif char == "/":
            value = 68
        elif char == "<":
            value = 69
        elif char == ">":
            value = 70
        elif char == ";":
            value = 71
        elif char == ":":
            value = 72
        elif char == "[":
            value = 73
        elif char == "]":
            value = 74
        elif char == "{":
            value = 75
        elif char == "}":
            value = 76
        elif char == "(":
            value = 77
        elif char == ")":
            value = 78
        elif char == "@":
            value = 79
        elif char == "#":
            value = 80
        elif char == "~":
            value = 81
        elif char == "^":
            value = 82
        elif char == "$":
            value = 83
        elif char == "%":
            value = 84
        elif char == "&":
            value = 85
        elif char == "*":
            value = 86
        elif char == "+":
            value = 87
        elif char == "-":
            value = 88
        elif char == "_":
            value = 89
        elif char == "|":
            value = 90
        elif char == "=":
            value = 91
        else:
            value = 0
        return value

    def decryption(user1_key, user2_key, msg):
        user1_key_list = []
        user2_key_list = []
        key_list = []
        msg_list, count = message(msg)
        i = 0
        for char in user1_key:
            user1_key_list.append(char)
        for char in user2_key:
            user2_key_list.append(char)
        for j in range(count):
            if i == 0:
                key_list.append(user2_key_list[j])
                i = 1
            if i == 1:
                key_list.append(user1_key_list[j])
                i = 0
        breaked_encrypt_3 = encrypt_3_breaker(msg_list)
        breaked_string = ""
        for elem in breaked_encrypt_3:
            breaked_encrypt_2 = encrypt_2_breaker(elem)
            breaked_string = breaked_string + breaked_encrypt_2
        breaked_str_list = []
        for char in breaked_string:
            breaked_str_list.append(char)

        decrypted_str = ""
        for i in range(count):
            real_bin = dec_to_bin(breaked_str_list[i])
            key_bin = dec_to_bin(key_list[i])
            decrypted_binary = binary_subtraction(real_bin, key_bin)
            decrypted_char = bin_to_char(decrypted_binary)
            decrypted_str = decrypted_str + decrypted_char
        return decrypted_str

    def bin_to_char(enc_num):
        char = ""
        if enc_num == 1:
            char = "a"
        elif enc_num == 2:
            char = "b"
        elif enc_num == 3:
            char = "c"
        elif enc_num == 4:
            char = "d"
        elif enc_num == 5:
            char = "e"
        elif enc_num == 6:
            char = "f"
        elif enc_num == 7:
            char = "g"
        elif enc_num == 8:
            char = "h"
        elif enc_num == 9:
            char = "i"
        elif enc_num == 10:
            char = "j"
        elif enc_num == 11:
            char = "k"
        elif enc_num == 12:
            char = "l"
        elif enc_num == 13:
            char = "m"
        elif enc_num == 14:
            char = "n"
        elif enc_num == 15:
            char = "o"
        elif enc_num == 16:
            char = "p"
        elif enc_num == 17:
            char = "q"
        elif enc_num == 18:
            char = "r"
        elif enc_num == 19:
            char = "s"
        elif enc_num == 20:
            char = "t"
        elif enc_num == 21:
            char = "u"
        elif enc_num == 22:
            char = "v"
        elif enc_num == 23:
            char = "w"
        elif enc_num == 24:
            char = "x"
        elif enc_num == 25:
            char = "y"
        elif enc_num == 26:
            char = "z"
        elif enc_num == 27:
            char = "A"
        elif enc_num == 28:
            char = "B"
        elif enc_num == 29:
            char = "C"
        elif enc_num == 30:
            char = "D"
        elif enc_num == 31:
            char = "E"
        elif enc_num == 32:
            char = "F"
        elif enc_num == 33:
            char = "G"
        elif enc_num == 34:
            char = "H"
        elif enc_num == 35:
            char = "I"
        elif enc_num == 36:
            char = "J"
        elif enc_num == 37:
            char = "K"
        elif enc_num == 38:
            char = "L"
        elif enc_num == 39:
            char = "M"
        elif enc_num == 40:
            char = "N"
        elif enc_num == 41:
            char = "O"
        elif enc_num == 42:
            char = "P"
        elif enc_num == 43:
            char = "Q"
        elif enc_num == 44:
            char = "R"
        elif enc_num == 45:
            char = "S"
        elif enc_num == 46:
            char = "T"
        elif enc_num == 47:
            char = "U"
        elif enc_num == 48:
            char = "V"
        elif enc_num == 49:
            char = "W"
        elif enc_num == 50:
            char = "X"
        elif enc_num == 51:
            char = "Y"
        elif enc_num == 52:
            char = "Z"
        elif enc_num == 53:
            char = "0"
        elif enc_num == 54:
            char = "1"
        elif enc_num == 55:
            char = "2"
        elif enc_num == 56:
            char = "3"
        elif enc_num == 57:
            char = "4"
        elif enc_num == 58:
            char = "5"
        elif enc_num == 59:
            char = "6"
        elif enc_num == 60:
            char = "7"
        elif enc_num == 61:
            char = "8"
        elif enc_num == 62:
            char = "9"
        elif enc_num == 63:
            char = " "
        elif enc_num == 64:
            char = "."
        elif enc_num == 65:
            char = ","
        elif enc_num == 66:
            char = "?"
        elif enc_num == 67:
            char = "!"
        elif enc_num == 68:
            char = "/"
        elif enc_num == 69:
            char = "<"
        elif enc_num == 70:
            char = ">"
        elif enc_num == 71:
            char = ";"
        elif enc_num == 72:
            char = ":"
        elif enc_num == 73:
            char = "["
        elif enc_num == 74:
            char = "]"
        elif enc_num == 75:
            char = "{"
        elif enc_num == 76:
            char = "}"
        elif enc_num == 77:
            char = "("
        elif enc_num == 78:
            char = ")"
        elif enc_num == 79:
            char = "@"
        elif enc_num == 80:
            char = "#"
        elif enc_num == 81:
            char = "~"
        elif enc_num == 82:
            char = "^"
        elif enc_num == 83:
            char = "$"
        elif enc_num == 84:
            char = "%"
        elif enc_num == 85:
            char = "&"
        elif enc_num == 86:
            char = "*"
        elif enc_num == 87:
            char = "+"
        elif enc_num == 88:
            char = "-"
        elif enc_num == 89:
            char = "_"
        elif enc_num == 90:
            char = "|"
        elif enc_num == 91:
            char = "="
        else:
            char = ""
        return char

    def binary_subtraction(real_bin, key_bin):
        real_value = 0
        if real_bin >= key_bin:
            real_value = real_bin - key_bin
        else:
            real_bin = real_bin + 91
            real_value = real_bin - key_bin
        return real_value

    decString = decryption(key1, key2, msg)
    return decString