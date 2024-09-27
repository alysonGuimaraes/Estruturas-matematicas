import matplotlib.pyplot as plt
import networkx as nx


# Função para gerar o grafo de um anel Z_n
def grafo_anel_zn(n):
    # Criar o grafo
    G = nx.DiGraph()

    # Adicionar os nós (elementos do anel Z_n)
    elementos = list(range(n))
    G.add_nodes_from(elementos)

    # Conectar nós com base na operação de adição módulo n
    for i in range(n):
        for j in range(n):
            soma = (i + j) % n
            G.add_edge(i, soma, label=f'{i}+{j}={soma}')

    # Layout circular para representar o anel
    pos = nx.circular_layout(G)

    # Desenhar o grafo
    plt.figure(figsize=(8, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000, font_size=12, font_weight='bold', arrows=True)

    # Adicionar rótulos de arestas (mostrando as operações de soma)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

    # Título do gráfico
    plt.title(f"Adição no Anel Z_{n} (Módulo {n})", size=15)
    plt.show()


# Função principal para gerar o gráfico para um anel Z_n
def gerar_grafo_anel_zn(n):
    grafo_anel_zn(n)


# Exemplo: Gerar o grafo do anel Z_6 (números inteiros módulo 6)
gerar_grafo_anel_zn(6)

