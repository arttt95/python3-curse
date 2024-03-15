import unittest

from s_testes_python.testes.atividades import comer, dormir, eh_engracada


class AtividadeTestes(unittest.TestCase):

    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável."""
        self.assertEqual(
            comer(comida='quiabo', eh_saudavel=True),
            'Estou comendo quiabo porque quero ficar em forma.'
        )

    def test_comer_besteira(self):
        """Testando o retorno com comida não saudável."""
        self.assertEqual(
            comer(comida='pizza', eh_saudavel=False),
            'Estou comendo pizza porque só se vive uma vez.'
        )

    def test_dormir_pouco(self):
        """Testando o retorno para quantidade baixa de horas de sono."""
        self.assertEqual(
            dormir(qtd_horas=4),
            'Continuo cansado porque dormi apenas 4 horas.'
        )

    def test_dormir_bastante(self):
        """Testando o retorno com qantidade alta de horas de sono."""
        self.assertEqual(
            dormir(qtd_horas=10),
            'Estou atrasado porque dormi demais.'
        )

    def test_not_eh_engracada(self):
        """Testando o retorno de uma pessoa que não é engraçada."""
        # self.assertEqual(eh_engracada('Fábio Porchat'), False)
        self.assertFalse(eh_engracada('Fábio Porchat'))

    def test_is_eh_engracada(self):
        """Testando o retorno para uma pessoa que realmente é engraçada."""
        self.assertTrue(
            eh_engracada('Jim Carrey'),
            'Jim Carrey deveria ser engraçado')


if __name__ == '__main__':
    unittest.main()
