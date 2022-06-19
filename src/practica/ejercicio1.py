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


def es_par_es_impar(numero):
    """
    Esta función se encarga de determinar si un número entero es par o impar.
    Precondicion: Se espera un número entero
    Postcondicion: Se devuelve un valor booleano, True para par False para impar
    """
    mitad = numero // 2
    suma = mitad + mitad
    if suma == numero:
        return True
    else:
        return False



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    numero = int(input("Ingrese un número: "))
    resultado = es_par_es_impar(numero)
    print(f"{resultado}")


if __name__ == "__main__":
    principal()
