
# JOGO DE PAR OU IMPAR

import random

nome = (input('Digite seu nome: '))

computador = random.randint(0, 10)

jogador = input('Escolha entre Par(P) ou Impar(I):').upper()

if (jogador != 'P' and jogador != 'I' and jogador != 'p' and jogador != 'i'):
    print("opcao invalida")
    exit()

Numerojogador = int(input('Escolha seu numero(0 a 10): '))

if (Numerojogador < 0 or Numerojogador > 10):
    print("opcao invalida")
    exit()

soma = Numerojogador + computador
print(f'{Numerojogador} + {computador} = {soma}')

if soma % 2 == 0:
    resultado = 'P'
else:
    resultado = 'I'

if jogador == resultado:
    print(f'{nome} ganhou !!!!!!!!')
else:
    print('computador ganhou!!!!!!!!')
