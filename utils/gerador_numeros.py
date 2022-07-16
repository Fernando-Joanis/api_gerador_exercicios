import random


def gerando_numeros(intervalo1, intervalo2):
    fator1 = random.randint(intervalo1, intervalo2)
    fator2 = random.randint(intervalo1, intervalo2)
    return fator1, fator2
