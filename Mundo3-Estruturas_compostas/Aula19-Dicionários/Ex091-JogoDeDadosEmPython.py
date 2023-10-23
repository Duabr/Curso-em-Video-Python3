# 4 jogadores jogam um dado de 6 lados cada um, quem tirar o maior número ganha.
# Sistematicamente, gera 4 números aleatórios entre 1 e 6 e os guarda em um dicionário.
# No fim, mostra o vencedor e os números em ordem crescente.
# (Que exercício difícil de fazer sem a solução dada no vídeo)
from random import randint
from time import sleep
resultados = {}
print('\033[1mSorteando números...\033[m')
sleep(2)
for c in range(4):
    resultados[f'{c+1}º jogador']=randint(1,6)
for jog, num in resultados.items():
    print(f'{jog}: Tirou o número \033[1m{num}\033[m no dado.')
    sleep(2)

numeros=[]
jogadores=[]
for j, n in resultados.items():
    jogadores.append(j)
    numeros.append(n)

maior={}
menor={}
jog_maior={}
jog_menor={}
for c in range(2):
        jog_maior[f'{c+1} maior']=jogadores[numeros.index(max(numeros))]
        maior[f'{c+1} maior']=max(numeros)
        del jogadores[numeros.index(maior[f'{c+1} maior'])]
        del numeros[numeros.index(maior[f'{c+1} maior'])]
        jog_menor[f'{c+1} menor']=jogadores[numeros.index(min(numeros))]
        menor[f'{c+1} menor']=min(numeros)
        if c==0:# # Para impedir alguns erros, só deleta parte dos itens na primeira rodada do for.
            del jogadores[numeros.index(menor[f'{c+1} menor'])]
            del numeros[numeros.index(menor[f'{c+1} menor'])]
            quanti_maiores=numeros.count(maior[f'{c+1} maior'])


print(f"Em primeiro lugar ficou o \033[1m{jog_maior['1 maior']}\033[m com o número \033[1m{maior['1 maior']}\033[m.")
sleep(2)
print(f"Em ordem crescente, os outros números foram sorteados: \033[1m{maior['2 maior']}, {menor['2 menor']} e {menor['1 menor']}.\033[m")
print(f"Sortedos pelos seguintes jogadores: \033[1m{jog_maior['2 maior']}, {jog_menor['2 menor']} e {jog_menor['1 menor']}.\033[m")

