#Ler um valor e se possível colocar pra inteiro e mostrar se é maior ou menor que 10
valor = input("digite um valor: ")

try:
     novo_valor = int(valor)
     if novo_valor > 10:
       print("Alto")
     else:
       print("Baixo")

except ValueError:
 print("Entrada inválida")