
# Cria um programa que receba o nome de um dia da semana e diga se é dia útil ou fim de semana.

opc = input("Digite um dia da semana: ")


match opc:
    case "segunda":
        print("Dia útil")
    case "terça":
        print("Dia útil")
    case "quarta":
        print("Dia útil")
    case "quinta":
        print("Dia útil")
    case "sexta":
        print("Dia útil")
    case "sábado":
        print("Fim de semana")
    case "domingo":
        print("Fim de semana")
    case _:
        print("Opção inválida")
