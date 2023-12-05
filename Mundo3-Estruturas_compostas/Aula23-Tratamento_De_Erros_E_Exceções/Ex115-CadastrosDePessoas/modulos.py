from time import sleep

def cadastro(arqui, nome, idade):
    """Cadastra nome e idade lidos em um arquivo de texto de forma tabulada

    Args:
        arqui (str): arquivo de texto usado
        nome (str): nome da pessoa, mostrada à direita
        idade (int): idade da pessoa, mostrada à esquerda do nome
    """
    open(arqui, 'a', encoding='utf-8').write(f'{nome:<30}{idade}\n')
    

def listar(arqui, lin=40):
    """Função feita para mostrar o conteúdo de um arquivo de texto.

    Args:
        arqui (str): o caminho do arquivo.
        lin (int, optional): o número de ífens mostrados acima e abaixo
        do conteúdo do arquivo. Defaults to 40.
    """
    conteu = open(arqui, encoding='utf-8').read()
    print('-'*lin)
    print(conteu[:-1])
    print('-'*lin)


def validarinp(para, pri=''):
    """Lê um valor (val) até que ele seja válido (val in para).

    Args:
        para (any): um único valor contendo todos os valores que validarão val
        pri (str, optional): o que será mostrado no terminal na hora de ler val. Defaults to ''.

    Returns:
        str: o valor lido.
    """
    val = input(pri)
    while val not in para or val=='':
        print('\033[1;31mValor inválido.\033[m')
        sleep(0.5)
        val = input(pri)
    return val


def leiaint(pri=''):
    """Lê um valor continuamente até que seja digitado um número inteiro.

    Args:
        pri (str, optional): o que será mostrado no terminal. Defaults to ''.

    Returns:
        int: valor lido, conforme explicado
    """
    val = input(pri)
    while not val.isnumeric():
        print('\033[1;31mValor inválido.\033[m')
        sleep(0.5)
        val = input(pri)
    return val
