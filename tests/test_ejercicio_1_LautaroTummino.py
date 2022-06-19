################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio1 import es_par_es_impar

"""
Se realiza una prueba de un numero entero positivo par,
y tambien se realiza el mismo caso de prueba pero con un numero negativo
"""


def test_es_par_es_impar_positivos():
    """
    Esta función testeara ls funcion de pares e impares positivos, ejercicio N°1
    """
    numero = 10
    resultado = es_par_es_impar(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is True, "True el numero es primo"


def test_es_par_es_impar_negativos():
    """
    Esta función testeara las funcion de pares e impares negativos, ejercicio N°1
    """
    numero = -15
    resultado = es_par_es_impar(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is False, "False no lo es"
