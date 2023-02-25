import unittest

from calculadora import Calculadora


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_inicial_valor(self):
        calc = Calculadora()
        self.assertEqual(calc.valor, 0)

    def test_suma(self):
        self.calc.suma(1, 3)
        self.assertEqual(self.calc.valor, 4)
