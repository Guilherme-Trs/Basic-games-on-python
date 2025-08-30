print('=================== Media geral ===================')

next = 'sim'
notas = []
while next == 'sim' or next =='s':
    
    n = float(input('Digite um numero com 2 casa decimais: '))
    notas.append(n)

    next = input("Deseja continuar: ")

print('Notas digitadas: ', notas)

if len(notas) > 0:
    media = sum(notas) / len(notas) 
    print(f'media geral = {media:.2f}')
else:
    print('Nenhuma nota informada.')
