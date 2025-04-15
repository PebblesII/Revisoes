# EXERCÍCIO MATRIZ 3x3 (Tipo Jogo da Velha)

# Crie uma matriz 3x3 com cada elemento prenchido com valores sequenciais de 1 a 9
matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


# Imprima cada linha da matriz em um linha diferente.
# for i in matriz:
#     print(i)
# Solicite ao usário escolher uma das nove posições digitando o número correspondente

# Verifique se o usuário digitou mesmo um número válido e dentro do intervalo de 1 a 9

# Substitua o valor escolhido por X (letra X maiúscula) ou por O (letra O maiúscula) alternadamente começando por X

# Se a casa escolhida pelo usuário já tiver sido preenchida antes por X ou O, imprima uma mensagem informando e solicite novamente outra opção válida.

# Quando todas as 9 casas da matriz tiver sido preenchidas, avise o usuário e termine o programa.

def jogo_velha():
    matriz = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    turn = "X"
    while True:
        for i in range(3):
            print(matriz[i])

        print(f"Turno : {turn}")
        user = int(input("Escolha de 1 a 9: "))
        if user.is_integer():
            for i in range(3):
                for x in range(3):
                    if user == matriz[i][x]:
                        matriz[i][x] = turn
                        if turn == "X":
                            turn = "0"
                        elif turn == "0":
                            turn = "X"
                        break
                    if matriz[i][x] == "X" or matriz[user][x] == "0":
                        print(" Ja preenchida")



jogo_velha()