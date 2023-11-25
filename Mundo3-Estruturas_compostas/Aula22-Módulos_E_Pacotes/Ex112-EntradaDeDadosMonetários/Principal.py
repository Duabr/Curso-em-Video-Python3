# Basicamente o mesmo código do Ex110. Dessa vez, com duas novas funções: "leianum" e "leiaresp".
from UtilidadesCeV import dado, moeda
val = dado.leianum('Digite um valor qualquer: ')
mais = dado.leianum('Digite um valor para porcentagem: ')
menos = dado.leianum('Digite outro: ')
teste = dado.leiaresp('Deseja que os valores sejam convertidos em real? [S/N] ').strip().upper()
if teste=='S':
    teste = True
else:
    teste = False

moeda.resumo(val, mais, menos, teste)

