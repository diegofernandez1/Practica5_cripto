from prime_generator import generate_prime
import utils
from random import randint

class RSA():

    def __init__(self):
        """
        Constructor de RSA, aquí se deben de generar los primos p y q
        para que puedan ser vistos por toda la clase, así como la llave
        pública y privada.
        """
        #Aquí también deben de generar su priv_key y pub_key
        self.p=generate_prime(100)
        self.q=generate_prime(100)
        self.n=self.p*self.q
        aux=self.__phi__()
        while True:
            aux_e=randint(1,aux)
            if(mcd(aux,aux_e) is 1):
                self.pub_key=aux_e
                break       
        file=open("pub_key","w+")
        file.write("("+str(self.n)+","+str(self.pub_key)+")")
        self.priv_key=modInverse(self.pub_key, self.n)
        

    def __phi__(self):
        """
        Función completamente privada y auxiliar, únicamente para el uso de las
        pruebas unitarias.
        :return: el número de primos relativos con n.
        """
        return (self.p -1)*(self.q -1)
            

    def encrypt(self, message):
        """
        Encripta un mensaje recibido como parámetro y lo regresa a manera
        de lista de enteros.
        :param message: el mensaje a encriptar.
        :return: una lista de enteros con el mensaje encriptado.
        """
        criptotext=[]
        for i in range(0,len(message)):
            aux=ord(message[i])
            aux=(aux**self.pub_key) % self.n
            criptotext.append(aux)
        return criptotext

    def decrypt(self, criptotext):
        """
        Desencripta un criptotexto cifrado con RSA y lo regresa a manera
        de cadena, recuperando la información del mensaje original.
        :param criptotext: el mensaje recibido que se va a desencriptar.
        :return: una cadena con el mensaje original.
        """
        clear_text=""
        for i in range(0,len(criptotext)):
            aux=criptotext[i]
            aux=(aux**self.priv_key) % self.n
            clear_text.append(aux)
        return clear_text
        
