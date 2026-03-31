#Ler um valor e mostrar o tipo, se for numérico, mostrar o quadrado

valor = input("Digite um valor: ")
print("O tipo do valor é", type(valor))

try:
    num = float(valor)
    print("É um valor numérico")
    
    quadrado = num ** 2
    print("O quadrado de", num,"é", quadrado)

except:
    print("Não é um valor numérico")

