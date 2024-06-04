while True:
    n_media = int(input('\nDESEJA ADICIONAR QUANTOS NUMEROS PARA FAZER A MÉDIA? \n- '))
    soma = 0
    for i in range(n_media):
        numero = float(input(f"Digite o número {i+1}: "))
        soma += numero

    media = soma / n_media
    print(f"A média dos {n_media} números inseridos é: {media}")

    continuar = input("Deseja continuar? (s/n): ")
    if continuar.lower() != 's' and continuar.lower() != 'sim':
        break
