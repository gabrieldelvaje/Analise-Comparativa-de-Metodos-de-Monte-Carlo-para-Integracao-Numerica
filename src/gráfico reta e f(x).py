import numpy as np
import matplotlib.pyplot as plt

# Definindo a função f(x)
def f(x, a, b):
    return np.exp(-a * x) * np.cos(b * x)

# Definindo os parâmetros a e b
a = 0.426348491
b = 0.39128791843

# Definindo a função g(x)
def g(x):
    return -0.3964634796444 * x + 1

# Criando um intervalo de valores de x
x_values = np.linspace(0, 1, 100)

# Calculando os valores de f(x) para cada valor de x
f_values = f(x_values, a, b)

# Calculando os valores de g(x) para cada valor de x
g_values = g(x_values)

# Criando o gráfico
plt.figure(figsize=(8, 6))
plt.plot(x_values, f_values, label='f(x)', color='blue')
plt.plot(x_values, g_values, label='g(x)', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Gráfico de f(x) e g(x)')
plt.legend()
plt.grid(True)
plt.show()
