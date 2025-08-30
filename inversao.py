print('=========================== Palavra Invertida ===========================')

palavra = input('digite uma palavra: ')
invertida = ''
print(f'a palavra digitada foi: {palavra}')

for letra in palavra:
    invertida = letra + invertida
    print(f' Palavra invertida: {invertida}')