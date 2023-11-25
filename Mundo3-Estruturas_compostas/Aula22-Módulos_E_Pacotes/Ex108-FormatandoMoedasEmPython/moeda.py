# Funções utilizadas no exercício.

# Adicionada no Ex107
def aumentar(n, por):# Número, porcentagem
    """Aumenta um número em certa porcentagem.

    Args:
        n (int/float): número a ser aumentado
        por (int/float): porcentagem para aumentar o número

    Returns:
        int/float: resultado do número aumentado
    """
    return n + (n * por / 100)


# Adicionada no Ex107
def diminuir(n, por):# Número, porcentagem
    """Diminui um número em certa porcentagem.

    Args:
        n (int/float): número a ser diminuído
        por (int/float): porcentagem para diminuir o número

    Returns:
        int/flaot: resultado do número diminuído
    """
    return n - (n * por / 100)


# Adicionada no Ex107
def dobro(n):# Número
    """Dobra um número dado.

    Args:
        n (int/float): número a ser dobrado

    Returns:
        int/float: resultado do número dobrado
    """
    return n*2


# Adicionada no Ex107
def metade(n):# Número
    """Divide um número por dois.

    Args:
        n (int/float): número a ser dividido

    Returns:
        float: resultado do número dividido
    """
    return n/2


# Adicionada no Ex108
def moeda(val):# Valor
    """Formata um número int ou float em valor de moeda, em real.
    Ex: "108" vira "R$108,00".

    Args:
        val (int/float): número que será formatado.

    Returns:
        str: valor formatado.
    """
    val = f'R${val:.2f}'.replace('.', ',')
    return val
