# Pequeno sistema de cadastros de pessoas, salvando o nome e idade de cada um em um arquivo de texto.
# Com essse sistema será possível cadastrar uma pessoa nova e ver a lista de todos os cadastros.
from modulos import *
from time import sleep
try:
    arquivo = open(r'C:\Trabaio\Curso-em-Video-Python3\Mundo3-Estruturas_compostas\Aula23-Tratamento_De_Erros_E_Exceções\Ex115-CadastrosDePessoas\Cadastros.txt')
    arquivo.close()
except FileNotFoundError:
    arquivo = open(r'C:\Trabaio\Curso-em-Video-Python3\Mundo3-Estruturas_compostas\Aula23-Tratamento_De_Erros_E_Exceções\Ex115-CadastrosDePessoas\Cadastros.txt', 'w')
    arquivo.write(f'{'NOME':<30}IDADE')
    arquivo.close()
    print('Arquivo criado com êxito.')
    sleep(2)

while True:
    print('-'*40)
    print('  \033[1mMENU PRINCIPAL\033[m')
    print('-'*40)
    print('''\033[1;36m1. Cadastrar uma nova pessoa
2. Visualizar todas as pessoas cadastradas
3. Encerrar código\033[m''')
    print('-'*40)
    opc = validarinp('123', '\033[1;36mDigite o número da ação desejada: \033[m').strip()
    arquivo = r'C:\Trabaio\Curso-em-Video-Python3\Mundo3-Estruturas_compostas\Aula23-Tratamento_De_Erros_E_Exceções\Ex115-CadastrosDePessoas\Cadastros.txt'

    if opc=='1':
        print('-'*40)
        nome = input('\033[1;33mDigite o nome da pessoa: \033[m')
        idade = leiaint('\033[1;33mAgora digite sua idade: \033[m')
        cadastro(arquivo, nome, idade)
        print('\033[1;33mCadastro concluído com sucesso!\033[m')
        sleep(2)

    elif opc=='2':
        listar(arquivo)
        sleep(2)
        input('Pressione Enter para continuar ')

    elif opc=='3':
        print('-'*40)
        print('\033[1mCódigo encerrado. Agradeço a preferência!\033[m')
        sleep(1)
        break
