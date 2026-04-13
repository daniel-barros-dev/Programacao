# Ler dois números e se forem positivos calcular a soma, se não forem calcular o produto
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))

if num1 >=0 and num2 >=0:
    print(num1 + num2)
else:
    print(num1 * num2)