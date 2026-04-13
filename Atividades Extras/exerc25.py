# Exibir o tipo e se possivel converter para float, exibir o resultado da divisão por 2 e caso contrario, exibir "não numerico"
valor = input("digite um valor:")
print(type(valor))

try:
    novo_valor = float(valor)
    print(novo_valor/2)

except ValueError:
    print("Não numérico")


              