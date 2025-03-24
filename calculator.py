import math

# lógica calculadora

def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return "Erro Divisão por zero!"
    return a / b

def raiz(a):
    return math.sqrt(a)

def potencia(a,b):
    return a ** b

def modulo(a,b):
    return a % b

def fatorial(a):
    if a == 0:
        return 1
    else:
        return a * fatorial((a-1))

import math
def logaritmo(a, b):
    return math.log(b, a)  # b é o número, a é a base

def absoluto(a):
    return abs(a)

def arredondar(a, casas_decimais=0):
    return round(a, casas_decimais)

def raiz_n(a, n):
    return a ** (1 / n)





