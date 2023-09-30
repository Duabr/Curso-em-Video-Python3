# Continua lendo valores até o usuário não quiser mais e então mostra as seguintes informações:
# a) Quantos números foram digitados
# b) Todos os números digitados em ordem decrescente
# c) Se o número 5 foi ou não digitado
from time import sleep
lista=[]
teste='S'
print('-'*50)
while teste=='S':
    lista.append(int(input('Digite um número: ')))
    teste=''
    while 'S'!=teste!='N':
        teste=input('Deseja continuar? [S/N]: ').strip().upper()
sleep(2)
print('-'*50)
print(f'Foram digitados um total de \033[m{len(lista)}\033[m números.')
print('-'*50)
sleep(3)
print('Os números digitados, em ordem decrescente, são: ')
for c,n in enumerate(sorted(lista,reverse=True)):
    if len(lista)-1!=c!=len(lista)-2:
        print(f'\033[1m{n}\033[m, ',end='')
    elif len(lista)-2==c:
        print(f'\033[1m{n}\033[m e ',end='')
    elif len(lista)-1==c:
        print(f'\033[1m{n}\033[m. ')
print('-'*50)
sleep(3)
print(f'O número \033[1m5\033[m foi digitado \033[1m{lista.count(5)}\033[m vez(es).' if 5 in lista else 'o número 5 não foi digitado \033[mnenhuma\033[m vez.')
print('-'*50)