# Módulo adicionado no Ex111, mas só é utilizado no Ex112.
from time import sleep

def leianum(pri=''):
    """Função que lê somente um valor que seja somente int ou float (seja o último com vírgula ou ponto).

    Args:
        inp (any, optional): O que será mostrado no terminal na hora de ler o valor. Defaults to ''.

    Returns:
        float: o valor lido, caso ele seja válido (como estabelecido acima).
    """
    inp, teste = '', False
    while not teste:
        inp = input(pri).replace(',', '.')
        teste = inp.replace('.','').isdigit() and not inp.count('.')>1
        if not teste:
            print('\033[1;31mValor inválido\033[m')
            sleep(1)
    return float(inp)


# Essa função não foi pedida no exercício, mas decidi fazê-la do mesmo jeito.
def leiaresp(inp=''):
    """Função que lê somente dois possíveis valores: 'S' ou 'N', ou seja, "sim" ou "não".
    "strip()" e "upper()" já são utilizados na leitura do valor.

    Args:
        inp (any, optional): O que será mostrado no terminal na hora de ler o valor. Defaults to ''.

    Returns:
        str: valor lido, caso ele válido (como estabelecido acima).
    """
    resp, teste = '', False
    while not teste:
        resp = input(inp).strip().upper()
        teste = resp=='S' or resp=='N'
        if not teste:
            print('\033[1;31mValor inválido\033[m')
            sleep(1)
    return resp
