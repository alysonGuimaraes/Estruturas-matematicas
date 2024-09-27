import numpy as np
import matplotlib.pyplot as plt


# Classe para Transformações Lineares
class TransformacaoLinear:
    def __init__(self, matriz):
        self.matriz = matriz

    def aplicar(self, vetor):
        return np.dot(self.matriz, vetor)


# Definindo uma matriz de transformação e vetores
matriz_transformacao = np.array([[1, 2], [3, 4]])  # Exemplo de matriz de transformação
vetores = np.array([[1, 0], [0, 1], [1, 1], [-1, -1]])  # Vetores de exemplo

# Aplicando a transformação linear
transformacao = TransformacaoLinear(matriz_transformacao)
vetores_transformados = np.dot(matriz_transformacao, vetores.T).T  # Vetores transformados

# Plotando os vetores originais e transformados
plt.figure(figsize=(8, 8))  # Ajustando o tamanho da figura

# Vetores originais (em azul)
for i in range(vetores.shape[0]):
    plt.quiver(0, 0, vetores[i, 0], vetores[i, 1], angles='xy', scale_units='xy',
               scale=1, color='blue', width=0.005, label='Original' if i == 0 else "")

# Vetores transformados (em vermelho)
for i in range(vetores_transformados.shape[0]):
    plt.quiver(0, 0, vetores_transformados[i, 0], vetores_transformados[i, 1],
               angles='xy', scale_units='xy', scale=1, color='red', width=0.005,
               label='Transformado' if i == 0 else "")

# Ajustes visuais
plt.xlim(-8, 8)
plt.ylim(-9, 9)
plt.axhline(0, color='black', lw=0.5, ls='--')  # Eixo X
plt.axvline(0, color='black', lw=0.5, ls='--')  # Eixo Y
plt.grid()
plt.title("Transformação Linear de Vetores")
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")
plt.legend()
plt.show()
