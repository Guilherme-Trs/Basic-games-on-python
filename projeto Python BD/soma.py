
print('======================= Soma de 1 ate N ==========================')

print('============= Soma de 1 até N =============')

n = int(input("Digite um numero n para a soma: "))

soma = 0

for i in range(1, n + 1):
    soma += i

print(f'A soma de 1 ate {n} eh {soma}')
