##JOGO DA MEMORIA

import random 

computador = random.randint(0,100)

print('=================== JOGO DA MEMORIA ===================')

tentativas = 10

while tentativas > 0:
    jogador = int(input('qual numero o computador escolheu ?'))
    if jogador == computador:
        print('parabens vc acertou!!!!!!!!\n')
        break
    if jogador < computador:
        print('Numero baixo, tente um maior\n')
    else:
        print('Numero alto, tento um menor\n')    
    tentativas -= 1
    print(f'ainda restam {tentativas}\n')

if tentativas == 0:
    print('Sua tentativas acabaram :(\n')
    print(f"o numero era {computador}\n")
