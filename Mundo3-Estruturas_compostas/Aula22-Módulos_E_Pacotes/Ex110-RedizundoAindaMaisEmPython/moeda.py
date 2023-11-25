# Funções utilizadas no exercício.

# Adicionada no Ex107, atualizada no Ex109
def aumentar(n, por, form=False):# Número, porcentagem, formatação
    """Aumenta um número em certa porcentagem.

    Args:
        n (int/float): número a ser aumentado
        por (int/float): porcentagem para aumentar o número
        form (bool, optional): Caso True, formata o valor retornado para real com a função "moeda". Defaults to False.

    Returns:
        int/float/str: resultado do número aumentado, formatado em reais caso format = True
    """
    val = n + (n * por / 100)
    if form:
        return moeda(val)
    else:
        return val


# Adicionada no Ex107, atualizada no Ex109
def diminuir(n, por, form=False):# Número, porcentagem, formatação
    """Diminui um número em certa porcentagem.

    Args:
        n (int/float): número a ser diminuído
        por (int/float): porcentagem para diminuir o número
        form (bool, optional): Caso True, formata o valor retornado para real com a função "moeda". Defaults to False.

    Returns:
        int/flaot/str: resultado do número diminuído, formatado em reais caso format = True
    """
    val = n - (n * por / 100)
    if form:
        return moeda(val)
    else:
        return val


# Adicionada no Ex107, atualizada no Ex109
def dobro(n, form=False):# Número, formatação
    """Dobra um número dado.

    Args:
        n (int/float): número a ser dobrado
        form (bool, optional): Caso True, formata o valor retornado para real com a função "moeda". Defaults to False.

    Returns:
        int/float/str: resultado do número dobrado, formatado em reais caso format = True
    """
    val = n*2
    if form:
        return moeda(val)
    else:
        return val


# Adicionada no Ex107, atualizada no Ex109
def metade(n, form=False):# Número, formatação
    """Divide um número por dois.

    Args:
        n (int/float): número a ser dividido
        form (bool, optional): Caso True, formata o valor retornado para real com a função "moeda". Defaults to False.

    Returns:
        float/str: resultado do número dividido, formatado em reais caso format = True
    """
    val = n/2
    if form:
        return moeda(val)
    else:
        return val
    

# Adicionada no Ex108
def moeda(val):
    """Formata um dado valor em reais (R$val, com dois números após a vírgula).

    Args:
        val (int/float): o valor a ser formatado

    Returns:
        float: formatação feita do valor.
    """
    val = f'R${val:.2f}'.replace('.', ',')
    return val


# Adicionada no Ex110
def resumo(val, aum, dimi, form=False):# Valor, aumento (%), diminuição (%)
    """Mostra o resumo de um valor numérico, usando as outras funções desse mesmo módulo.

    Args:
        val (int/float): valor a ser analizado
        aum (int/float): juros do valor, em porcentagem
        dimi (int/float): desconto do valor, em porcentagem
        form (bool, optional): se os valores serão formatados para moeda (em real). Defaults to False.
    """
    if form:
        preço_form = moeda(val)
    else:
        preço_form = val

    print('-'*30)
    print(f'{'RESUMO DOS VALORES':^30}')
    print(f'{preço_form:^30}')
    print('-'*30)

    print(f'Metade: \033[1;32m{metade(val, form)}\033[m.')
    print(f'Dobro: \033[1;31m{dobro(val, form)}\033[m.')
    print(f'{dimi}% de desconto: \033[1;32m{diminuir(val, dimi, form)}\033[m.')
    print(f'{aum}% de juros: \033[1;31m{aumentar(val, aum, form)}\033[m.')

    print('-'*30)