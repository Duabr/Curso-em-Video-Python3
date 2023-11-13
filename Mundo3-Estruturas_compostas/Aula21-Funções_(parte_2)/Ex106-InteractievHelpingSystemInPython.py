# Função que ajuda na utilização do Interactive Help do Python.
from time import sleep

def int_help(teste):
    while teste!='':
        teste=input('\033[1mDigite o nome de uma função interna do Python (ou aperte Enter para finalizar): ')
        if teste!='':
            print('Carregando documentação...')
            sleep(3)
            print('\033[1;32m')
            help(teste)
            print('\033[m')
            sleep(2)
    print()
    print(f'{'Fim do código':=^60}')


int_help('a')