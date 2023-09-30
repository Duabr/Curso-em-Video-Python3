# Lê 5 números, guardando eles em uma lista e então dizendo quais são o maior e o menor
# Números da lista e suas respectivas posições.
from time import sleep
nums=[]
for c in range(5):
    nums.append(int(input(f'Digite o {c+1}º número: ')))
maior=max(nums)
menor=min(nums)
txt_maior=''
txt_menor=''
nums_maiores=[]
nums_menores=[]

for n in nums:
    if n==maior:
        nums_maiores.append(n)
    if n==menor:
        nums_menores.append(n)

start=0
for c, n in enumerate(nums_maiores):
    if len(nums_maiores)-1!=c!=len(nums_maiores)-2:
        txt_maior+=f'\033[1m{nums.index(maior,start)+1}ª\033[m, '
        start=nums.index(maior,start)+1
    elif len(nums_maiores)-2==c:
        txt_maior+=f'\033[1m{nums.index(maior,start)+1}ª\033[m e '
        start=nums.index(maior,start)+1
    elif len(nums_maiores)-1==c:
        txt_maior+=f'\033[1m{nums.index(maior,start)+1}ª\033[m posição.'
        start=nums.index(maior,start)+1

start=0
for c, n in enumerate(nums_menores):
    if len(nums_menores)-1!=c!=len(nums_menores)-2:
        txt_menor+=f'\033[1m{nums.index(menor,start)+1}ª\033[m, '
        start=nums.index(menor,start)+1
    elif len(nums_menores)-2==c:
        txt_menor+=f'\033[1m{nums.index(menor,start)+1}ª\033[m e '
        start=nums.index(menor,start)+1
    elif len(nums_menores)-1==c:
        txt_menor+=f'\033[1m{nums.index(menor,start)+1}ª\033[m posição.'
        start=nums.index(menor,start)+1

print(f'O \033[1mmaior\033[m número encontrado foi: \033[1m{maior}\033[m.')
print(f'Ele foi encontrado nas seguintes posições: {txt_maior}')
print(f'O \033[1mmenor\033[m número encontrado foi: \033[1m{menor}\033[m.')
print(f'Ele foi encontrado nas seguintes posições: {txt_menor}')