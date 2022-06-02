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
    Precondicion: Se espera un número entero positivo
    Postcondicion: Se devuelve un valor booleano, True o False
    """
    mitad = numero // 2
    suma = mitad + mitad
    if suma == numero:
        return(True)
    else:
        return(False)


(par_e_impar(25))


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