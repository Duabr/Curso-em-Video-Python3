# Lê 5 valores numéricos, colocando-os em uma lista JÁ EM ORDEM CRESCENTE assim que o número for digitado.
# Depois mostra todos os números digitados.
from time import sleep
lista=[]
print('-'*50)
for _ in range(5):
    num = int(input(f'Digite o {_+1}º número da lista: '))
    if _==0 or num<=lista[0]:
        lista.insert(0,num)
        print('Número adicionado na \033[1m1ª\033[m posição!')
    elif _==1 and lista[0]<=num:
        lista.append(num)
        print(f'Número adicionado na \033[1m2ª\033[m posição!')
    elif num>=lista[-1]:
                lista.append(num)
                print(f'Número adicionado na \033[1m{len(lista)}ª\033[m posição!')
    else:
        for c,n in enumerate(lista):
            if n<=num<=lista[c+1]:
                lista.insert(lista.index(lista[c+1]), num)
                print(f'Número adicionado na \033[1m{lista.index(lista[c+1])+1}ª\033[m posição!')
                break
print('-'*50)
sleep(2)
print(f'Os 5 números digitados foram: \033[1m{lista[0]}, {lista[1]}, {lista[2]}, {lista[3]} e {lista[4]}.\033[m')