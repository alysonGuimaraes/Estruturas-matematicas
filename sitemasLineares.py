import numpy as np
import matplotlib.pyplot as plt


# Função para resolver o sistema de equações lineares
def resolver_sistema(A, B):
    try:
        # Resolve o sistema Ax = B
        solucao = np.linalg.solve(A, B)
        return solucao
    except np.linalg.LinAlgError:
        print("O sistema não tem uma solução única.")
        return None


# Função para representar graficamente duas equações lineares
# Recebe os coeficientes das equações para plotar o gráfico
def plotar_equacoes(coeficientes, interval=(-10, 10)):
    x_vals = np.linspace(interval[0], interval[1], 400)

    plt.figure(figsize=(8, 6))

    for coef in coeficientes:
        a, b, c = coef
        # isola y (ax + by = c -> y = (c - ax)/b)
        y_vals = (c - a * x_vals) / b
        plt.plot(x_vals, y_vals, label=f'{a}x + {b}y = {c}')

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Representação gráfica das equações')
    plt.show()


################ Exemplo 1 ################
A = np.array([[2, 3], [4, -6]])  # 2x + 3y = 5 e 4x - 6y = 12
B = np.array([5, 12])

solucao = resolver_sistema(A, B)
if solucao is not None:
    print(f'Solução sistema 1: x = {solucao[0]}, y = {solucao[1]}')

coeficientes_sis1 = [
    [2, 3, 5],  # 2x + 3y = 5
    [4, -6, 12]  # 4x - 6y = 12
]

plotar_equacoes(coeficientes_sis1)


################ Exemplo 2 ################
C = np.array([[3, 1], [2, -4]])  # 3x + 1y = 4 e 2x - 4y = -2
D = np.array([4, -2])

solucao = resolver_sistema(C, D)
if solucao is not None:
    print(f'Solução sistema 2: x = {solucao[0]}, y = {solucao[1]}')

coeficientes_sis2 = [
    [3, 1, 4],  # 2x + 3y = 5
    [2, -4, -2]  # 4x - 6y = 12
]

plotar_equacoes(coeficientes_sis2)


################ Exemplo 3 ################
E = np.array([[5, 10], [-8, 4]])  # 5x + 10y = 42 e -8x + 4y = -14
F = np.array([42, -14])

solucao = resolver_sistema(E, F)
if solucao is not None:
    print(f'Solução sistema 3: x = {solucao[0]}, y = {solucao[1]}')

coeficientes_sis3 = [
    [5, 10, 42],  # 5x + 10y = 42
    [-8, 4, -14]  # -8x + 4y = -14
]

plotar_equacoes(coeficientes_sis3)
