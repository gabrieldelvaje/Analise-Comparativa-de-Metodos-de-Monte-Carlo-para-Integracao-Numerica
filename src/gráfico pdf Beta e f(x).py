import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Dados para plotar a distribuição beta
x = np.linspace(0, 1, 1000)

# Ajustando alfa e beta para a nova distribuição beta
alfa_novo = 1
beta_novo = 1

# Dados para plotar a nova distribuição beta com os novos parâmetros
y_novo_beta = beta.pdf(x, alfa_novo, beta_novo)

# Adicionando a curva da função exp(-ax) * cos(bx)
a = 0.426348491
b = 0.39128791843
y_funcao = np.exp(-a*x) * np.cos(b*x)

# Adicionando a curva da função exp(-ax) * cos(bx) multiplicada pela distribuição beta
y_funcao_mult_beta = y_funcao / y_novo_beta

# Plotando a nova distribuição beta
plt.plot(x, y_novo_beta, 'b-', lw=2, label='g(x) = PDF Beta ')

# Plotando a curva da função exp(-ax) * cos(bx)
plt.plot(x, y_funcao, 'k-', lw=1, label='f(x) = exp(-ax) * cos(bx)')

# Plotando a curva da função exp(-ax) * cos(bx) multiplicada pela distribuição beta
plt.plot(x, y_funcao_mult_beta, 'r-', lw=2, label='h(x) = f(x)/g(x)')

# Configurando o gráfico
plt.title('Distribuição Beta, Função exp(-ax) * cos(bx), e h(x)')
plt.xlabel('x')
plt.ylabel('Função')
plt.legend()

# Exibindo o gráfico
plt.show()
