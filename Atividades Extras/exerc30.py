# Ler um valor e converter para inteiro, se for possivel, ver se é par maior que 100 ou par e menor ou igual a 100, se não for esses exiba "Impar"
valor = input("Digite um valor: ")

try:
    novo_valor = int(valor)
    if novo_valor %2 == 0 :
        if novo_valor > 100:
         print("Par alto")
        else:
         print("Par baixo")
    else:
       print("Ímpar")
except ValueError:
    print("Tipo inválido")