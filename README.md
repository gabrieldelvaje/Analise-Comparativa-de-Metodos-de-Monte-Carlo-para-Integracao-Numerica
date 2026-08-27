# Monte Carlo Methods for Numerical Integration

Projeto desenvolvido para a disciplina de Simulação do curso de Matemática Aplicada e Computacional da Universidade de São Paulo (USP).

## 📚 Sobre o Projeto

Este trabalho tem como objetivo comparar diferentes técnicas de Monte Carlo para estimar numericamente a integral da função:

\[
f(x) = e^{-ax}\cos(bx)
\]

no intervalo \([0,1]\), utilizando:

- Monte Carlo Crude
- Monte Carlo Hit or Miss
- Importance Sampling
- Control Variate

O foco do estudo é determinar quantas simulações são necessárias para obter uma aproximação com erro máximo de ±0,005 e comparar a eficiência de cada método.

## 🎯 Objetivos

- Implementar diferentes métodos de integração via Monte Carlo.
- Avaliar a convergência das estimativas.
- Comparar a variância dos métodos.
- Analisar o custo computacional necessário para atingir uma determinada precisão.

## 🔬 Métodos Implementados

### 1. Monte Carlo Crude

Utiliza amostragem uniforme no intervalo de integração para estimar diretamente o valor da integral.

### 2. Hit or Miss

Estima a área sob a curva utilizando pontos aleatórios gerados em um retângulo que contém a função.

### 3. Importance Sampling

Utiliza uma distribuição auxiliar para reduzir a variância das estimativas.

### 4. Control Variate

Emprega uma função auxiliar semelhante à função original para reduzir significativamente a variância da estimativa.

## 📈 Resultados

Os experimentos mostraram que todos os métodos convergem para um valor próximo de:

```text
Integral ≈ 0.7957
