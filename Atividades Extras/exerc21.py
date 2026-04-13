# Ler um número inteiro e informar se é positivo, se for, analise se é multiplo de 2 e 3 ao mesmo tempo
num = int(input("Digite um número: "))

if num >=0:
    if num %2 == 0 and num %3 == 0:
        print("Múltiplo de 2 e 3")
    else:
        print("Não atende")
else:
    print("Número inválido")
