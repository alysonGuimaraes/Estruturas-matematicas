import matplotlib.pyplot as plt
import networkx as nx


# Função para gerar o corpo finito F_p
def corpo_finito(p):
    elementos = list(range(p))  # Conjunto {0, 1, ..., p-1}
    return elementos


# Função para desenhar o grafo do corpo finito F_p
def desenhar_grafo_corpo_finito(p):
    elementos = corpo_finito(p)

    # Criar um grafo
    G = nx.DiGraph()

    # Adicionar os nós (elementos do corpo F_p)
    G.add_nodes_from(elementos)

    # Conectar nós com base na operação de adição módulo p
    for i in elementos:
        for j in elementos:
            soma = (i + j) % p
            multiplicacao = (i * j) % p

            # Adicionando arestas de adição e multiplicação
            G.add_edge(i, soma, label=f'{i}+{j}={soma}', color='blue')
            if j != 0:  # Multiplicação por zero é inválida para divisão, mas ainda permitida
                G.add_edge(i, multiplicacao, label=f'{i}*{j}={multiplicacao}', color='red')

    # Layout circular para representar o corpo finito
    pos = nx.circular_layout(G)

    # Desenhar o grafo
    plt.figure(figsize=(10, 10))
    colors = [G[u][v]['color'] for u, v in G.edges()]
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', node_size=1000, font_size=12, font_weight='bold',
            edge_color=colors, arrows=True)

    # Adicionar rótulos às arestas
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='black')

    # Título do gráfico
    plt.title(f"Grafo do Corpo Finito F_{p} (Módulo {p})", size=15)
    plt.show()


# Função principal para gerar o gráfico para um corpo F_p
def gerar_grafo_corpo_finito(p):
    desenhar_grafo_corpo_finito(p)


# Exemplo: Gerar o grafo do corpo finito F_5 (números inteiros módulo 5)
gerar_grafo_corpo_finito(5)