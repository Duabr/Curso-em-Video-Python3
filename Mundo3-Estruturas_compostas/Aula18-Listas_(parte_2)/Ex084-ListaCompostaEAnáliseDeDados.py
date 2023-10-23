# Lê o nome e o peso de diversas pessoas e então mostra as seguintes informações:
# a) O número de pessoas que foram cadastradas.
# b) O maior peso cadastrado e quais pessoas têm esse peso.
# c) O menor peso cadastrado e quais pessoas têm esse peso.
from time import sleep
cadastros=[]
pessoa=[]
num_cadastros=0
teste='S'
while teste=='S':
    teste=''
    pessoa.append(input('Digite o nome da pessoa: ').strip())
    pessoa.append(float(input('Agora digite seu peso corporal em kg: ')))
    cadastros.append(pessoa[:])
    del pessoa[:]# Deleta todos os itens da lista  
    num_cadastros+=1
    while 'S'!=teste!='N':
        teste=input('Deseja continuar com mais cadastros? [S/N]: ').strip().upper()
print('\033[1mAnalizando...\033[m')
sleep(2)

print('-'*50)
print(f'Você cadastrou um total de \033[1m{num_cadastros} pessoa(s)\033[m.')
print('-'*50)
sleep(2)


for c, pessoa in enumerate(cadastros):
    if c==0:
        maior_peso=pessoa[1]
    elif pessoa[1]>=maior_peso:
        maior_peso=pessoa[1]
nomes_maior_peso=[]
for nome, peso in cadastros:# Para cada item da lista "cadastros", a variável "pessoa" pega o nome da pessoa (o primeiro item de cada "sublista"), enquanto a variável "peso" pega o peso (segundo item de cada "sublista"). Descobri isso sozinho hehe.
    if peso==maior_peso:
        nomes_maior_peso.append(nome)
print(f'O maior peso cadastrado foi de \033[1m{maior_peso}Kg\033[m.')
sleep(2)
print('Os seguintes \033[1mnomes\033[m foram cadastrados com esse peso: ')
sleep(2)
for c, nome in enumerate(nomes_maior_peso):
    print(f'{c+1}º nome: \033[1m{nome}\033[m.')
print('-'*50)
sleep(2)

for c, pessoa in enumerate(cadastros):
    if c==0:
        menor_peso=pessoa[1]
    elif pessoa[1]<=menor_peso:
        menor_peso=pessoa[1]
nomes_menor_peso=[]
for nome, peso in cadastros:# Mesmo coisa do comentário anterior.
    if peso==menor_peso:
        nomes_menor_peso.append(nome)
print(f'O menor peso cadastrado foi de \033[1m{menor_peso}Kg\033[m.')
sleep(2)
print('Os seguintes \033[1mnomes\033[m foram cadastrados com esse peso: ')
sleep(2)
for c, nome in enumerate(nomes_menor_peso):
    print(f'{c+1}º nome: \033[1m{nome}\033[m.')
print('-'*50)
sleep(2)