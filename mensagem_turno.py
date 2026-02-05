# Você foi contrato para criar um menu interativo de mensagens de cumprimento.
 
# Se o usuário entrar com a letra M ou palavra Manhã, deve mostrar a mensagem "Bom dia e o nome da pessoa!"
# Se o usuário entrar com a letra T ou palavra Tarde, deve mostrar a mensagem "Boa tarde e o nome da pessoa!"
# Se o usuãrio entrar com a letra N ou palavra Noite, deve mostrar a mensagem "Boa noite eo nome da pessoa!"

nome = input('Digite seu nome: ')
periodo = input('Digite o período: ').strip().lower()

match periodo:
    case 'm' | 'manha':
        print("Bom dia", nome)

    case 't' | 'tarde':
        print("Boa tarde", nome)

    case 'n' | 'noite':
        print("Bom noite", nome)
        
    case _:
        print("Periodo iunválido")
        
