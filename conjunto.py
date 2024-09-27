import matplotlib.pyplot as plt
from matplotlib_venn import venn3

##### Exemplo de conjunto: Primeiros 21 numeros naturais #####
N = list(range(0, 21))

# Configuração do gráfico
plt.plot(N, 'bo', label="N = {x | 0 <= x <= 21}")

plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('Conjunto primeiros 21 números naturais')

# Exibição do gráfico
plt.grid(True)
plt.show()


##### exemplo de conjunto fechado #####
F = [1, 2, 3, 4, 5]

# Configuração do gráfico
plt.plot(F, 'ro', label='F = {x | 1 <= x <= 5}')

plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('Conjunto Fechado')

# Exibindo o gráfico
plt.grid(True)
plt.show()


##### Exemplo de conjunto aberto #####
A = list(range(2, 5))

# Configuração do gráfico
plt.plot(A, 'bo', label='A = {x | 1 < x < 5}')

plt.xlabel('Índice')
plt.ylabel('Valor')
plt.title('Conjunto Aberto')

# Exibindo o gráfico
plt.grid(True)
plt.show()


##### Os 3 conjuntos em formato de diagrama de venn #####
diagrama = venn3((set(N), set(F), set(A)),
                 set_labels=('Conjunto primeiros 21 naturais',
                             'Conjunto Fechado',
                             'Conjunto Aberto')
                 )

plt.title('Diagrama de Venn dos três exemplos')
plt.show()

