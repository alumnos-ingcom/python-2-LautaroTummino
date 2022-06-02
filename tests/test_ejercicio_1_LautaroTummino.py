################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from src.ejercicio1.py import par_e_impar

"""
Describir aquí que es lo que se esta probando.
Tengan en cuenta que el archivo tiene que llamarse igual
que el archivo a probar agregando antes `test_`
"""


def test_par_e_impar_positivos():
    """
    Esta función testeara ls funcion de pares e impares, ejercicio N°1
    """
    numero = 10
    resultado = par_e_impar(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano
    assert resultado == True "True por que numero es primo"


def test_par_e_impar_negativos():
    """
    Esta función testeara ls funcion de pares e impares, ejercicio N°1
    """
    numero = -15
    resultado = par_e_impar(numero)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano
    assert resultado == False "False por que no lo es"

    
