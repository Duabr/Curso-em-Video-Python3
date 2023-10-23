# Lê 7 números e coloca-os em duas listas duas listas separadas: uma com os números pares e outra com os números ímpares.
# Essas duas listas devem estar dentro de outra lista.
# No fim, mostra os números pares e ímpares digitados, ambos em ordem crescente.
from time import sleep
numeros=[[], []]# A primeira "sublista" será de números pares, a segunda de números ímpares.
for c in range(7):
    n=int(input(f'Digite o \033[1m{c+1}º\033[m número: '))
    if n%2==0:
        numeros[0].append(n)
    else:
        numeros[1].append(n)
print('\033[1mAnalizando números...\033[m')
sleep(2)

txt_pares=txt_impares=''
for c, v in enumerate(sorted(numeros[0])):# Organiza os números pares.
    if len(numeros[0])-1!=c!=len(numeros[0])-2:
        txt_pares+=f'\033[1m{v}\033[m, '
    elif len(numeros[0])-2==c:
        txt_pares+=f'\033[1m{v}\033[m e '
    elif len(numeros[0])-1==c:
        txt_pares+=f'\033[1m{v}\033[m.'
for c, v in enumerate(sorted(numeros[1])):
    if len(numeros[1])-1!=c!=len(numeros[1])-2:# Organiza os números ímpares.
        txt_impares+=f'\033[1m{v}\033[m, '
    elif len(numeros[1])-2==c:
        txt_impares+=f'\033[1m{v}\033[m e '
    elif len(numeros[1])-1==c:
        txt_impares+=f'\033[1m{v}\033[m.'

print('-'*80)
print(f'Os números pares digitados, em ordem crescente, foram: {txt_pares}')
print('-'*80)
sleep(2)
print(f'Agora, os números ímpares digitados, em ordem crescente, foram: {txt_impares}')
print('-'*80)