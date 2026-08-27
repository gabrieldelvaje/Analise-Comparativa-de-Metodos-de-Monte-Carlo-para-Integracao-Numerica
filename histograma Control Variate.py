import numpy as np
import matplotlib.pyplot as plt

# Definindo a função f(x)
def f(x, a, b):
    return np.exp(-a * x) * np.cos(b * x)

# Definindo a função g(x)
def g(x):
    return -0.3964634796444 * x + 1

# Definindo a integral de g(x)
def G(x):
    return -0.3964634796444 * ((x**2) / 2) + x

def integrar(a, b, n):
    xi = np.random.uniform(0, 1, n)
    integral = np.sum(f(xi, a, b) - g(xi) + G(1))
    return integral/n

# Definindo os parâmetros a e b
a = 0.426348491
b = 0.39128791843
n = 500
num_simulacoes = 100

# Realizar as simulações
estimativas_integrais = [integrar(a, b, n) for _ in range(num_simulacoes)]

# Calculando a média
media = np.mean(estimativas_integrais)

# Calculando o erro e a porcentagem de pontos dentro da margem
limite_inferior = media - 0.0005
limite_superior = media + 0.0005
erros = [abs(estimativa - media)/media for estimativa in estimativas_integrais]
pontos_dentro_da_margem = sum(1 for erro in erros if erro < 0.0005)
porcentagem_dentro_da_margem = (pontos_dentro_da_margem / num_simulacoes) * 100

# Plotar histograma
plt.figure(figsize=(10, 6))
plt.hist(estimativas_integrais, bins='auto', edgecolor='black', alpha=0.7, label='Estimativas')

# Adicionando a média e a porcentagem dentro da margem na legenda
legenda = 'Média: {:.6f}\nDentro da margem: {:.2f}%'.format(media, porcentagem_dentro_da_margem)
plt.legend([legenda])

# Linhas verticais representando a margem
plt.axvline(x=limite_inferior, color='r', linestyle='--')
plt.axvline(x=limite_superior, color='r', linestyle='--')

# Configurações adicionais do gráfico
plt.xlabel('Estimativas de f(x)')
plt.ylabel('Frequência')
plt.title('Histograma das Estimativas de f(x)')

# Exibindo o gráfico
plt.grid(True)
plt.show()

print("Estimativa de f(x):", media)

