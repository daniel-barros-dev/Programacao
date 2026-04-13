# Ler 3 números inteiros e exibir a ordem decrescente o resto da divisão por 3
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
num3 = int(input("Digite outro número: "))

lista = [num1%3, num2%3, num3%3]

ordenada = sorted(lista, reverse=True)

print(ordenada)