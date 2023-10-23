# Versão aprimorada do Ex093-CadastroDeJogadorDeFutebol, em que poderam ser cadastrados vários jogadores ao invés deum só,
# e no fim mostra os detalhes de cada jogador de forma tabelada. O usuário pode ainda ver os detalhes de um jogador específico.
from time import sleep

jogadores=[]
while True:
    jog_atual = {}
    jog_atual['nome'] = input('Digite o nome do(a) jogador(a): ')
    jog_atual['num jogos'] = int(input(f'Quantos jogos \033[1m{jog_atual["nome"]}\033[m jogou? R: '))
    jog_atual['gols'] = []
    for c in range(jog_atual['num jogos']):
        jog_atual['gols'].append(int(input(f'Quantos gols \033[1m{jog_atual["nome"]}\033[m fez no \033[1m{c+1}º\033[m jogo? R: ')))
    jog_atual['total gols'] = sum(jog_atual['gols'])
    jog_atual['media gols'] = f"{jog_atual['total gols']/jog_atual['num jogos']:.1f}"
    jogadores.append(jog_atual)

    resp = ''
    while 'N'!= resp!= 'S':
        resp = input('Deseja cadastrar mais algum(a) jogador(a)? Digite "S" ou "N": ').strip().upper()
    print('^-'*35+'^')
    if resp[0] == 'N':
        break

print('\033[1mAnalizando e organizando dados...\033[m')
sleep(2)

print(f"{'NUM':-<6}{'NOME':-<15}{'NUM JOGOS':-<12}{'TOTAL GOLS':-<15}MEDIA GOLS")
for c, dic in enumerate(jogadores):
    print(f"{f'{c+1}'+'º':<6}{dic['nome']:<15}{dic['num jogos']:<12}{dic['total gols']:<15}{dic['media gols']}")
print('-'*48)

while True:
    resp=-1
    while resp<0 or resp>len(jogadores):
        resp=int(input('Deseja ver os dados de qual jogador? Digite o número correspondente (ou 0 para encerrar): '))
        if resp<0 or resp>len(jogadores):
            print('\033[31mPor favor, digite um número válido.\033[m')
    if resp==0:
        break
    print(f'Jogador n° \033[1m{resp}\033[m: fez um total de \033[1m{jogadores[resp-1]["total gols"]}\033[m gols em \033[1m{jogadores[resp-1]["num jogos"]}\033[m jogos; ')
    sleep(2)
    for jogo, gol in enumerate(jogadores[resp-1]['gols']):
        print(f'\033[1m{gol}\033[m gol(s) no \033[1m{jogo+1}º\033[m jogo;')
        sleep(1)
    sleep(1)
    print(f'Dando um média de \033[1m{jogadores[resp-1]["media gols"]}\033[m gols por jogo.')
    sleep(2)

print('\033[1mFim do código. Agradeço a preferência!\033[m')