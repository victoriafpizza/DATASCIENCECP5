import unittest
import numpy as np
from memory_profiler import profile

from strassen import strassen
from winograd import winograd
from karatsuba import karatsuba_matrix
from multiplicacao_tradicional import multiplicar_matrizes_tradicional

class TesteMultiplicacaoTradicional(unittest.TestCase):

    def teste_matrizes_pequenas(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        resultado_esperado = np.array([[19, 22], [43, 50]])
        resultado_obtido = multiplicar_matrizes_tradicional(A, B)
        self.assertTrue(np.allclose(resultado_obtido, resultado_esperado))

    def teste_matrizes_grandes(self):
        A = np.random.rand(100, 100)
        B = np.random.rand(100, 100)
        resultado_esperado = np.dot(A, B)
        resultado_obtido = multiplicar_matrizes_tradicional(A, B)
        self.assertTrue(np.allclose(resultado_obtido, resultado_esperado))

    def teste_matrizes_identidade(self):
        A = np.identity(100)
        B = np.random.rand(100, 100)
        resultado_esperado = B
        resultado_obtido = multiplicar_matrizes_tradicional(A, B)
        self.assertTrue(np.allclose(resultado_obtido, resultado_esperado))

class TesteStrassen(unittest.TestCase):

    def teste_matrizes_pequenas(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        resultado_esperado = np.array([[19, 22], [43, 50]])
        resultado_obtido = strassen(A, B)
        self.assertTrue(np.allclose(resultado_obtido, resultado_esperado))

    def teste_matrizes_grandes(self):
        A = np.random.rand(100, 100)
        B = np.random.rand(100, 100)
        resultado_esperado = np.dot(A, B)
        resultado_obtido = strassen(A, B)
        self.assertTrue(np.allclose(resultado_obtido, resultado_esperado))

    def teste_matrizes_identidade(self):
        A = np.identity(100)
        B = np.random.rand(100, 100)
        resultado_esperado = B
        resultado_obtido = strassen(A, B)
        self.assertTrue(np.allclose(resultado_obtido, resultado_esperado))

class TesteWinograd(unittest.TestCase):

    def teste_matrizes_pequenas(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        resultado_esperado = np.array([[19, 22], [43, 50]])
        resultado_obtido = winograd(A, B)
        self.assertTrue(np.allclose(resultado_obtido, resultado_esperado))

    def teste_matrizes_grandes(self):
        A = np.random.rand(100, 100)
        B = np.random.rand(100, 100)
        resultado_esperado = np.dot(A, B)
        resultado_obtido = winograd(A, B)
        self.assertTrue(np.allclose(resultado_obtido, resultado_esperado))

    def teste_matrizes_identidade(self):
        A = np.identity(100)
        B = np.random.rand(100, 100)
        resultado_esperado = B
        resultado_obtido = winograd(A, B)

from karatsuba import karatsuba_matrix

class TesteKaratsuba(unittest.TestCase):

    def teste_matrizes_pequenas(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[5, 6], [7, 8]])
        resultado_esperado = np.array([[19, 22], [43, 50]])
        resultado_obtido = karatsuba_matrix(A, B)
        self.assertTrue(np.allclose(resultado_obtido, resultado_esperado))

    def teste_matrizes_grandes(self):
        A = np.random.rand(100, 100)
        B = np.random.rand(100, 100)
        resultado_esperado = np.dot(A, B)
        resultado_obtido = karatsuba_matrix(A, B)
        self.assertTrue(np.allclose(resultado_obtido, resultado_esperado))

    def teste_matrizes_identidade(self):
        A = np.identity(100)
        B = np.random.rand(100, 100)
        resultado_esperado = B
        resultado_obtido = karatsuba_matrix(A, B)
        self.assertTrue(np.allclose(resultado_obtido, resultado_esperado))