class Encrypto():
    def __init__(self):
        self.keys = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's','t', 'u', 'v', 'w', 'x', 'y', 'z','0','1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '@', '#', '%', '^', '&', '*', '(', ')', '+', '_', '=', '-', '?', '>', '<', '.', ',', '|', ':', ';']
        self.len = len(self.key)-2
        self.cipher = []
        self.decipher = []

    def keyset(self,keylist):
        self.keys = keylist

    def encrypt(self,message,rotator):
        for word in message:
            if word ==" ":
                self.cipher.append("$")
            else:
                counter = 0
                for key in self.keys:
                    counter += 1
                    if word == key:
                        if (rotator+(counter - 1)) > self.len:
                            adder = (rotator+counter - 1) % self.len
                        else:
                            adder = (rotator+counter - 1) 

                        self.cipher.append(key[adder])

        return "".join(self.cipher)
    
    def decrypt(self,cipher,rotator):
        for word in cipher:
            if word =="$":
                self.decipher.append(" ")
            else:
                counter = 0
                for key in self.keys:
                    counter += 1
                    if word == key:
                        if ((counter - 1) -rotator) < 0:
                            adder = self.len - abs((counter - 1)-rotator)
                        else:
                            adder = ((counter - 1)-rotator) 
                        self.decipher.append(key[adder])

        return "".join(self.decipher)    


enc = Encrypto()
mes = input("TEXT : ")
rotator = int(input("ROTATOR : "))

#FOR ENCRYPTION
cipher = enc.encrypt(mes,rotator)


#FOR DECRYPTION
decipher = enc.decrypt(cipher,rotator)

