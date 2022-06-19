################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio2 import maximo_tupla, minimo_tupla, sumando_tupla, promedio_tupla

"""
Se prueban unitariamente cada funcion que contiene el archivo original
maximo,minimo,promedio y suma.
"""


def test_maximo_tupla():
    """
    Esta función testeara la funcion de num maximo en secuencia numerica
    """
    notas = 2,10,11
    resultado = maximo_tupla(notas)
    assert isinstance(resultado, int), "El resultado debe ser el numero mayor"


def test_minimo_tupla():
    """
    Esta función testeara la funcion de num minimo en secuencia numerica
    """
    notas = "2,4,1,10,15"
    resultado = minimo_tupla(notas)
    assert isinstance (resultado, str), "El resultado debe ser un número entero"
    assert resultado == notas[6], "El menor es 1"


def test_sumando_tupla():
    """
    Esta funcion se encarga de testear la suma de toda una secuencia numerica
    """
    notas = "10,10,9"
    resultado = sumando_tupla(notas)
    assert isinstance (resultado, float), "El resultado es un valor entero"
    assert resultado == 29.0, "La suma de los numeros es de 29"


def test_promedio_tupla():
    """
    Esta funcion testea si el promedio de una secuencia numerica
    """
    notas = "9,9,9"
    resultado = promedio_tupla(notas)
    assert isinstance (resultado, float), "El resultado es un valor decimal"
    assert resultado == 9.0, "El promedio es 9.0"
