# Adiciona uma nova função chamada "resumo", que mostra os valores retornados pelas outras funções do módulo.
from moeda import resumo
from time import sleep

valor = float(input('Digite um número qualquer: '))
porc_mais = float(input('Digite um valor em porcentagem para aumentar o número: '))
porc_menos = float(input('Agora digite um para diminui-lo: '))
teste = input('Deseja que os números sejam convertidos em moeda? S ou N: ').strip().upper()
if teste=='S':
    teste = True
else:
    teste = False
print('\033[1mAnalizando...\033[m')
sleep(3)

resumo(valor, porc_mais, porc_menos, teste)