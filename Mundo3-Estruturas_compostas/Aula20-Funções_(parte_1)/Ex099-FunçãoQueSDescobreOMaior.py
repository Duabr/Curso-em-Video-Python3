# Com uma função, analisa diversos valores para mostrar qual deles é o maior. Também mostra quantos valores foram analisados.
from time import sleep

def maior(*num):
    print('\033[1mAnalisando...\033[m', flush=True)
    sleep(2)
    maior=max(num,default='* (nenhum número encontrado)')# O parâmetro "default" define o que será retornado caso nenhum valor seja inserido na chamada da função

    print('Dentre os números dados: ', end='')
    quanti=0
    for n in num:
        print(f'{n}', end=' ', flush=True)
        quanti+=1
        sleep(0.25)

    print(';', flush=True)
    sleep(2)
    print(f'O maior número encontrado, dos {quanti} números, foi o \033[1m{maior}\033[m.')
    print(f'^-'*40+'^', flush=True)
    sleep(3)
    

print(f'^-'*40+'^')
maior(1, 2, 7, 3, 2, 66, 33, 17, 12, 52)
maior(2, 5, 7, 1, 4)
maior(1, 999)
maior(2)
maior()
