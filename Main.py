import Prova01 as p1
import Prova02 as p2

import unittest  



class TestProvaEscrita01(unittest.TestCase):
    """Tests per a Prova Escrita 01 (excepte Exercicis 1 i 5)"""

    def setUp(self):
        self.videojocs = p1.videojocs
        self.biblioteca = []

    def test_buscar_per_titol(self):
        self.assertIsNotNone(p1.buscar_per_titol("Cyberpunk 2077", self.videojocs))
        self.assertIsNone(p1.buscar_per_titol("Joc Inexistent", self.videojocs))

    def test_afegir_a_biblioteca(self):
        self.assertEqual(p1.afegir_a_biblioteca("FIFA 24", self.videojocs, self.biblioteca), "oc afegit!")
        self.assertEqual(p1.afegir_a_biblioteca("FIFA 24", self.videojocs, self.biblioteca), "Ja està a la biblioteca")
        self.assertEqual(p1.afegir_a_biblioteca("Joc Inexistent", self.videojocs, self.biblioteca), "oc no trobat")

    def test_joc_mes_car(self):
        joc_car = p1.joc_mes_car(self.videojocs)
        self.assertEqual(joc_car["titol"], "FIFA 24")


class TestProvaEscrita02(unittest.TestCase):
    """Tests per a Prova Escrita 02 (excepte Exercicis 5 i 6)"""

    def test_crear_sequencia(self):
        self.assertEqual(p2.crear_sequencia(5, 10), [5, 6, 7, 8, 9, 10])
        self.assertEqual(p2.crear_sequencia(10, 5), [])
        self.assertEqual(p2.crear_sequencia(-2, 5), [])

    def test_numeros_senars_majors(self):
        llista = [3, -1, 7, 2, -1, 9, 4, 7]
        self.assertEqual(p2.numeros_imparells_majors(llista, 3), [7, 9, 7])
        self.assertEqual(p2.numeros_imparells_majors([], 3), [])

    def test_primera_posicio(self):
        llista = [3, -1, 7, 2, -1, 9, 4, 7]
        self.assertEqual(p2.primera_posicio(llista, 7), 2)
        self.assertEqual(p2.primera_posicio(llista, 15), -1)
        self.assertEqual(p2.primera_posicio([], 5), -1)

    def test_diagonal_principal(self):
        matriu = [[1,2,3],[4,5,6],[7,8,9]]
        matriu_no_quadrada = [[1,2],[3,4,5]]
        self.assertEqual(p2.diagonal_principal(matriu), [1,5,9])
        self.assertEqual(p2.diagonal_principal(matriu_no_quadrada), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)  # no me ha quedado claro como funciona el verbosity=2