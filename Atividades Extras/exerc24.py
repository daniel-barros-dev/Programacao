# Ler um número inteiro e exibir se ele é par ou impar no intervalo e se esta fora do intervalo
num = int(input("Digite um número: "))

if num >=1 and num <=100:
    if num % 2 == 0:
        print("Par no intervalo")
    else:
        print("Impar no intervalo")
else:
    print("Fora do intervalo")