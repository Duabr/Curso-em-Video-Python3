# Versão melhorada do exercício anterior (ex086-MatrizEmPython), em que as seguintes informalções extras aparecem: 
# a) A soma de todos os valores pares;
# b) A soma de todos os valores da terceira coluna;
# c) O maior valor da segunda linha.
from time import sleep
nums=[[], [], []]
soma_pares=soma_ter_col=0
print('Digite 9 númerso para colocá-los em uma matriz;')
for c in range(9):
    nums[c//3].append(int(input(f'Digite o número que ficará na posição \033[1m[{c//3}][{c%3}]\033[m: ')))
print('\033[1mOrganizando os números...\033[m')
sleep(2)

print('-'*70)
for c in range(9):
    print(f' [{nums[c//3][c%3]:^5}] ',end='')
    if c%3==2 and c!=8:
        print('\n')

    if nums[c//3][c%3]%2==0:
        soma_pares+=nums[c//3][c%3]

    if c%3==2:
        soma_ter_col+=nums[c//3][c%3]

    if c==1:
        maior_seg_lin=nums[c//3][c%3]
    elif c//3==1 and nums[c//3][c%3]>maior_seg_lin:
        maior_seg_lin=nums[c//3][c%3]
print('\n', '-'*70)
sleep(3)

print(f'Somando todos os números pares digitados, o resultado é \033[1m{soma_pares}\033[m.')
print('-'*70)
sleep(3)

print(f'A soma de todos os números da terceira coluna é igual a \033[1m{soma_ter_col}\033[m.')
print('-'*70)
sleep(3)

print(f'O maior número da segunda linha é \033[1m{maior_seg_lin}\033[m')
print('-'*70)
sleep(3)