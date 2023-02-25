import unittest


class PruebasMetodosCadenas (unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
    
    def test_split(self):
        s = 'hola mundo'
        self.assertEqual(s.split(), ['hola', 'mundo'])
        # Chequea que s.split lance una excepción cuando el separador no es una cadena
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
