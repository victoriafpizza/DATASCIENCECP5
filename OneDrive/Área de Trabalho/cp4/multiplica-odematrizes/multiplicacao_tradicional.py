import time
import numpy as np
import matplotlib.pyplot as plt

def multiplicar_matrizes_tradicional(A, B):
  """
  Multiplica duas matrizes usando a multiplicação tradicional.

  Args:
    A: Primeira matriz.
    B: Segunda matriz.

  Returns:
    A matriz resultante da multiplicação.
  """
  return np.dot(A, B)

# ... (resto do código) ...

# Gerando matrizes aleatórias
A = gerar_matriz_aleatoria(100, float)
B = gerar_matriz_aleatoria(100, float)

# Medindo o tempo de execução da multiplicação tradicional
tempo_tradicional = medir_tempo(multiplicar_matrizes_tradicional, A, B)

print(f"Tempo de execução da multiplicação tradicional: {tempo_tradicional:.4f} segundos")

# Criando uma lista de tamanhos de matrizes
tamanhos = [10, 50, 100, 200, 500]

# Criando listas para armazenar os tempos de execução
tempos_tradicional = []

# Executando os testes para cada tamanho de matriz
for tamanho in tamanhos:
  A = gerar_matriz_aleatoria(tamanho, float)
  B = gerar_matriz_aleatoria(tamanho, float)
  tempos_tradicional.append(medir_tempo(multiplicar_matrizes_tradicional, A, B))

# Plotando os resultados
plt.plot(tamanhos, tempos_tradicional, label="Multiplicação Tradicional")
plt.xlabel("Tamanho da Matriz")
plt.ylabel("Tempo de Execução (segundos)")
plt.title("Comparação de Desempenho de Algoritmos de Multiplicação de Matrizes")
plt.legend()
plt.show()