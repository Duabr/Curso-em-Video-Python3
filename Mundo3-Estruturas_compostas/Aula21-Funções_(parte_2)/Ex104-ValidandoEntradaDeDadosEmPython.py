# Criação de uma função semelhante ao "input()", chamada "leiaint()". Essa função aceita somente números inteiros.
from time import sleep

def leiaint(msg):
    """Lê valor somente inteiro. Qualquer outro tipo de valor digitado não
    será aceito. Continua lendo o valor até ele ser considerado válido.

    Args:
        msg (literal): mensagem de output.

    Returns:
        int: número inteiro digitado.
    """
    n=''
    while not n.isnumeric():
        n = input(msg)
        if not n.isnumeric():
            print('\033[1;31mValor inválido.\033[m')
            sleep(1)
    return n


n = leiaint('Digite um número inteiro: ')
print(f'O número digitado foi: \033[1m{n}\033[m.')
