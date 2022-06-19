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
    Esta función se encarga de determinar el valor maximo de una secuencia
    numérica.
    Precondición: Ingresar una secuencia numérica: "2,4,5,10"
    Postcondición: Mostrar en pantalla el numero mayor
    """
    #notas = notas.split(",")
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
    Esta función se encarga de determinar el valor minimo de una secuencia númerica
    Precondición: Ingresar una secuencia de numeros "2,4,5,6,10"
    Postcondición: Mostrar en pantalla el numero menor
    """
    notas = notas.split(",")
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
    Esta función se encarga de sumar todos los valores de una secuencia númerica
    Precondición: Ingresar una secuencia numerica "2,10,9,8,7"
    Postcondición: Mostrar resultado de la suma de todos los números  
    """
    notas = notas.split(",")
    total = 0
    sumando = 0
    longitud =len(notas)
    rango = 0
    while rango < longitud:
        sumando += float(notas[rango])
        rango += 1
        total = sumando
    return total


def promedio_tupla(notas):
    """
    Esta función se encarga de determinar el promedio de una secuencia numérica
    llamando a la función suma, para luego realizar la division por la cantidad
    de numeros ingresados en la secuencia.
    Precondición: Ingresar una secuencia numerica
    Postcondición: Mostrar el promedio de los números ingresados
    """  
    sumando = sumando_tupla(notas)
    cantidad_notas= notas.split(",")
    return sumando / len(cantidad_notas)


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    notas = input("Ingrese una secuencia numerica, ej 2,5,10 : ")
    maxi = maximo_tupla(notas) 
    mini = minimo_tupla(notas)
    sumando = sumando_tupla(notas)
    promediar = promedio_tupla(notas)
    print((mini,maxi,sumando,f"{promediar:.2f}"))


if __name__ == "__main__":
    principal()
