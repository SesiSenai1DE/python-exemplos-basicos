opcao = int(input("Escolha uma opção: 1 - Pizza, 2 - Hambúrguer, 3 - Salada: \n"))

match opcao:
    case 1:
        print("Você escolheu Pizza.")
    case 2:
        print("Você escolheu Hambúrguer.")
    case 3:
        print("Você escolheu Salada.")
    case _:
        print("Opção inválida!")
