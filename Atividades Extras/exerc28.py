# Ler um valor e exibir o tipo, se for númerico pode ser inteiro e ter que calcular o dobro e real calculando a metade, se não, exibir "inválido"
valor = input("Digite um valor: ")
print(type(valor))

try:
    novo_valor = int(valor)
    print(novo_valor * 2)
except ValueError:
    try:
     novo_valor = float(valor)
     print(novo_valor / 2)
    except ValueError:
     print("Tipo inválido")
