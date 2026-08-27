import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Definindo os parâmetros da função f(x) = exp(-a*x) * cos(b*x)
a = 0.426348491
b = 0.39128791843

# Definindo os parâmetros da distribuição beta
alpha = 1
beta_param = 1
amostra = 100
n = 900000

# Definindo a função f(x)
def f(x):
    return np.exp(-a * x) * np.cos(b * x)

# Estimando a integral por Monte Carlo
def estimar_integral(n):
    xi = np.random.beta(alpha, beta_param, n)
    return np.sum(f(xi) / beta.pdf(xi, alpha, beta_param)) / n

# Calculando a estimativa da integral
estimativa_integral = estimar_integral(n)

# Função para obter amostras de estimativas
def amostras(nn):
    estimativas = []
    for i in range(nn):
        estimativas.append(estimar_integral(n))
    return estimativas

# Obtendo amostras de estimativas
amostras_estimativas = amostras(amostra)

# Contando quantas estimativas estão dentro do intervalo de erro de ±0.0005
erro = 0.0005
dentro_erro = sum(abs(estimativa_integral - est) <= erro for est in amostras_estimativas)

# Calculando a porcentagem
porcentagem_dentro_erro = (dentro_erro / amostra) * 100
print("Porcentagem de valores dentro do erro de ±0.0005:", porcentagem_dentro_erro)

# Plotando o histograma
plt.figure(figsize=(10, 6))
plt.hist(amostras_estimativas, bins='auto', edgecolor='black', alpha=0.7, label='Estimativas')

# Adicionando a estimativa da integral e a porcentagem dentro do erro na legenda
legenda = 'Estimativa da Integral: {:.6f}\nDentro do Erro: {:.2f}%'.format(estimativa_integral, porcentagem_dentro_erro)
plt.legend([legenda])

# Adicionando linhas verticais representando o intervalo de erro de ±0.0005
plt.axvline(estimativa_integral - erro, color='r', linestyle='--', label='-0.0005')
plt.axvline(estimativa_integral + erro, color='r', linestyle='--', label='+0.0005')

# Configurações adicionais do gráfico
plt.xlabel('Estimativas')
plt.ylabel('Frequência')
plt.title('Histograma das Estimativas de Monte Carlo')

# Exibindo o gráfico
plt.grid(True)
plt.legend()
plt.show()
