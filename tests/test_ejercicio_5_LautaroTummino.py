################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio5 import corchetes_balanceados

"""
Este testo es el encargado de testear dos casos de prueba, en donde el primer
resultado es falso, ya que los corchetes no estan balanceados, y el segundo es
True ya que se encuentran balanceados.
"""


def test_corchetes_balanceados():
    """
    Esta función testeara la funcion de fibonacci
    """
    cadena = "(()"
    resultado = corchetes_balanceados(cadena)
    cadena_uno = "()"
    resultado_uno = corchetes_balanceados(cadena_uno)
    assert isinstance(resultado, bool), "El resultado debe ser un valor booleano"
    assert resultado is False, "Resultado Falso se abren corchetes y no cierran"
    assert resultado_uno is True, "Esta balanceado"