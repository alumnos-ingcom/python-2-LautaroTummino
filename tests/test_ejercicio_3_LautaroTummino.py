################
# Lautaro Tummino - @LautaroTummino
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from practica.ejercicio3 import compara_cadenas

"""
Se prueban los casos en donde las dos cadenas sean iguales
"hola" y "hola" la tuple debe contener la cantidad de superposiciones
en que caracteres, y el numero 1 indicando que existe algun tipo de superposicion
tambien un caso de prueba en donde las dos candeas sean distintas
"""


def test_compara_cadenas():
    """
    Esta función testeara la funcion de comparar cadenas
    """
    cadena_uno = "hola"
    cadena_dos = "hola"
    resultado = compara_cadenas(cadena_uno, cadena_dos)
    assert isinstance(resultado, tuple), ("El resultado debe ser una tupla"
    "que diga si hay superposición, si la hay cuantos caracteres se superponen"
    "y en donde")
    assert cadena_uno == cadena_dos, ("La superposicion es: 1, por que las"
                                " cadenas sesuperponen un total de 4 vez/veces"
                                    " en los caracteres: [0, 1, 2, 3]")
    cadena_uno = "perro"
    cadena_dos = "gato"
    result = compara_cadenas(cadena_uno, cadena_dos)
    assert isinstance(resultado, tuple), "El resultado debe ser una tupla"
    assert result is 0 , "Resutlado 0 no hay superposicion"
