import numpy as np

num_operacoes = 0

def strassen(A, B):
  """
  Multiplica duas matrizes usando o algoritmo de Strassen.

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

  # Calcule as sete multiplicações de submatrizes
  P1 = strassen(A11 + A22, B11 + B22)
  num_operacoes += 1  # Incrementa o contador para a multiplicação P1
  P2 = strassen(A21 + A22, B11)
  num_operacoes += 1  # Incrementa o contador para a multiplicação P2
  P3 = strassen(A11, B12 - B22)
  num_operacoes += 1  # Incrementa o contador para a multiplicação P3
  P4 = strassen(A22, B21 - B11)
  num_operacoes += 1  # Incrementa o contador para a multiplicação P4
  P5 = strassen(A11 + A12, B22)
  num_operacoes += 1  # Incrementa o contador para a multiplicação P5
  P6 = strassen(A21 - A11, B11 + B12)
  num_operacoes += 1  # Incrementa o contador para a multiplicação P6
  P7 = strassen(A12 - A22, B21 + B22)
  num_operacoes += 1  # Incrementa o contador para a multiplicação P7

  # Combine os resultados para obter a matriz final
  C11 = P1 + P4 - P5 + P7
  C12 = P3 + P5
  C21 = P2 + P4
  C22 = P1 - P2 + P3 + P6

  return combinar_matrizes(C11, C12, C21, C22)

def dividir_matriz(A):
  """
  Divide uma matriz em quatro submatrizes.

  Args:
    A: A matriz a ser dividida.

  Returns:
    Uma tupla com as quatro submatrizes.
  """
  n = A.shape[0]
  A11 = A[:n//2, :n//2]
  A12 = A[:n//2, n//2:]
  A21 = A[n//2:, :n//2]
  A22 = A[n//2:, n//2:]
  return A11, A12, A21, A22

def combinar_matrizes(C11, C12, C21, C22):
  """
  Combina quatro submatrizes em uma única matriz.

  Args:
    C11, C12, C21, C22: As quatro submatrizes.

  Returns:
    A matriz combinada.
  """
  n = C11.shape[0]
  C = np.zeros((2*n, 2*n))
  C[:n, :n] = C11
  C[:n, n:] = C12
  C[n:, :n] = C21
  C[n:, n:] = C22
  return C

# Define o limite para a multiplicação tradicional
THRESHOLD = 16