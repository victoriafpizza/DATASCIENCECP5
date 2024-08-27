import numpy as np

num_operacoes = 0

def karatsuba_matrix(A, B):
  """
  Multiplica duas matrizes usando o algoritmo de Karatsuba.

  Args:
    A: Primeira matriz.
    B: Segunda matriz.

  Returns:
    A matriz resultante da multiplicação.
  """
  global num_operacoes
  n = A.shape[0]

  # Caso base: se a matriz for pequena, use a multiplicação tradicional
  if n <= THRESHOLD:
    return np.dot(A, B)

  # Divida as matrizes em submatrizes
  A11, A12, A21, A22 = dividir_matriz(A)
  B11, B12, B21, B22 = dividir_matriz(B)

  # Calcule as multiplicações de submatrizes usando Karatsuba
  P1 = karatsuba_matrix(A11, B11)
  P2 = karatsuba_matrix(A12, B21)
  P3 = karatsuba_matrix(A21, B12)
  P4 = karatsuba_matrix(A22, B22)
  P5 = karatsuba_matrix(A11 + A21, B11 + B12)
  P6 = karatsuba_matrix(A12 + A22, B21 + B22)
  P7 = karatsuba_matrix(A11 + A12, B22)
  P8 = karatsuba_matrix(A21 + A22, B11)

  # Combine os resultados para obter a matriz final
  C11 = P1 + P4 - P6 + P5
  C12 = P2 + P4
  C21 = P3 + P1
  C22 = P3 + P4 - P7 + P8

  return combinar_matrizes(C11, C12, C21, C22)

# As funções dividir_matriz e combinar_matrizes são as mesmas do algoritmo de Strassen

# Define o limite para a multiplicação tradicional
THRESHOLD = 16