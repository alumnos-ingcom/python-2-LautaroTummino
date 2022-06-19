################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio6 import cifrado_cesar, decifrado_cesar

"""
Estos testeos son los encargados de corroborar que la función cumple su trabajo
le pasamos como argumento "hola" a la funcion de cifrado, para que la transofmer
en "lspe", y luego la comparamos con el mensaje1
"""


def test_cifrado_cesar():
    """
    Esta función testeara ls funcion de pares e impares positivos, ejercicio N°1
    """
    mensaje = "hola"
    resultado = cifrado_cesar(mensaje)
    mensaje1 = "lspe"
    resultado1 = decifrado_cesar(mensaje1)
    assert isinstance(resultado, str), "El resultado debe ser str con el mensaje cifrado"
    assert mensaje == resultado1, "Es igual al decifrar el mensaje"


def test_decifrado_cesar():
    """
    Esta función testeara ls funcion de pares e impares positivos, ejercicio N°1
    """
    mensaje = "lspe"
    resultado = decifrado_cesar(mensaje)
    mensaje1= "hola"
    assert isinstance(resultado, str), "El resultado debe ser str con el mensaje decifrado"
    assert resultado == mensaje1, "Decifrar mensaje"
    assert mensaje != resultado, "Deben ser distintos"
