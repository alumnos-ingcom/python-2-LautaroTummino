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
    Esta función se encarga de encontrar el n-esimo número
    de una secuencia númerica, siempre y cuando el número sea mayor a 2
    Precondicion: Ingresar un número mayor a 2
    Postcondicion: Imprimir por pantalla el n-esimo termino.
    """
    if num < 2:
        print("Error, Intente con un numero mayor a 2")
    else:
        ant = num - 1
        total = ant + num
        result = []
        while total < 1550000:
            total = ant + num
            ant = num
            num = total
            result = result + [num]
    return result[8]


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    num = int(input("Ingrese un número N mayor que 2: "))
    fibo = fibonacci(num)
    print(f"El n-esimo termino es: {fibo}")


if __name__ == "__main__":
    principal()
