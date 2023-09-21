# Gera 5 números eleatórios entre 0 e 9, que são guardados em uma tupla. 
# Em seguida, mostra quais foram o maior e o menor números dentre os 5.
from random import randint
numeros = (randint(0,9), randint(0,9), randint(0,9), randint(0,9), randint(0,9))
print(f'Os 5 números sorteados foram: ',end='')
for c in range(5):
    if 4!=c!=3:
        print(f'\033[1m{numeros[c]}\033[m, ',end='')
    elif c==3:
        print(f'\033[1m{numeros[c]}\033[m e ',end='')
    elif c==4:
        print(f'\033[1m{numeros[c]}\033[m.')

print(f'O maior número da tupla é o \033[1m{max(numeros)}\033[m.')
print(f'E o menor número da tupla é o \033[1m{min(numeros)}.\033[m')