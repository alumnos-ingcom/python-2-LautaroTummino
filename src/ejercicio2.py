"""
2. Estadísticas
Implementar una función que obtenga los máximos,
mínimos y promedio de una secuencia con números,
retornando los valores como una tuple.
Sin utilizar lazos for o las funciones integradas del lenguaje que procesan secuencias.
"""


def maximo(notas):
    """
    Esta función se encarga de determinar el valor maximo de una lista númerica
    Precondicion: Ingresar una lista de números [1,2,5,8,9]
    Postcondicion: Regresar el número mayor [9]
    """
    longi=len(notas)
    mayor=notas[0]
    i=0
    notas = notas
    while i < longi:
        if notas[i] > mayor:
            mayor = notas[i]
        i+=1
    return mayor


def minimo(notas):
    """
    Esta función se encarga de determinar el valor minimo de una lista númerica
    Precondicion: Ingresar una lista de números [1,2,5,8,9]
    Postcondicion: Regresar el número mayor [1]
    """
    longi=len(notas)
    menor=notas[0]
    i=0
    resultado= []
    while i < longi:
        if notas[i] < menor:
            menor = notas[i]
        i+=1
    return menor


def suma(notas):
    """
    Esta función se numar todos los numeros dentro de una lista
    Precondicion: Ingresar una lista númerica
    Postcondicion : El resultado de la suma de los numeros
    """
    suma = (0)
    rango = len(notas)
    contador = (0)
    while contador < rango:
        suma = suma + notas[contador]
        contador = contador + 1
        resultado = (suma)
    return resultado




def promedio(notas):
    """
    Esta función encarga de hacer un promedio de toda una lista numerica, sumando
    todos los numeros ingresados, y dividiendo por la misma cantidad de números
    Precondicion: Ingresar una lista númerica
    Postcondicion : El resultado de la suma de los numeros
    """
    cantidad_notas=len(notas)
    prome = suma(notas) / cantidad_notas
    result = prome
    return result

def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    notas=tuple(input("Ingrese una lista númerica ejemplo: [1,2,9,10]"))
    maxi = maximo(notas)
    mini = minimo(notas)
    print(maxi)
    



if __name__ == "__main__":
    principal()

