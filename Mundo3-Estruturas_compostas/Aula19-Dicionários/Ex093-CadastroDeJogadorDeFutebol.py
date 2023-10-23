# Gerenciamento do aproveitamento de um jogador de futebol: lê o nome, o números de jogos em um campeonato e o número
# de gols feitos pelo jogador em cada jogo. No fim, mostra todos os dados, incluindo o total gols feitos e a média de gols por jogo.
from time import sleep
jogador = {'nome':input('Digite o nome do(a) jogador(a): ')}
jogador['num jogos']=int(input(f'Quantos jogos \033[1m{jogador["nome"]}\033[m jogou nesse campeonato? R: '))
gols_jogos=[]
total_gols=0
for c in range(jogador['num jogos']):
    gols_jogos.append(int(input(f'Quantos gols \033[1m{jogador["nome"]}\033[m fez no \033[1m{c+1}º\033[m jogo? R: ')))
    total_gols+=gols_jogos[c]
jogador['gols']=gols_jogos
jogador['total gols']=total_gols
jogador['media']=f'{total_gols/jogador["num jogos"]:.2f}'

print('^-'*30+'^')
print(f'\033[1m{jogador["nome"]}\033[m fez um total de \033[1m{jogador["total gols"]}\033[m gols em todos os jogos;')
sleep(2)
for jogo, gol in enumerate(jogador['gols']):
    print(f'    \033[1m{gol}\033[m gol(s) no \033[1m{jogo+1}º jogo\033[m;')
    sleep(1)
sleep(1)
print(f'Dando uma média de \033[1m{jogador["media"]}\033[m de gols por jogo.')
sleep(2)
print('^-'*30+'^')
