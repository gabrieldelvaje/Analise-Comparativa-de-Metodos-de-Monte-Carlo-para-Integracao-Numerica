import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, beta
import time

class MonteCarloCrude:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def f(self, x):
        """Função a ser integrada."""
        return np.exp(-self.a * x) * np.cos(self.b * x)
    
    def estimate_integral(self, n, num_simulations):
        """Estima a integral usando o método de Monte Carlo."""
        integral_estimates = []
        for _ in range(num_simulations):
            xi = np.random.uniform(0, 1, n)
            integral_sum = np.sum(self.f(xi))
            integral_estimates.append(integral_sum / n)
        return integral_estimates

class MonteCarloHitOrMiss:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def f(self, x, y):
        """Função a ser integrada (para o método de hit or miss)."""
        return np.where(np.exp(-self.a * x) * np.cos(self.b * x) > y, 1, 0)
    
    def estimate_integral(self, n, num_simulations):
        """Estima a integral usando o método de Monte Carlo hit or miss."""
        integral_estimates = []
        for _ in range(num_simulations):
            xi = np.random.uniform(0, 1, n) 
            yi = np.random.uniform(0, 1, n)  
            count_inside = np.sum(self.f(xi, yi))
            integral_estimates.append(count_inside / n)
        return integral_estimates

class SamplingImportance:
    def __init__(self, a, b, alpha, beta_param):
        self.a = a
        self.b = b
        self.alpha = alpha
        self.beta_param = beta_param
    
    def f(self, x):
        """Função a ser integrada (para o método de amostragem de importância)."""
        return np.exp(-self.a * x) * np.cos(self.b * x)
    
    def estimate_integral(self, n, num_simulations):
        """Estima a integral usando o método de amostragem de importância."""
        integral_estimates = []
        for _ in range(num_simulations):
            xi = np.random.beta(self.alpha, self.beta_param, n)
            weights = self.f(xi) / beta.pdf(xi, self.alpha, self.beta_param)
            integral_estimate = np.sum(weights) / n
            integral_estimates.append(integral_estimate)
        return integral_estimates
    
class ControlVariate:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def f(self, x):
        """Função a ser integrada."""
        return np.exp(-self.a * x) * np.cos(self.b * x)
    
    def g(self, x):
        """Função g para o método de variável de controle."""
        return -0.3964634796444 * x + 1

    def G(self, x):
        """Integral da função g."""
        return -0.3964634796444 * ((x**2) / 2) + x
    
    def estimate_integral(self, n, num_simulations):
        """Estima a integral usando o método de variável de controle."""
        integral_estimates = []
        for _ in range(num_simulations):
            xi = np.random.uniform(0, 1, n)
            integral = np.sum(self.f(xi) - self.g(xi) + self.G(1))
            integral_estimates.append(integral / n)
        return integral_estimates

def plot_distribution(integral_estimates, mean, std, percent_within_margin, label, color):
    """Plota a distribuição das estimativas da integral."""
    x = np.linspace(mean - 3*std, mean + 3*std, 100)
    pdf = norm.pdf(x, mean, std)
    plt.plot(x, pdf, label=label, linestyle='-', color=color)

def main():
    # Definindo os parâmetros
    a = 0.426348491 # 0.RG
    b = 0.39128791843 # 0.CPF
    alpha = 1
    beta_param = 1
    n_cru = 900000 # n para Monte Carlo Crude
    n_hit = 10000000 # n para Monte Carlo Hit ou miss
    n_importance = 900000 # n para Monte Carlo Amostragem por Importância
    n_control = 500 # n para Monte Carlo Variável de Controle
    num_simulations = 50

    # Criando instâncias das classes
    mc_crude = MonteCarloCrude(a, b)
    mc_hit = MonteCarloHitOrMiss(a, b)
    sampling_importance = SamplingImportance(a, b, alpha, beta_param)
    control_variate = ControlVariate(a,b)

    start_time = time.time()
    
    # Estimando a integral para cada método
    integral_estimates_crude = mc_crude.estimate_integral(n_cru, num_simulations)
    integral_estimates_hit = mc_hit.estimate_integral(n_hit, num_simulations)
    integral_estimates_importance = sampling_importance.estimate_integral(n_importance, num_simulations)
    integral_estimates_control = control_variate.estimate_integral(n_control, num_simulations)

    # Calculando médias, desvios padrão e variâncias para cada conjunto de estimativas
    mean_crude, std_crude , var_crude= np.mean(integral_estimates_crude), np.std(integral_estimates_crude), np.var(integral_estimates_crude, ddof = 1)
    mean_hit, std_hit, var_hit = np.mean(integral_estimates_hit), np.std(integral_estimates_hit), np.var(integral_estimates_hit, ddof = 1)
    mean_importance, std_importance, var_importance = np.mean(integral_estimates_importance), np.std(integral_estimates_importance), np.var(integral_estimates_importance, ddof = 1)
    mean_control, std_control, var_control = np.mean(integral_estimates_control), np.std(integral_estimates_control), np.var(integral_estimates_control, ddof = 1)

    # Calculando erros para cada método
    error_crude = np.abs(integral_estimates_crude - mean_crude)/mean_crude
    error_hit = np.abs(integral_estimates_hit - mean_hit)/mean_hit
    error_importance = np.abs(integral_estimates_importance - mean_importance)/mean_importance
    error_control = np.abs(integral_estimates_control - mean_control)/mean_control

    # Calculando porcentagem de pontos dentro da margem de erro
    percent_within_margin_crude = np.mean(error_crude < 0.0005) * 100
    percent_within_margin_hit = np.mean(error_hit < 0.0005) * 100
    percent_within_margin_importance = np.mean(error_importance < 0.0005) * 100
    percent_within_margin_control = np.mean(error_control < 0.0005) * 100

    # Plotando as curvas normais
    plt.figure(figsize=(10, 6))
    plot_distribution(integral_estimates_crude, mean_crude, std_crude, percent_within_margin_crude, 
                      'MC Crude\n(média: {:.4f}, {:.2f}% dentro)'.format(mean_crude, percent_within_margin_crude), 'DarkBlue')
    plot_distribution(integral_estimates_hit, mean_hit, std_hit, percent_within_margin_hit, 
                      'MC Hit\n(média: {:.4f}, {:.2f}% dentro)'.format(mean_hit, percent_within_margin_hit), 'DarkRed')
    plot_distribution(integral_estimates_importance, mean_importance, std_importance, percent_within_margin_importance, 
                      'MC Importance\n(média: {:.4f}, {:.2f}% dentro)'.format(mean_importance, percent_within_margin_importance), 'DarkGreen')
    plot_distribution(integral_estimates_control, mean_control, std_control, percent_within_margin_control, 
                      'MC Control\n(média: {:.4f}, {:.2f}% dentro)'.format(mean_control, percent_within_margin_control), 'Black')

    # Adicionando linhas tracejadas verticais para indicar a margem de erro
    for mean_val, color in zip([mean_crude, mean_hit, mean_importance, mean_control], ['DarkBlue', 'DarkRed', 'DarkGreen', 'Black']):
        plt.axvline(mean_val - 0.0005, color=color, linestyle='--')
        plt.axvline(mean_val + 0.0005, color=color, linestyle='--')

    # Configurações adicionais do gráfico
    plt.xlabel('Estimativa da Integral')
    plt.ylabel('Densidade de Probabilidade')
    plt.title('Distribuição dos Erros na Estimativa da Integral')
    plt.legend()
    plt.grid(True)

    # Exibindo Média e Variância
    print("Monte Carlo Crude:\n- média: {:.4f}\n- variância: {:.5f}".format(mean_crude,var_crude),"\n")
    print("Monte Carlo Hit or Miss:\n- média: {:.4f}\n- variância: {:.5f}".format(mean_hit, var_hit),"\n")
    print("Monte Carlo Importance Sample:\n- média: {:.4f}\n- variância: {:.5f}".format(mean_importance, var_importance),"\n")
    print("Monte Carlo Control Variate:\n- média: {:.4f}\n- variância: {:.5f}".format(mean_control, var_control))

    # Exibindo o gráfico
    plt.show()

    elapsed_time = time.time() - start_time
    print("\nTempo decorrido para cálculo: {:.2f} segundos".format(elapsed_time))

if __name__ == "__main__":
    main()
