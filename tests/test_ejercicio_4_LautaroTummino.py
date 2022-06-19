################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio4 import fibonacci

"""
Esta función se encarga de corroborar que el n-esimo termino sea el correcto
como argumento le pasamos el número 9 de la susceción y el resultado debe ser
34.
"""


def test_fibonacci():
    """
    Esta función testeara la funcion de fibonacci
    """
    num = 9
    resultado = fibonacci(num)
    assert isinstance(resultado, int), "El resultado debe ser un N entero"
    assert resultado == 34, "Resultado del n-esimo termino"
    assert resultado > 0, "El resultado debe ser mayor a 0"
