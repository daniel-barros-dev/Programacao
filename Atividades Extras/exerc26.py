# Ler um número e informar em que posição ele está
num = float(input("Digite um número: "))

if num > 0 and num <=10:
    print("Pequeno")
elif num > 10 and num <= 100:
    print("Médio")
elif num > 100:
    print("Grande")
else:
    print("Negativo ou zero")