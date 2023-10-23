# Um "auxílio" para a mega sena: pergunta quantos jogos o usuário quer jogar e então,
# para cada jogo, sorteia 6 números aleatórios de 1 a 60, sem repetições de números dentro de um jogo.
from time import sleep
from random import randint

quanti=int(input('Quantos jogos você deseja jogar? '))

jogos=[]
for c in range(quanti):
    jogos.append([])
    while len(jogos[c]) < 6:
        num=randint(1,60)
        if num not in jogos[c]:
            jogos[c].append(num)

for c, j in enumerate(jogos):
    print(f'{c+1}º jogo: \033[1m{j}\033[m')
    sleep(1)

print('\033[1;32mTODOS OS JOGOS FORAM GERADOS\033[m')