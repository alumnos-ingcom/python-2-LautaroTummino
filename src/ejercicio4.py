################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
4. Fibonacci
La sucesión de Fibonacci es una sucesión infinita donde cada
elemento es la suma de los dos anteriores.
En la misma, los dos primeros términos son 1.
(En algunos lugares se toma el primer término en 0 y el segundo en 1)
Implementar una función que permita obtener el n-esimo termino de la
sucesión de Fibonacci. Siendo este número un entero positivo mayor a 2.
"""


def fibonacci(num):
    """
    Esta función se encarga de encontrar el n-esimo valor
    de una sucesión fibonacci
    Precondicion: Ingresar un número > 2 siendo este valor a corrobora
    en la sucesión. 
    Postcondicion: Imprimir por pantalla el n-esimo termino.
    """
def fibonacci(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    num = int(input("Ingrese un número: "))
    fibo = fibonacci(num)
    print(f"El n-esimo termino es: {fibo}")


if __name__ == "__main__":
    principal()
