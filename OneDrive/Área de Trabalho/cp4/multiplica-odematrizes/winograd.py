import numpy as np

num_operacoes = 0

def winograd(A, B):
  """
  Multiplica duas matrizes usando o algoritmo de Winograd.

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

  # Calcule as multiplicações de submatrizes
  T1 = A11 + A22
  T2 = A21 + A22
  T3 = B11 + B22
  T4 = B21 + B22
  T5 = A11 + A12
  T6 = B21 - B11
  T7 = B12 - B22
  T8 = A21 - A11
  T9 = A12 - A22
  T10 = B11 + B12
  T11 = B21 + B22

  # Calcule as multiplicações intermediárias
  P1 = winograd(T1, T3)
  P2 = winograd(T2, B11)
  P3 = winograd(A11, T7)
  P4 = winograd(A22, T6)
  P5 = winograd(T5, B22)
  P6 = winograd(T8, T10)
  P7 = winograd(T9, T11)

  # Combine os resultados para obter a matriz final
  C11 = P1 + P4 - P5 + P7
  C12 = P3 + P5
  C21 = P2 + P4
  C22 = P1 - P2 + P3 + P6

  return combinar_matrizes(C11, C12, C21, C22)

# As funções dividir_matriz e combinar_matrizes são as mesmas do algoritmo de Strassen

# Define o limite para a multiplicação tradicional
THRESHOLD = 16