import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

#símbolos para as variáveis
x = sp.symbols('x')

while True:
    expr = input(
        "Insira a expressão da função em termos de 'x' (ou 's' para sair):")

    if expr == 's':
        break
    try:
        f = sp.sympify(expr)
        derivada = sp.diff(f, x)
        print("A derivada de", expr, "é:", derivada)
        #funções que podem ser plotadas
        f_lambda = sp.lambdify(x, f, 'numpy')
        derivada_lambda = sp.lambdify(x, derivada, 'numpy')
        # delimitação do intervalo de tempo
        x_vals = np.linspace(-10, 10)
        y_vals = f_lambda(x_vals)
        y_derivada = derivada_lambda(x_vals)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title('Gráfico')
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.plot(x_vals, y_vals, label='Função')
        plt.plot(x_vals, y_derivada, label='Derivada')
        plt.legend()
        plt.show()
    except Exception as e:
        print("Não foi possível calcular a derivada. Certifique-se de que a expressão esteja correta. Erro:", e)
        # ex: x**3_ 2*x**2 _ 4*x :::: 2*x**2 + 3*x - 5
