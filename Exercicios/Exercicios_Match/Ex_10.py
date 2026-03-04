
# Cria um programa que receba duas jogadas:
# •	Jogador 1
# •	Jogador 2
# Usa match para determinar o resultado:
# •	Pedra ganha de Tesoura
# •	Tesoura ganha de Papel
# •	Papel ganha de Pedra
# •	Se forem iguais, é Empate


print("Opções: pedra, papel, tesoura")

jogador1 = input("Jogador 1, escolha: ").lower()
jogador2 = input("Jogador 2, escolha: ").lower()

match (jogador1, jogador2):
    case (j1, j2) if j1 == j2:
        print("Empate!")
    case ("pedra", "tesoura") | ("tesoura", "papel") | ("papel", "pedra"):
        print("Jogador 1 venceu!")
    case ("tesoura", "pedra") | ("papel", "tesoura") | ("pedra", "papel"):
        print("Jogador 2 venceu!")
    case _:
        print("Jogada inválida")