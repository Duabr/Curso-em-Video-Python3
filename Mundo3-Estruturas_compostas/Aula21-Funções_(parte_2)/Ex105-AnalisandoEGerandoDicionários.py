# Analisando várias notas de alunos, retorna as seguintes informaões: 
# a) Quantia de notas dadas.
# b) A maior nota dada
# c) A menor nota dada.
# d) A média das notas.
# e) A situação da média (argumento opcional).
from time import sleep

def notas(*n, sit=False):
    """Analisa diversas notas dadas, retornando um dicionário com vários valores.

    Args:
        sit (bool, optional): Se a situação da média será mostrada. Defaults to False.

    Returns:
        dict: Número de notas (int);
    Maior nota (float);
    Menor nota (float);
    Média das notas (float);
    Situação da média (str, optional).
    """
    dic = {'num':len(n)}
    dic['maior'] = float(max(n))
    dic['menor'] = float(min(n))
    dic['media'] = float(f'{sum(n)/len(n):.1f}')# Número float formatado para um número após o ponto.
    dic['situaçao']=''
    if sit and dic['media']<5:
        dic['situaçao'] = 'RUIM'
    elif sit and 5<=dic['media']<7:
        dic['situaçao'] = 'ACEITÁVEL'
    elif sit and dic['media']>=7:
        dic['situaçao'] = 'BOA'
    return dic


nums = notas(6, 2, 9, 4, 3.5, sit=True)

print('^-'*20+'^')
print(nums)
sleep(3)
print('^-'*20+'^')

print(f'Número de notas analisadas: {nums['num']}')
sleep(1.5)
print(f'Maior nota: {nums['maior']}')
sleep(1.5)
print(f'Menor nota: {nums['menor']}')
sleep(1.5)
print(f'Média das notas: {nums['media']}')
sleep(1.5)
if nums['situaçao']!='':
    print(f'Situação da média: {nums['situaçao']}')
sleep(3)

print('^-'*20+'^')

if input('Mostrar documentação da função? [S/N]').strip().upper()=='S':
    help(notas)
