# Com uma função de dois parâmetros chamada "fatorial", calcula o fatorial de um número dado.
# o primeiro parâmetro é o número a ser calculado o fatorial, enquanto o segundo parâmetro "show" definirá se
# o processo da conta será mostrado ou não na tela ("False" como valor padrão).
def fatorial(num, show=False):
    """Cálculo de fatorial.

    Args:
        num (int): Número a ser calculado seu fatorial
        show (bool, optional): Se o processo da conta será mostrado. Defaults to False.
    """
    from time import sleep

    print('-'*40)
    print(f'Fatorial de \033[1m{num}\033[m:')
    sleep(2)
    resul = num
    for c in range(num, 1, -1):
        if show:
            print(f'{c} x ', end='', flush=True)
        if c!=num:
            resul *= c
    if show:
        print(f'1 = \033[1m{resul}\033[m')
    else:
        print(f'O resultado do fatorial de \033[1m{num}\033[m deu \033[1m{resul}\033[m.')
    sleep(3)


fatorial(4, True)
fatorial(3)
fatorial(7, True)

print()
help(fatorial)