################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
5. Corchetes balanceados
Implementar una función que determine si
una cadena con corchetes está balanceada.
Es decir, si cada corchete que abre, tiene su par que cierra.
El resultado debe ser un valor lógico indicando si esta o no balanceado.
"""


def corchetes_balanceados(cadena):
    """
    Esta función se encarga de corroborar si todos los: '(' '{' '[' que se abren
    en una cadena se cierran ')' ']' '}'. Retornando True si sucede, False si no.
    Aun no logro que ignore todos los caracteres, si le pasamos una cadena sin
    corchetes, el resultado va a ser TRUE cuando debria ser FALSE
    Precondicion: Ingresar una cadena de caracteres con llaves, parentesis
    o corchetes ej: (hola), ]hola(.
    Postcondicion: Retornar un valor booleano, True si cierran False si no.
    """
    contador = 0
    sumador = 0
    cont = 0
    for elemento in cadena:
        if elemento == "(":
            contador += 1
        if elemento == ")":
            contador -= 1
        if elemento == "[":
            sumador += 1
        if elemento == "]":
            sumador -= 1
        if elemento == "{":
            cont += 1
        if elemento == "}":
            cont -= 1
        if contador < 0 or sumador < 0 or cont < 0:
            return False
    if contador == 0 and sumador == 0 and cont == 0:
        return True
    else:
        return False


def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    cadena = input("Ingrese untexto con (, ] o {")
    corroborando = corchetes_balanceados(cadena)
    print(corroborando)


if __name__ == "__main__":
    principal()
