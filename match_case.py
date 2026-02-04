
print("=== Bem vindo!! Calculadora do SENAC === ")

n1 = float(input('Digite um valor: '))
operador = input('Digite um operador: ')
n2 = float(input('Digite outro valor: '))

match operador:
    case '+':
        print(f'{n1} + {n2} = {n1 + n2}')
    
    case '-':
        print(f'{n1} - {n2} = {n1 - n2}')

    case '*':
        print(f'{n1} x {n2} = {n1 * n2}')

    case '/':
        if n2 != 0:
            print(f'{n1} / {n2} = {n1 / n2}')
        else:
            print("a")
            print('Não pode')
    
    case _:
        print("Operação Inválida")


