################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
1. Pares e impares
Escribir una función que retorne True
cuando un número entero es par y False
cuando no lo sea, sin utilizar módulo. (%)
"""


def par_e_impar(numero):
    """
    Esta función se encarga de determinar si un número es par o impar.
    Precondicion: Se espera un número entero
    Postcondicion: Se devuelve un valor booleano, True para pares False para impares
    """
    mitad = numero // 2
    suma = mitad + mitad
    if suma == numero:
        resultado=bool(True)
    else:
        resultado=bool(False)
    return resultado


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    entrada = 20
    resultado = par_e_impar(numero)
    salida = un valor booleano
    """


if __name__ == "__main__":
    principal()
