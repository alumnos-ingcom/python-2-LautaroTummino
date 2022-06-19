################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Súper-puestos
Desarrollar una función que
indique el grado de superposición
entre dos listas. Siendo 0 sin
superposición y uno para cada elemento superpuesto.
['H', 'o', 'l', 'a', ' ', 'M', 'u', 'n', 'd', 'o']
y
['H', 'o', 'l', 'a']
Tienen una superposición de cuatro elementos.
Extra #1
Indicar en lugar de la cantidad
de caracteres superpuestos, la posicion de inicio
de la superposición.
"""


def compara_cadenas(cadena_uno, cadena_dos):
    """
    Esta función se encarga de comparar la superposición en dos cadenas
    mostrando una tupla con la cantidad de veces que se superponen, en que
    caracteres se superponen, y mostrando 1 si hay superposicion y 0 si no
    la hay.
    Precondicion: ingresar dos cadenas de texto
    Postcondicion: Muestra tupla con los valores de la comparación
    """
    cadena=list(cadena_uno)
    cadena1=list(cadena_dos)
    cantidad = 0
    total = []
    superposicion = 0
    i = 0
    while i < len(cadena_uno) and i < len(cadena_dos):
        if cadena_uno[i] == cadena_dos[i]:
            superposicion = 1
            cantidad += 1
            total = total + [i]
            msg = (superposicion,cantidad,total)
        else:
            superposicion = 0
            msg = (superposicion)          
        i += 1
    return msg


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena_uno = str(input("Ingrese una cadena"))
    cadena_dos = str(input("Ingrese una cadena"))
    compara = compara_cadenas(cadena_uno, cadena_dos)
    print(f"{compara}")


if __name__ == "__main__":
    principal()
