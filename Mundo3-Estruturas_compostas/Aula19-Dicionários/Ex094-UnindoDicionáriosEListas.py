# Lê o nome, sexo e idade de diversas pessoas. Depois, mostra os seguintes dados:
# a) O número de pessoas cadastradas
# b) A média de idade de todos
# c) Os dados de todas as mulheres
# d) Todas as pessoas com a idade acima da MÉDIA.
# Os dados das pessoas estarão guardados em um dicionário para cada pessoa, e todos os dicionários estarão guardados em uma lista.
from time import sleep

pessoas=[]
while True:
    p={}
    teste=''

    p['nome']=input('Qual é o nome da pessoa? R: ').strip()
    while 'F'!=teste!='M' and teste!='NB':
        teste=input('E o seu sexo? [M/F/NB]: ').strip().upper()# M para masculino, F para feminino, NB para não-binário.
    p['sexo']=teste

    p['idade']=int(input(f'Quantos anos \033[1m{p["nome"]}\033[m tem? R: '))
    pessoas.append(p)

    while 'N'!=teste!='S':
        teste=input('Deseja cadastrar mais uma pessoa? Digite S ou N: ').strip().upper()
    if teste in 'nN':
        break

    print('\033[1mContinuando...\033[m')
    sleep(1)

print('\033[1mAnalizando dados...\033[m')
sleep(2.5)


# Dados da a):
print('^-'*30+'^')
print(f'Foram cadastradas um total de \033[1m{len(pessoas)} pessoas\033[m;')
print('^-'*30+'^')
sleep(1)
input('\nPressione Enter para continuar \n')
sleep(1)

# Dados da b):
total_idade=0
for dic in pessoas:
    total_idade+=dic['idade']
media_idade=total_idade/len(pessoas)
print('^-'*30+'^')
print(f'A \033[1mmédia de idade\033[m de todas as pessoas cadastradas é de \033[1m{media_idade:.1f}\033[m anos;')
print('^-'*30+'^')
sleep(1)
input('\nPressione Enter para continuar \n')
sleep(1)

# Dados da c):
print('^-'*30+'^')
print('Todas as mulheres cadastradas: ')
sleep(1.5)
c=0
for dic in pessoas:
    if dic['sexo'] == 'F':
        c+=1
        print(f'{c}ª mulher: \033[1m{dic["nome"]}\033[m.')
        sleep(1)
print('^-'*30+'^')
sleep(1)
input('\nPressione Enter para continuar \n')
sleep(1)

# Dados da d):
print('^-'*30+'^')
print('Todas as pessoas com a idade acima da média citada anteriormente: ')
sleep(2)
for dic in pessoas:
    if dic['idade']>media_idade:
        print(f"\033[1m{dic['nome']}\033[m, com \033[1m{dic['idade']}\033[m anos de idade;")
        sleep(1)
print('^-'*30+'^')
sleep(2)

print('\n\033[1mFim dos dados. Agradeço a preferência!\033[m')