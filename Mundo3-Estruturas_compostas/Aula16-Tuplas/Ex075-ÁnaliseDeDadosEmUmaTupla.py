# Lê 4 números e então mostra as seguintes informações:
# a) Quantas vezes o número 9 aparece
# b) Em quaus posições o número 3 aparece
# c) Quais foram os números pares digitados e em quantos eles são
from time import sleep
nums = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Só mais um: ')), int(input('Agora é sério, último número: ')))

print('-'*50)
print('Os números digitados foram: ',end='')
for c in range(4):
    if 2!=c!=3:
        print(f'\033[1m{nums[c]}\033[m, ',end='')
    elif c==2:
        print(f'\033[1m{nums[c]}\033[m e ',end='')
    elif c==3:
        print(f'\033[1m{nums[c]}\033[m.')
print('-'*50)
sleep(2)

print('-'*50)
if 9 not in nums:
    print('O número 9 \033[1;31mnão foi digitado nenhuma vez\033[m.')
else:
    print(f'Você digitou o número 9 um total de \033[1m{nums.count(9)}\033[m vez(es).')
print('-'*50)
sleep(2)

print('-'*50)
txt=''
for c in range(4):
    if 3 == nums[c]:
        txt+=f'Na {nums.index(3,c)+1}ª posição; '
if 3 not in nums:
    print('O número 3 \033[1;31mnão foi digitado nenhuma vez\033[m.')
else:
    print(f'Você digitou o número 3 nas seguintes posições: ')
    print(txt)
print('-'*50)
sleep(2)

print('-'*50)
quanti_par=0
num_par=txt2=''
for n in nums:
    if n%2==0:
        quanti_par+=1
        num_par+=f'{n}'
for c in range(quanti_par):
    if quanti_par-2!=c!=quanti_par-1:
        txt2 += f'\033[1m{num_par[c]}\033[m, '
    elif c==quanti_par-2:
        txt2 += f'\033[1m{num_par[c]}\033[m e '
    elif c==quanti_par-1:
        txt2 += f'\033[1m{num_par[c]}\033[m.'
if quanti_par==0:
    print('Dos números digitados, \033[1;mnenhum deles é par\033[m.')
else:
    print(f'Dos números digitados, há \033[1m{quanti_par} número(s) par(es)\033[m, sendo ele(s):')
    len_num_par=len(num_par)
    print(txt2)
print('-'*50)
sleep(2)

print('FIM')