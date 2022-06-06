################
# LautaroTummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
2. Estadísticas
Implementar una función que obtenga los máximos,
mínimos y promedio de una secuencia con números, retornando los valores como una tuple.
Sin utilizar lazos for o las funciones integradas del lenguaje que procesan secuencias.
"""


def maximo(notas):
    longi=len(notas)
    mayor=notas[0]
    i=0
    while i < longi:
        if notas[i] > mayor:
            mayor = notas[i]
            resultado = mayor
        i+=1
    return resultado


def minimo(notas):
    longi=len(notas)
    menor=notas[0]
    i=0
    while i < longi:
        if notas[i] < menor:
            menor = notas[i]
            resultado = menor
        i+=1
    return resultado
    

def suma(notas):
    suma = 0
    rango = len(notas)
    contador = 0
    while contador < rango:
        suma = suma + notas[contador]
        contador = contador + 1
        resultad = suma
    return resultad


def promedio(notas):
    cantidad_notas=len(notas)
    prome = suma(notas) / cantidad_notas
    result = prome
    return result

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    entrada = []
    num_max = maximo(notas)
    num_min = minimo(notas)
    num_suma = suma(notas)
    num_promedio = promedio(notas)
    print(f"{(maximo, minimo, suma, promedio)}")
    """

if __name__ == "__main__":
    principal()
