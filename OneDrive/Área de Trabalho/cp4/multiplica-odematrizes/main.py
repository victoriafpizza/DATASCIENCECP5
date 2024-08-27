import numpy as np
import timeit

from strassen import strassen
from winograd import winograd
from karatsuba import karatsuba
from multiplicacao_tradicional import multiplicar_matrizes_tradicional
from utils import medir_tempo, zerar_contador_operacoes

# Define o tamanho das matrizes
n = 100

# Gera matrizes aleatórias
A = np.random.rand(n, n)
B = np.random.rand(n, n)

# Define a função para medir o tempo de execução
def medir_tempo(funcao, *args):
  """
  Mede o tempo de execução de uma função.

  Args:
    funcao: A função a ser medida.
    *args: Argumentos da função.

  Returns:
    O tempo de execução da função em segundos.
  """
  tempo = timeit.timeit(lambda: funcao(*args), number=1)
  return tempo

# Calcula o tempo de execução de cada algoritmo
tempo_tradicional = medir_tempo(multiplicar_matrizes_tradicional, A, B)
tempo_strassen = medir_tempo(strassen, A, B)
tempo_winograd = medir_tempo(winograd, A, B)
tempo_karatsuba = medir_tempo(karatsuba, A, B)

# Imprime os resultados
print(f"Tempo de execução da multiplicação tradicional: {tempo_tradicional:.4f} segundos")
print(f"Tempo de execução do algoritmo de Strassen: {tempo_strassen:.4f} segundos")
print(f"Tempo de execução do algoritmo de Winograd: {tempo_winograd:.4f} segundos")
print(f"Tempo de execução do algoritmo de Karatsuba: {tempo_karatsuba:.4f} segundos")

zerar_contador_operacoes()
tempo_tradicional = medir_tempo(multiplicar_matrizes_tradicional, A, B)
print(f"Tempo de execução da multiplicação tradicional: {tempo_tradicional:.4f} segundos")
print(f"Número de operações: {num_operacoes}")

zerar_contador_operacoes()
tempo_strassen = medir_tempo(strassen, A, B)
print(f"Tempo de execução do algoritmo de Strassen: {tempo_strassen:.4f} segundos")
print(f"Número de operações: {num_operacoes}")

zerar_contador_operacoes()
tempo_winograd = medir_tempo(winograd, A, B)
print(f"Tempo de execução do algoritmo de Winograd: {tempo_winograd:.4f} segundos")
print(f"Número de operações: {num_operacoes}")

zerar_contador_operacoes()
tempo_karatsuba = medir_tempo(karatsuba_matrix, A, B)
print(f"Tempo de execução do algoritmo de Karatsuba: {tempo_karatsuba:.4f} segundos")
print(f"Número de operações: {num_operacoes}")

tempos_tradicional = []
tempos_strassen = []
tempos_winograd = []
tempos_karatsuba = []

operacoes_tradicional = []
operacoes_strassen = []
operacoes_winograd = []
operacoes_karatsuba = []

tamanhos = [10, 50, 100, 200, 500]

for tamanho in tamanhos:
  # Gere matrizes de tamanho 'tamanho'
  A = np.random.rand(tamanho, tamanho)
  B = np.random.rand(tamanho, tamanho)

  # Meça o tempo e conte as operações para cada algoritmo
  tempo_tradicional, operacoes_tradicional = medir_tempo_e_operacoes(multiplicar_matrizes_tradicional, A, B)
  tempo_strassen, operacoes_strassen = medir_tempo_e_operacoes(strassen, A, B)
  tempo_winograd, operacoes_winograd = medir_tempo_e_operacoes(winograd, A, B)
  tempo_karatsuba, operacoes_karatsuba = medir_tempo_e_operacoes(karatsuba_matrix, A, B)

  # Armazene os resultados
  tempos_tradicional.append(tempo_tradicional)
  tempos_strassen.append(tempo_strassen)
  tempos_winograd.append(tempo_winograd)
  tempos_karatsuba.append(tempo_karatsuba)

  operacoes_tradicional.append(operacoes_tradicional)
  operacoes_strassen.append(operacoes_strassen)
  operacoes_winograd.append(operacoes_winograd)
  operacoes_karatsuba.append(operacoes_karatsuba)

def medir_tempo_e_operacoes(funcao, *args):
  """
  Mede o tempo de execução e conta o número de operações de uma função.

  Args:
    funcao: A função a ser medida.
    *args: Argumentos da função.

  Returns:
    Uma tupla com o tempo de execução em segundos e o número de operações.
  """
  zerar_contador_operacoes()
  tempo = timeit.timeit(lambda: funcao(*args), number=1)
  return tempo, num_operacoes

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(tamanhos, tempos_tradicional, label="Multiplicação Tradicional")
plt.plot(tamanhos, tempos_strassen, label="Strassen")
plt.plot(tamanhos, tempos_winograd, label="Winograd")
plt.plot(tamanhos, tempos_karatsuba, label="Karatsuba")
plt.xlabel("Tamanho da Matriz")
plt.ylabel("Tempo de Execução (segundos)")
plt.title("Comparação de Tempo de Execução")
plt.legend()

plt.subplot(2, 1, 2)
plt.bar(tamanhos, operacoes_tradicional, label="Multiplicação Tradicional")
plt.bar(tamanhos, operacoes_strassen, label="Strassen")
plt.bar(tamanhos, operacoes_winograd, label="Winograd")