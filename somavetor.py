print('===================== Soma dos Valores do Vetor =====================\n')

vetor = []

for i in range(5):
    n = int(input('Digite um numero para adicionar o vetor: '))
    vetor.append(n)

resultado = sum(vetor)
print('o elementos do vetor são: ', vetor)
print(f'O elemento presente do indice 0 do vetor é:', vetor[0])
print(f'O elemento presente do indice 1 do vetor é:', vetor[1])
print(f'O elemento presente do indice 2 do vetor é:', vetor[2])
print(f'O elemento presente do indice 3 do vetor é:', vetor[3])
print(f'O elemento presente do indice 4 do vetor é:', vetor[4])

print(f'a soma dos valores do vetor é {resultado}')

