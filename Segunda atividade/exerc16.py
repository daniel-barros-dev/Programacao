#Ler um valor e mostrar o tipo, se for numérico, mostrar o quadrado

valor = input("Digite um valor: ")
print("O tipo do valor é", type(valor))

if valor.isnumeric():
    num = int(valor)
    print("O", num," é um valor numérico e o seu quadrado é",num**2)
    print("O novo tipo agora é", type(num))
    
else:
    print("Não é um valor numérico")

