print('============================ CALCULADORA ============================')

next = 'sim'
while next == 'sim' or next == 's':
    a = int(input('Escolha o primeiro numero: '))
    b = int(input('Escolha o segundo numero: '))
    op = input('Escolha a operacao( +, -, *, /)').upper()

    if op == '+':
        resultado = a + b
        print(f'o resultado da operacao eh {resultado}')
    if op == '-':
        resultado = a - b
        print(f'o resultado da operacao eh {resultado}')
    if op == '*':
        resultado = a * b
        print(f'o resultado da operacao eh {resultado}')
    if op == '/':
        if b == 0:
            print('impossivel divisao por zero')
            exit()
        resultado = a/b
        print(f'o resultado da operacao eh {resultado}')

    next = input('deseja continuar ?').lower()
