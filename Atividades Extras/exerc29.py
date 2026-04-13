# Ler um número multiplo de 5 e ver se é maior que 50 se for, exibir "multiplo alto",caso contrario, exibir "multiplo baixo", caso não seja multiplo de 5, exibir "não é multiplo"
num = float(input("Digite um número: "))

if num%5 == 0:
    if num >=50:
        print("Múltiplo alto")
    else:
        print("Múltiplo baixo")
else:
    print("Não é múltiplo")