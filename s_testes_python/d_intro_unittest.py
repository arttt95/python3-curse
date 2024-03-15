"""
Introdução ao módulo Unittest

Unittest -> Testes Unitários

O que são testes unitários?

Testes unitário é a forma de se testar unidades individuais de código fonte.

Unidades inidividuais podem ser: funções, métodos, classes, módulos etc.

# OBS: Teste unitário não é específico da linguagem Python.

Para criarmos nossos testes, criamos classes que herdam de unittest. TestCase
e a partir de então ganhamos todos os 'assertions' presentes no módulo.

Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de teste para sua unidade

# Conhecendo as assertions

Método                        Checa se

assertEqual(a, b)             a == b
assertNotEqual(a, b)          a != b
assertTrue(x)                 x é True
asserFalse(x)                 x é False
assertIs(a, b)                a é b
assertIsNot(a, b)             a não é b
assertIsNone(x)               x é None
assertIsNotNone(x)            x não é None
assertIn(a, b)                a está em b
assertNotIn(a, b)             a não está em b
assertIsInstance(a, b)        a é uma instância de b
assertNotIsInstance(a, b)     a não é uma instância de b

Por convenção, todos os testes em um test case, devem ter seu nome
iniciado com test_unidadeasertestada

# Para executar os testes com unittest

python nome_do_modulo_de_teste.py

# Para executar os testes com unittest no modo verbose

python nome_do_modulo_de_teste.py -v

Docstrings nos testes

Podemos acrescentar (E É RECOMENDADO) que coloquemos Docstrings nos nossos testes.
"""

# Prática - Utilizando a abordagem TDD

