import unittest


# TDD - Test-driven development. ->
#   BDD - Behaviour driven development - Outside-in TDD - Mocks
# Inside-out TDD VS Outside-in TDD

# Paso 1: Definir una buena lista de requisitos - Piensa primero cobarde.
##
# Design principles: Less Astonishment/Surprise Principle
# ToDo list:
# La coma es el separador de numeros en las expresiones.
# None -> 0
# "" -> 0
# "8" -> 8
# "1,1" -> 2
# "2,10" -> 12
# "1,a" ->  1
# "a" -> 0
# "1,a,2" -> 3
# "1a,2" -> 2
# "1,2,3" -> 6

# "//#/3#2" -> 5
# "//#/3,2" -> 0
# "//%/1%2%3" -> 6


# Paso 2: escribir el test primero
# Paso 3: ejecutar TODOS los tests y ver que el ultimo falla
# Paso 4: escribir el codigo MINIMO/mas simple para que el test pase
# Paso 5: ejecutar todos los tests y ver si todos siguen pasando
# Paso 6: refactoring
# Paso 7: Repetir
from string_calculator import sum_numbers_in


class StringCalculatorTests(unittest.TestCase):
    def test_none_and_empty_compute_as_zero(self):
        self.assertEqual(sum_numbers_in(""), 0)
        self.assertEqual(sum_numbers_in(None), 0)

    def test_numbers_in_expression_are_converted_to_integers(self):
        self.assertEqual(sum_numbers_in("8"), 8)

    def test_numers_in_expression_are_separated_by_commas(self):
        self.assertEqual(sum_numbers_in("1,4"), 5)
        self.assertEqual(sum_numbers_in("1,4,1"), 6)

    def test_non_numeric_symbols_are_evaluated_as_zeros(self):
        self.assertEqual(sum_numbers_in("10,a"), 10)
        self.assertEqual(sum_numbers_in("a"), 0)
        self.assertEqual(sum_numbers_in("1a,2"), 2)
