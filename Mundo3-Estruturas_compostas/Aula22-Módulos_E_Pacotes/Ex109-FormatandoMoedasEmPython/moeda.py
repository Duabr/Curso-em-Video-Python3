# Funções utilizadas no exercício.

# Adicionada no Ex107, atualizada no Ex109
def aumentar(n, por, form=False):# Número, porcentagem, formatação
    """Aumenta um número em certa porcentagem.

    Args:
        n (int/float): número a ser aumentado
        por (int/float): porcentagem para aumentar o número
        format (bool, optional): Caso True, formata o valor retornado para real com a função "moeda". Defaults to False.

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
        format (bool, optional): Caso True, formata o valor retornado para real com a função "moeda". Defaults to False.

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
        format (bool, optional): Caso True, formata o valor retornado para real com a função "moeda". Defaults to False.

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
        format (bool, optional): Caso True, formata o valor retornado para real com a função "moeda". Defaults to False.

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
    """Formata um dado valor em reais (R$n, com dois números após a vírgula).

    Args:
        val (int/float): o valor a ser formatado

    Returns:
        float: formatação feita do valor.
    """
    val = f'R${val:.2f}'.replace('.', ',')
    return val