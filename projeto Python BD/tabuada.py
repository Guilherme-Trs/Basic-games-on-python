print('================= Tabuada =================')

n = int(input('Digite o numero que farei a tabuada dele do 0 ao 10: '))

for i in range(1, 11):
        resp = n * i
        print(f"{n} * {i} = {resp}")