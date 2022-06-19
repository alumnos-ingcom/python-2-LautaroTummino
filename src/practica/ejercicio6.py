################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
6. El Cifrado del Cesar
El cifrado César o cifrado de rotación usa una
encriptación de sustitución simple.
Esto significa que cada caracter se sustituye
por otro caracter de acuerdo con un sistema especifico.
La codificación debe ser tal que la palabra codificada contenga
unicamente caracteres del tipo AZaz y 0 a 9, de manera que al codificar las
ultimas letras del abecedario se vuelva a las primeras letras.
Por ejemplo, el método conocido y muy utilizado ROT13
rota el alfabeto con 13 posiciones, resultando en A->N, B->O... Y->L y Z->M.

Implementar una funcion que codifique un texto rotandolo
una cantidad de posiciones ajustable.
Implementar la funcion que decodifique el texto rotado
una cantidad de posiciones ajustable.
Una buena forma para verificar este ejercicio es codificar
y decodificar un texto y compararlo con lo que fué ingresado originalmente.
Tip: Implementar las funciones utilizando las funciones ord y chr.
"""


def cifrado_cesar(mensaje):
    """
    Esta función se encarga de cifrar un mensaje se pueden utilizar MAYUSCULAS
    pero el programa no distingue entre acentos y números.
    Precondicion: Ingresar un mensaje para cifrar
    Postoncidicon: Print del mensaje cifrado, con una rotacion de 4 posiciones
    por letra.
    """
    dic = "abcdefghijklmnopqrstuvwxyz"
    clave = 4
    cifrado = ""
    for letra in mensaje.lower():
        if letra in dic:
            indice = dic.find(letra)
            indice += clave
            if indice >= 26:
                indice -= 26
            cifrado += dic[indice]
        else:
            cifrado += letra
    return cifrado


def decifrado_cesar(mensaje):
    """
    Esta función se encarga de decifrar un mensaje se pueden utilizar MAYUSCULAS
    pero el programa no distingue entre acentos y números.
    Precondicion: Ingresar un mensaje para decifrar
    Postoncidicon: Print del mensaje decifrado con una rotacion de 4 posiciones
    por letra.
    """
    dic = "abcdefghijklmnopqrstuvwxyz"
    clave=4
    cifrado =""
    for letra in mensaje.lower():
        if letra in dic:
            indice = dic.find(letra)
            indice -= clave
            if indice <=0:
                indice +=26
            if indice >=26:
                indice -=26
            cifrado += dic[indice]
        else:
            cifrado += letra
    return cifrado



def principal():
    """
    Esta función es la que se encarga de la parte 'interactiva' del ejercicio
    (La entrada, la llamada al algoritmo y la salida)
    """
    mensaje = input("Ingrese un mensaje: ")
    cifrando = cifrado_cesar(mensaje)
    print(f"{cifrando}")
    mensaje = input("Ingrese el mensaje cifrado: ")
    decifrando = decifrado_cesar(mensaje)
    print(f"{decifrando}")


if __name__ == "__main__":
    principal()
