import math
from random import randint
#Saca el valor 2-adico del número n
def get2adicVal(n): 
    val = 0
    num = n
    while (num % 2 == 0):
        val = val + 1
        #floor division
        num = num // 2
    return val

#Obtenemos una base a, donde gcd(a,n) = 1
def getA(n):
    if n <= 4: 
        return n
    r = randint(2,n-2)
    while math.gcd(r,n) != 1:
        r = randint(2,n-2)
    return r

#Verificamos si un número es congruente con otro modulo n
def congruentWithBMod(a,b,mod):
    return (a) == (b % mod)
def prime_relative(a, b):
    if(b == 0):
        return a == 1
    else:
        return prime_relative(b, a%b)
'''Máximo común divisor entre dos enteros a y b'''
def mcd(a, b):
    	resto = 0
	while(b > 0):
		resto = b
		b = a % b
		a = resto
	return a
'''Función que obtiene el inverso multiplicativo modular de a módulo m'''
def modInverse(a, m) : 
    a = a % m; 
    for x in range(1, m) : 
        if ((a * x) % m == 1) : 
            return x 
    return 1
