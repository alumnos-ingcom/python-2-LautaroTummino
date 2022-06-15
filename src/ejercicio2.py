################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Estadísticas
Implementar una función que obtenga los máximos,
mínimos y promedio de una secuencia con números,
retornando los valores como una tuple.
Sin utilizar lazos for o las funciones integradas del lenguaje que procesan secuencias.
"""


def maximo_tupla(notas):
    """
    Esta función se encarga de determinar el valor maximo de una lista numérica
    Precondición: Ingresar una lista o tupla numérica
    Postcondición: Mostrar en pantalla el numero mayor
    """
    #notas = list(notas)
    rango = 0
    longitud = len(notas)
    mayor = notas[0]
    while rango < longitud:
        if notas[rango] > mayor:
            mayor = notas[rango]
        rango += 1
    return mayor


def minimo_tupla(notas):
    """
    Esta función se encarga de determinar el valor minimo de una lista númerica
    Precondición: Ingresar una lista o tupla númerica
    Postcondición: Mostrar en pantalla el numero menor
    """
    #notas = list(notas)
    rango = 0
    longitud = len(notas)
    menor = notas[0]
    while rango < longitud:
        if notas[rango] < menor:
            menor = notas[rango]
        rango +=1
    return menor


def sumando_tupla(notas):
    """
    Esta función se encarga de sumar todos los valores de una lista númerica
    Precondición: Ingresar una lista o tupla númerica
    Postcondición: Mostrar la suma de todos los números
    """
    total = 0
    sumando = 0
    longitud =len(notas)
    rango = 0
    while rango < longitud:
        sumando += notas[rango]
        rango += 1
        total = sumando     
    return total
    

def promedio_tupla(notas):
    """
    Esta función se encarga de determinar el promedio de una lista numérica
    llamando a la función suma, para luego realizar la division por la cantidad
    de numeros ingresados en la lista
    Precondición: Ingresar una lista o tupla númerica
    Postcondición: Mostrar el promedio de los números ingresados
    """
    maximo = maximo_tupla(notas)
    minimo = minimo_tupla(notas)
    sumando = sumando_tupla(notas)
    cantidad_notas=len(notas)
    prome = sumando / cantidad_notas
    return prome


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    Esta función tiene un problema, y aun no logro resolverla, cuando la utilizo
    en future coder, y el argumento se lo indico mediante listas o tuplas
    el programa funcióna, cuando lo traigo a thony y intento que el usuario
    ingrese un número me da un error que estoy sumando STR con INT pero no logro
    encontrar la solución. 
    """
    notas = (2,1,5)
    maxi = maximo_tupla(notas) 
    mini = minimo_tupla(notas)
    sumando = sumando_tupla(notas)
    promediar = promedio_tupla(notas)
    print((mini,maxi,sumando,promediar))


if __name__ == "__main__":
    principal()
