# Com uma função (vou parar de citar essa parte), lê o nome de um jogador e quantos gols ele fez.
# Ambos esses valores são opcionais.
def ficha(nome='<desconhecido>', gols=0):
    print('^-'*30+'^')
    print(f'O(a) jogador(a) \033[1m{nome}\033[m fez um total de \033[1m{gols}\033[m gol(s).')
    print('^-'*30+'^')


nome=input('Qual é o nome do(a) jogador(a)? ').strip()
gols=input(f'Quantos gols ele(a) marcou? ').strip()

if nome!='' and gols.isnumeric():
    ficha(nome, gols)
elif nome=='' and gols.isnumeric():
    ficha(gols=gols)
elif nome!='' and not gols.isnumeric():
    ficha(nome=nome)
else:
    ficha()
