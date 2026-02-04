print(" Bem-vindo ao sistema de atendimento! ".center(50,'='))
print()

while True:

    opcao = input("Digite a opção desejada: \n[1] Falar com atendente\n[2] Segunda via de boleto\n[3] Cancelar serviço\n[4] Informações sobre planos\n[5] Sair\n")

    match opcao:
        case '1':
            print("Aguarde... ")
            break
        case '2':
            print("Imprimindo boleto...")
            break
        case '3':
            print('Cancelando serviço...')
            break
        case '4':
            print('Informações sobre planos...')
            break
        case '5':
            print('Saindo...')
            break
        case _:
            print('Opção inválida, tente novamente!')
            continue

