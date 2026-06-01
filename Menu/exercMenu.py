# MENU

def menu():
    print("MENU: ")
    print("1 - Maior e menor valor")
    print("2 - Pares e ímpares")
    print("3 - Buscar número")
    print("4 - Remover número")
    print("5 - Contagem de sinais")
    print("6 - Comparar listas")
    print("7 - Cadastro de produtos")
    print("8 - Ordenação")
    print("0 - Sair")


# ALGORITMO 1

def algoritmo1():
    numeros = []

    for i in range(10):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)

    print("Lista:", numeros)
    print("Maior valor:", max(numeros))
    print("Menor valor:", min(numeros))


# ALGORITMO 2

def algoritmo2():
    numeros = []
    pares = []
    impares = []

    for i in range(15):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)

        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    print("Lista original:", numeros)
    print("Pares:", pares)
    print("Ímpares:", impares)


# ALGORITMO 3

def algoritmo3():
    numeros = []

    for i in range(8):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)

    busca = int(input("Digite um número para buscar: "))

    if busca in numeros:
        print("O número está na lista.")
    else:
        print("O número NÃO está na lista.")


# ALGORITMO 4

def algoritmo4():
    numeros = []

    for i in range(10):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)

    remover = int(input("Digite o número que deseja remover: "))

    if remover in numeros:
        while remover in numeros:
            numeros.remove(remover)

        print("Lista atualizada:", numeros)

    else:
        print("Número não encontrado.")


# ALGORITMO 5

def algoritmo5():
    positivos = 0
    negativos = 0
    zeros = 0

    numeros = []

    for i in range(20):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)

        if num > 0:
            positivos += 1

        elif num < 0:
            negativos += 1

        else:
            zeros += 1

    print("Lista:", numeros)
    print("Positivos:", positivos)
    print("Negativos:", negativos)
    print("Zeros:", zeros)


# ALGORITMO 6

def algoritmo6():
    lista1 = []
    lista2 = []

    print("LISTA 1")

    for i in range(5):
        num = int(input(f"Digite o {i+1}º número: "))
        lista1.append(num)

    print("LISTA 2")

    for i in range(5):
        num = int(input(f"Digite o {i+1}º número: "))
        lista2.append(num)

    comuns = []
    exclusivos1 = []
    exclusivos2 = []

    for num in lista1:
        if num in lista2 and num not in comuns:
            comuns.append(num)

    for num in lista1:
        if num not in lista2:
            exclusivos1.append(num)

    for num in lista2:
        if num not in lista1:
            exclusivos2.append(num)

    print("Valores em comum:", comuns)
    print("Exclusivos da lista 1:", exclusivos1)
    print("Exclusivos da lista 2:", exclusivos2)


# ALGORITMO 7

def algoritmo7():
    nomes = []
    precos = []
    estoques = []

    for i in range(5):
        nome = input("Nome do produto: ")
        preco = float(input("Preço: "))
        estoque = int(input("Estoque: "))

        nomes.append(nome)
        precos.append(preco)
        estoques.append(estoque)

    print("Produtos com estoque menor que 10:")

    for i in range(5):
        if estoques[i] < 10:
            print(nomes[i])

    maior_preco = max(precos)
    indice = precos.index(maior_preco)

    print("Produto mais caro:", nomes[indice])


# ALGORITMO 8

def algoritmo8():
    numeros = []

    for i in range(12):
        num = int(input(f"Digite o {i+1}º número: "))
        numeros.append(num)

    crescente = sorted(numeros)
    decrescente = sorted(numeros, reverse=True)

    pares = 0
    impares = 0

    for num in numeros:
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

    print("Ordem crescente:", crescente)
    print("Ordem decrescente:", decrescente)
    print("Quantidade de pares:", pares)
    print("Quantidade de ímpares:", impares)


# PROGRAMA PRINCIPAL

while True:
    menu()

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        algoritmo1()

    elif opcao == 2:
        algoritmo2()

    elif opcao == 3:
        algoritmo3()

    elif opcao == 4:
        algoritmo4()

    elif opcao == 5:
        algoritmo5()

    elif opcao == 6:
        algoritmo6()

    elif opcao == 7:
        algoritmo7()

    elif opcao == 8:
        algoritmo8()

    elif opcao == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")