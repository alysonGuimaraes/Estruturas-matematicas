import itertools
import networkx as nx
import matplotlib.pyplot as plt


# Função para gerar o grupo simétrico de um conjunto de tamanho n
def grupo_simetrico(n):
    elementos = list(range(1, n + 1))  # Conjunto {1, 2, ..., n}

    # Gerar todas as permutações do conjunto
    permutacoes = list(itertools.permutations(elementos))

    return permutacoes


# Função para desenhar o grafo do grupo simétrico
def desenhar_grafo_grupo_simetrico(permutacoes):
    # Criar um grafo
    G = nx.Graph()

    # Adicionar os nós (cada permutação é um nó)
    for perm in permutacoes:
        G.add_node(perm)

    # Conectar os nós que diferem por uma única transposição (troca de dois elementos)
    for i in range(len(permutacoes)):
        for j in range(i + 1, len(permutacoes)):
            if sum(p != q for p, q in zip(permutacoes[i], permutacoes[j])) == 2:
                G.add_edge(permutacoes[i], permutacoes[j])

    # Desenhar o grafo
    plt.figure(figsize=(10, 10))
    pos = nx.spring_layout(G, seed=42)  # Layout para melhor visualização
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=2000, font_size=10, font_weight='bold')
    plt.title(f"Grafo do Grupo Simétrico S_{len(permutacoes[0])}")
    plt.show()


# Função principal para gerar e desenhar o grupo simétrico
def gerar_grafo_grupo_simetrico(n):
    permutacoes = grupo_simetrico(n)
    desenhar_grafo_grupo_simetrico(permutacoes)


# Chamar a função com um conjunto de tamanho 3
gerar_grafo_grupo_simetrico(3)
