import unittest
from s_testes_python.testes.robo import Robo


class RoboTestes(unittest.TestCase):

    def setUp(self):
        self.megaman = Robo('Mega Man', bateria=50)
        print('setUp() sendo executado...')

    def test_carregar(self):
        self.megaman.carregar()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(), f'BEEP BOOP BEEP BOOP. '
                                                    f'Eu sou o MEGA MAN.')
        self.assertEqual(self.megaman.bateria, 49, 'A bateria deveria ter'
                                                   'descarregado 1% e chegado a 49.')

    def tearDown(self):
        print('tearDown() sendo executado...')


if __name__ == '__main__':
    unittest.main()
