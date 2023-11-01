# Criando uma função "contador" para realizar contagens com início, fim e passo. Serão feitas as seguintes contagens:
# a) De 1 até 10, de 1 em 1
# b) De 10 até 0, de 2 em 2
# c) Uma contagem personalizada, dada pelo usuário
from time import sleep

def contador(i, f, p):# (Início, fim, passo)
    if p==0:
        p=1
    elif p<0 and not i>f:
        p=-p

    print('-'*50)
    print(f'{i} até {f}, pulando de {p} em {p}:')
    sleep(2)

    if i>f and not p<0:
        p=-p
    if i>f:
        f-=2
    
    for c in range(i, f+1, p):
        print(c, end=' ', flush=True)# Esse flush só descobri na resolução do vídeo. Só coloquei aqui pois é algo puramente estético.
        sleep(0.25)

    print()
    print('-'*50)


contador(1, 10, 1)
contador(10, 0, 2)

print('Agora, crie sua própria sequência;')
sleep(2)
nums={'i':int(input('Início: ')), 'f':int(input('Fim: ')), 'p':int(input('Passo: '))}
contador(nums['i'], nums['f'], nums['p'])

# Vendo o a solução, percebi que a minha versão ficou um pouco mais complicada. Hehe