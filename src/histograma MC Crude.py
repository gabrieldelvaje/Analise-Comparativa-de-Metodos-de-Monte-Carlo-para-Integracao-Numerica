import numpy as np
import matplotlib.pyplot as plt

# Função para calcular f(x)
def f(x, a, b):
    return np.exp(-a*x) * np.cos(b*x)

# Função para calcular a integral usando Monte Carlo
def monte_carlo_integration(a, b, n):
    xi = np.random.uniform(0, 1, n)
    integral_sum = np.sum(f(xi, a, b))
    return integral_sum / n

# Valores dados
a = 0.426348491
b = 0.39128791843
n = 900000 # Número de pontos
num_simulacoes = 100  # 50 amostras

# Realizar as simulações
estimativas_integrais = [monte_carlo_integration(a, b, n) for _ in range(num_simulacoes)]

# Calculando a média e variância
media = np.mean(estimativas_integrais)
variancia = np.var(estimativas_integrais, ddof=1)

# Calculando e imprimindo o erro percentual para a média
erros = [(estimativa - media) / media for estimativa in estimativas_integrais]

# Contando os pontos dentro da margem em relação à média
limite_inferior = -0.0005
limite_superior = 0.0005
pontos_dentro_da_margem = sum(1 for erro in erros if limite_inferior < erro < limite_superior)
porcentagem_dentro_da_margem = (pontos_dentro_da_margem / num_simulacoes) * 100

# Plotar histograma
plt.figure(figsize=(10, 6))
plt.hist(erros, bins='auto', edgecolor='black', alpha=0.7, label='Erros')

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
