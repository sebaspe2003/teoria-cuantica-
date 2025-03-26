import numpy as np


def convertir_complejo(num):
    n = complex(num)
    real = np.real(n)
    imaginario = np.imag(n)
    return real, imaginario


def probabilidad(vect, pos):
    vector = np.array(vect)
    i = int(pos)
    a, b = convertir_complejo(vector[i])
    numerador = (a ** 2 + b ** 2)
    denominador = 0

    for j in range(len(vector)):
        x, y = convertir_complejo(vector[j])
        d = (a ** 2 + b ** 2)
        denominador += d

    return numerador / denominador


def main():
    print(probabilidad([2 + 1j, -3j, 4], 1))


main()
