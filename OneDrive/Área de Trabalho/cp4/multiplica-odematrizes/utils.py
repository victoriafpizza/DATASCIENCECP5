import time
import numpy as np
import matplotlib.pyplot as plt

def medir_tempo(funcao, *args):
  """
  Mede o tempo de execução de uma função.

  Args:
    funcao: A função a ser medida.
    *args: Argumentos da função.

  Returns:
    O tempo de execução da função em segundos.
  """
  inicio = time.time()
  funcao(*args)
  fim = time.time()
  return fim - inicio

def gerar_matriz_aleatoria(n, tipo_dado):
  """
  Gera uma matriz quadrada aleatória de tamanho n com o tipo de dado especificado.

  Args:
    n: Tamanho da matriz.
    tipo_dado: Tipo de dado da matriz (ex: int, float).

  Returns:
    Uma matriz numpy.ndarray.
  """
  return np.random.rand(n, n).astype(tipo_dado)

def gerar_matriz_identidade(n):
  """
  Gera uma matriz identidade de tamanho n.

  Args:
    n: Tamanho da matriz.

  Returns:
    Uma matriz numpy.ndarray.
  """
  return np.identity(n)

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

def zerar_contador_operacoes():
  """
  Zera a variável global num_operacoes.
  """
  global num_operacoes
  num_operacoes = 0