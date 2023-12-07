# Calculadora em Python
def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    return x / y if y != 0 else "Não é possível dividir por zero."

# Função principal


def calculadora():
    while True:
        print("Escolha a operação:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        escolha = input("Digite a opção (1/2/3/4/5): ")

        if escolha == '5':
            print("Encerrando a calculadora.")
            break

        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"{num1} + {num2} = {adicao(num1, num2)}")

        elif escolha == '2':
            print(f"{num1} - {num2} = {subtracao(num1, num2)}")

        elif escolha == '3':
            print(f"{num1} * {num2} = {multiplicacao(num1, num2)}")

        elif escolha == '4':
            resultado = divisao(num1, num2)
            print(
                f"{num1} / {num2} = {resultado}" if not isinstance(resultado, str) else resultado)

        else:
            print("Opção inválida")


# Chamar a função da calculadora
calculadora()
