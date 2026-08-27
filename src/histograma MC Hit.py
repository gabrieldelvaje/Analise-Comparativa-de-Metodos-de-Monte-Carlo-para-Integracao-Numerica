import numpy as np
import matplotlib.pyplot as plt

# Função indicadora para verificar se um ponto (x, y) está dentro da curva
def h(x, y, a, b):
    return np.where(np.exp(-a*x) * np.cos(b*x) > y, 1, 0)

# Função para calcular a integral usando Monte Carlo
def monte_carlo_integration(a, b, n):
    xi = np.random.rand(n)
    yi = np.random.rand(n)
    count_inside = np.sum(h(xi, yi, a, b))
    return count_inside / n

# Valores dados
a = 0.426348491
b = 0.39128791843
n = 9000000  # Número de pontos
num_simulacoes = 50  # 50 amostras

# Realizar as simulações
estimativas_integrais = [monte_carlo_integration(a, b, n) for _ in range(num_simulacoes)]

# Calculando a média e variância
media = np.mean(estimativas_integrais)
variancia = np.var(estimativas_integrais, ddof=1)

# Calculando e imprimindo o erro percentual médio
erros_percentuais = (estimativas_integrais - media) / media

# Contando os pontos dentro da margem em relação à média
limite_inferior = -0.0005
limite_superior = 0.0005
pontos_dentro_da_margem = np.sum((limite_inferior < erros_percentuais) & (erros_percentuais < limite_superior))
porcentagem_dentro_da_margem = (pontos_dentro_da_margem / num_simulacoes) * 100

# Plotar histograma
plt.figure(figsize=(10, 6))
plt.hist(erros_percentuais, bins='auto', edgecolor='black', alpha=0.7, label='Erros')

# Adicionando a média e a porcentagem dentro da margem na legenda
legenda = 'Média: {:.6f}\nDentro da margem: {:.2f}%'.format(media, porcentagem_dentro_da_margem)
plt.legend([legenda])

# Linhas verticais representando a margem
plt.axvline(x=limite_inferior, color='r', linestyle='--')
plt.axvline(x=limite_superior, color='r', linestyle='--')

# Configurações adicionais do gráfico
plt.xlabel('Erro Percentual em Relação à Média')
plt.ylabel('Frequência')
plt.title('Histograma do Erro Percentual em Relação à Média')

# Exibindo o gráfico
plt.grid(True)
plt.show()
