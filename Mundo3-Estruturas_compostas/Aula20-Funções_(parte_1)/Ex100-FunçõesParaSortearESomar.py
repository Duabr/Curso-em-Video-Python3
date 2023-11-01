# Com duas funções, sorteia 5 números aleatórios de 1 a 10, guardando-os em uma lista,
# e então mostra a soma de todos os valores pares sorteados.
from random import randint
from time import sleep

numeros=[]

def sorteia():
    print('Os 5 números sorteados foram: \033[1m', end='', flush=True)
    sleep(2)
    for c in range(5):
        numeros.append(randint(1, 10))
        print(f'{numeros[c]} ', end='', flush=True)
        sleep(0.5)
    print('\033[m')

def soma_par():
    print('Os números pares encontrados foram: \033[1m', end='', flush=True)
    sleep(2)
    soma=0
    for n in numeros:
        if n%2==0:
            soma+=n
            print(f'{n} ', end='', flush=True)
            sleep(0.5)
    print('\033[m')
    if soma>0:
        print(f'A \033[1mSOMA\033[m de todos esses números é igual a \033[1m{soma}\033[m')
    else:
        print('\033[1;31mnão houve nenhum número par sorteado.\033[m')
        
    
sorteia()
soma_par()