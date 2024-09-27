from matplotlib import pyplot as plt
import pandas as pd


class Funcao:
    def __init__(self, tipo):
        self.tipo = tipo

    def aplicar(self, x):
        if self.tipo == "quadrática":
            return x ** 2 + x + 4
        elif self.tipo == "linear":
            return 2 * x + 1
        else:
            return x


# Definindo valores fixos para a função
tipo_funcao = "quadrática"  # Você pode mudar para "quadrática"
funcao = Funcao(tipo_funcao)
x_valores_funcao = list(range(-6, 6))  # Valores de x de -6 a 5

# Aplicar a função
resultados_funcao = [funcao.aplicar(x) for x in x_valores_funcao]
df_funcao = pd.DataFrame(resultados_funcao, columns=['Resultado'], index=x_valores_funcao)
print(resultados_funcao)
# Configuração do gráfico
fig, ax = plt.subplots()
ax.axhline(color='black', linewidth=1)
ax.axvline(color='black', linewidth=1)

regular_alt_y = 1.4 if min(resultados_funcao) < 0 else 0
tamanho_eixo_x = [min(x_valores_funcao)*1.4, max(x_valores_funcao)*1.4]
tamanho_eixo_y = [min(resultados_funcao)*regular_alt_y, max(resultados_funcao)*1.4]

ax.set_xlim(tamanho_eixo_x[0], tamanho_eixo_x[1])
ax.set_ylim(tamanho_eixo_y[0], tamanho_eixo_y[1])

# Definição dos pontos no gráfico
ax.plot(x_valores_funcao, resultados_funcao, marker='o', linestyle='--')


plt.grid(True)
plt.show()
