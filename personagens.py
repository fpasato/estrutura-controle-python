


experiencia  = int(input('Digite sua experiencia: '))

if experiencia < 100:
     print('experiencia: iniciante')
elif experiencia >= 100 and experiencia < 500:
     print('experiencia: Intermediário')
else:
     print('experiencia: Veterano')

acao  = input('Qual ação o jogador deseja executar:\n[A] → Atacar\n[D] → Defender\n[F] → Fugir\n').strip().lower()

match acao:
    case 'a':
        print("Você avançou para o ataque!")
    case 'd':
          print("Você levantou o escudo!")
    case 'f':
          print("Você fugiu da batalha!")
    case _:
        print('Ação inválida!')