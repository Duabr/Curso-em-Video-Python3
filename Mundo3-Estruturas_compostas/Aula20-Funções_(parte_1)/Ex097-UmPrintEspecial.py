# Escreve algumas frases juntamente com linhas que acompanham o tamanho da dela.
# Depois, pede se o usuário quer escrever alguma frase para vê-la da mesma forma, ou seja, com as linhas.
from time import sleep

def frases(f):
    print(f'{'-':-^{len(f)+5}}')
    print(f'{f:^{len(f)+5}}')
    print(f'{'-':-^{len(f)+5}}')


frases('Atividades feitas!')
sleep(1)
frases('"Procure vantagens nos seus defeitos."')
sleep(1)
frases('"Now you, who have set foot in this world..."')
sleep(1)

while True:
    teste=''
    while 'N'!=teste!='S':
        teste=input('Deseja escrever uma frase para deixá-la da mesma forma que as outras? Responta S ou N: ').strip().upper()
    if teste=='N':
        break
    frases(input('Digite a frase desejada: '))
    sleep(2)

print('\033[1mFim do programa. Espero que tenha se divertido!\033[m')