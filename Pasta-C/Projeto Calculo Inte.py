import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# símbolo para a variável de integração
x = sp.symbols('x')

while True:
    expr = input(
        "Insira a expressão da função em termos de 'x' (ou 's' para sair): ")

    if expr == 's':
        break
    try:
        f = sp.sympify(expr)
        integral = sp.integrate(f, x)
        print("A integral de", expr, "é:", integral)
        # função que pode ser plotada
        f_lambda = sp.lambdify(x, f, 'numpy')
        # intervalo de tempo
        x_vals = np.linspace(-12, 12)
        y_vals = f_lambda(x_vals)
        # gráfico da função e da área sob a curva
        plt.plot(x_vals, y_vals, label=expr)
        plt.fill_between(x_vals, y_vals, 0,
                         where=[-12 <= x <= 12 for x in x_vals], alpha=0.2)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Gráfico da integral")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.legend()
        plt.show()
# em caso de erro demonstrar texto
    except Exception as e:
        print("Não foi possível calcular a integral. Certifique-se de que a expressão esteja correta. Erro:", e)
        # ex: 2*x**2 + 3*x - 5 ::::
