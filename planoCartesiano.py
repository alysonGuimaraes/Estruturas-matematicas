import matplotlib.pyplot as plt


# Funções para retirada de valores x e y de um conjunto
# de pontos passados como parametro
def obter_valores_x(produto):
    return [p1 for (p1, p2) in produto]


def obter_valores_y(produto):
    return [p2 for (p1, p2) in produto]


# Função de montagem dos gráficos do plano cartesiano
def montar_plano(pontos):
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    # ax.set_xlim(-1, 10)
    # ax.set_ylim(-1, 10)
    pontos_x = obter_valores_x(pontos)
    pontos_y = obter_valores_y(pontos)
    for ponto in pontos:
        plt.text(ponto[0], ponto[1], f'P{pontos.index(ponto)}{ponto}', va='bottom')
    plt.plot(pontos_x, pontos_y, 'bo')
    plt.grid(True)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Representação gráfica')
    plt.show()


# Exemplo Gráfico de dois pontos em um plano cartesiano
ponto1 = [2, 0]
ponto2 = [8, 2]
montar_plano([ponto1, ponto2])


# Exemplo de produto cartesiano
conj_A = [3, 7, 5]
conj_B = [2, 6, 8]
produto_cartesiano = [(p1, p2) for p1 in conj_A for p2 in conj_B]
montar_plano(produto_cartesiano)
