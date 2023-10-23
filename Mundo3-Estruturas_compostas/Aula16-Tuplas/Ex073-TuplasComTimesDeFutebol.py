# Em uma tebela, está os 20 primeiros times colocados do Campeonato Brasileiro de Futebol 2023 até setembro.
# Depois, Mostra as seguintes informações:
# a) Mostrar os 5 primeiros colocados 
# b) Mostrar os 4 últimos colodados
# c) Mostrar todos os times em ordem alfabética
# d) Mostrar em qual posição está o time do Flamengo (o enuncioado pedia a colocação do time da Chapecoense, mas ele não está na tebela atual).
from time import sleep
tabela_brasileirao=('Botafogo','Palmeiras','Grêmio','Flamengo','Fluminense','Bragantino','Ahtletico-PR','Fortaleza','Atlético-MG','Cuiabá',
                    'São Paulo','Cruzeiro','Corinthians','Internacional','Goiás','Bahia','Santos','Vasco da Gama','América-MG','Coritiba')
print('-'*50)
print(f'Tabela completa do Brasileirão de Setembro de 2023:')
sleep(2)
for c in range(20):
    print(f'{c+1}º Lugar: \033[1m{tabela_brasileirao[c]}\033[m')
print('-'*50)
input('Pressione Enter para continuar ')

print('-'*50)
print('Os 5 primeiros colocados são:')
sleep(2)
for c in range(5):
    print(f'{c+1}º Lugar: \033[1m{tabela_brasileirao[c]}\033[m')
print('-'*50)
input('Pressione Enter para continuar ')

print('-'*50)
print('Os 4 últimos colocados são: ')
sleep(2)
for c in range(4):
    print(f'{-c+20}º Lugar: \033[1m{tabela_brasileirao[-c-1]}\033[m')
print('-'*50)
input('Pressione Enter para continuar ')

tabela_ordem_alfa=sorted(tabela_brasileirao)
print('-'*50)
print('A tabela em ordem alfabética: ')
sleep(2)
for c in range(20):
    print(f'\033[1m{tabela_ordem_alfa[c]}\033[m')
print('-'*50)
input('Pressione Enter para continuar ')

print('-'*50)
print(f'O time do Flamengo está na {tabela_brasileirao.index("Flamengo")+1}ª posição.')
print('-'*50)
