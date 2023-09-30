# Lê diversos números e então mostra quais dos números digitados são pares e quais são ímpares.
from time import sleep
nums=[]
continuar='S'
while continuar=='S':
    continuar=''
    nums.append(int(input('Digite um número para adicioná-lo na lista: ')))
    while 'S'!=continuar!='N':
        continuar=input('Deseja adicionar mais um número? [S/N]: ').strip().upper()
print('\033[1manalizando números...\033[m')
sleep(3)

nums_pares=[]
nums_impares=[]
print(f'Foram digitados um total de \033[1m{len(nums)}\033[m números: ',end='')
for c, n in enumerate(nums):
    if len(nums)-1!=c!=len(nums)-2:
        print(f'\033[1m{n}\033[m, ',end='')
    elif len(nums)-2==c:
        print(f'\033[1m{n}\033[m e ',end='')
    elif len(nums)-1==c:
        print(f'\033[1m{n}\033[m.')

    if n%2==0:
        nums_pares.append(n)
    else:
        nums_impares.append(n)
sleep(3)

print(f'Dentre os números digitados, há \033[1m{len(nums_pares)}\033[m número(s) par(es): ',end='')
for c, n in enumerate(nums_pares):
    if len(nums_pares)-1!=c!=len(nums_pares)-2:
        print(f'\033[1m{n}\033[m, ',end='')
    elif len(nums_pares)-2==c:
        print(f'\033[1m{n}\033[m e ',end='')
    elif len(nums_pares)-1==c:
        print(f'\033[1m{n}\033[m.')
sleep(3)

print(f'E há um total de \033[1m{len(nums_impares)}\033[m número(s) ímpar(es): ',end='')
for c, n in enumerate(nums_impares):
    if len(nums_impares)-1!=c!=len(nums_impares)-2:
        print(f'\033[1m{n}\033[m, ',end='')
    elif len(nums_impares)-2==c:
        print(f'\033[1m{n}\033[m e ',end='')
    elif len(nums_impares)-1==c:
        print(f'\033[1m{n}\033[m.')