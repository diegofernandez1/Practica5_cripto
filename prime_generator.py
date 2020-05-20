from random import randint
from random import randrange
from utils import *
import math

def big_int(size=None):
    """
    Generador de números aleatorios de un tamaño fijo recibido como parámetro, si el parámetro es
    menor que 100 o None, entonces la función no le hace caso y genera uno de tamaño arbitrario,
    máximo es de 150 dígitos.
    :return: Un número del tamaño descrito.
    """
    if size is None or size < 100:
        size = randint(100, 150)
    kind_of_number = [randint(0, 9) for i in range(size)]
    if kind_of_number[0] == 0:
        kind_of_number[0] = randint(1, 9)
    to_string = ""
    return to_string.join(map(str, kind_of_number))
        
def miller_rabin(n):
    """
    Implementación del test de primalidad de Miller-Rabin.
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    nMinusOne = n-1
    twoAdicVal = get2adicVal(nMinusOne)
    factorN = nMinusOne // pow(2,twoAdicVal)

    a = getA(n)
    aToM = pow(a,factorN,n)
    if congruentWithBMod(aToM,1,n) or congruentWithBMod(aToM,-1,n):
        return True
    sIndex = 1
    while sIndex < twoAdicVal: 
        powerTwo = pow(2,sIndex)
        aToPower = pow(aToM,powerTwo,n)
        if congruentWithBMod(aToPower,1,n):
            return False
        if congruentWithBMod(aToPower,-1,n):
            return True
        sIndex = sIndex + 1
    return False
    


def wilson(n):
    """
    Implementaión del test de primalidad de Wilson, basado en el teorema de Wilson,
    (p-1)! ≡ -1 mod p
    :param n: El número a determinar su primalidad.
    :return: True si n es primo, False en otro caso.
    """
    result=1
    for i in range(2,n):
        result=(result*i)%n
    if(result is ((-1)% n)):
        return True
    return False

def generate_prime(size=None):
    """
    Genera un primo de al menos $size dígitos, si no se especifica,
    este tiene que asegurar que al menos tiene 100 dígitos.

    :param size: El tamaño del primo a generar.
    :return: Un número que se asegura que es primo.
    """
    if(size is not None):
        size=100
    while True:
        prime_candidate=big_int(size)
        if wilson(prime_candidate):
           return prime_candidate 
    
