import unittest


def doblar(n):
    return n * 2


def suma(a, b):
    return a + b


def es_par(n):
    return True if n % 2 == 0 else False


class Pruebas (unittest.TestCase):
    def test_doblar(self):
        self.assertEqual(doblar(2), 4)
        self.assertEqual(doblar('Ab'), 'AbAb')

    def test_suma(self):
        self.assertEqual(suma(-15, 15), 0)
        self.assertEqual(suma('Ab', 'cd'), 'Abcd')

    def test_es_par(self):
        self.assertTrue(es_par(2), True)
        self.assertFalse(es_par(3), False)


if __name__ == '__main__':
    unittest.main()
