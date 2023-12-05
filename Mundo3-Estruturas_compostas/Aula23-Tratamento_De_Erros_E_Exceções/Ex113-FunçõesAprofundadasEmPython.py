# Igual ao Ex104-ValidandoEntradaDeDadosEmPython, mas usando tratamento de erros ("try" e "except").
from time import sleep

def leiaint(pri=''):
    """Lê valor somente inteiro. Qualquer outro tipo de valor digitado não
    será aceito. Continua lendo o valor até ele ser considerado válido.

    Args:
        pri (str, optional): mensagem de output. Defaults to ''.

    Returns:
        int/str: número lido, caso ele seja válido. No caso de "KeyboardInterrupt" retorna uma mensagem.
    """
    n = None
    while type(n) != int:
        try:
            n = int(input(pri))
        except ValueError:
            print('\033[1;31mValor digitado é inválido.\033[m')
            sleep(1)
        except KeyboardInterrupt:
            print('\n\033[1;31mPrograma ecerrado antes do previsto.\033[m')
            sleep(1)
            break
    return n if n != None else '<valor não informado>'

def leiafloat(pri=''):
    """Lê valor inteiro ou float. Qualquer outro tipo de valor digitado não
    será aceito. Continua lendo o valor até ele ser considerado válido.

    Args:
        pri (str, optional): mensagem de output. Defaults to ''.

    Returns:
        float/str: número lido, caso ele seja válido. No caso de "KeyboardInterrupt" retorna uma mensagem.
    """
    n = None
    while int != type(n) != float:
        try:
            n = float(input(pri))
        except ValueError:
            print('\033[1;31mValor digitado é inválido.\033[m')
            sleep(1)
        except KeyboardInterrupt:
            print('\n\033[1;31mPrograma encerrado antes do previsto.\033[m')
            sleep(1)
            break
    return n if n != None else '<valor não informado>'


inteiro = leiaint('Digite um número inteiro: ')
real = leiafloat('Digite um número inteiro ou com vírgula: ')

print('^-'*25+'^')
print(f'O número inteiro digitado foi \033[1m{inteiro}\033[m e o número real foi \033[1m{real}\033[m.')