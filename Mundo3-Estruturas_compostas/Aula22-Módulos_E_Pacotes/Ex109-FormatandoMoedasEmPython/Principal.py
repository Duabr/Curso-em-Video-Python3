# Com as funções do módulo "moeda" modificadas para receber um parâmetro opcional chamado "format", esse
# parâmetro define se a formatação em moeda será feita.
import moeda
from time import sleep

num = float(input('Digite um valor qualquer: '))
teste = input('Deseja que o valor seja mostrado em forma de real? Digite S ou N: ').strip().upper()
sleep(1)
if teste == 'S':
    teste = True
    num_form = moeda.moeda(num)
else:
    teste = False
    num_form = num

print('\n'+'^-'*30+'^')
print(f'A metade de \033[1m{num_form}\033[m é igual à \033[1;32m{moeda.metade(num, teste)}\033[m.')
sleep(2)
print(f'O dobro de \033[1m{num_form}\033[m é igual à \033[1;31m{moeda.dobro(num, teste)}\033[m.')
sleep(2)
print('^-'*30+'^')

por = float(input('Digite um número para porcentagem: '))
print('^-'*30+'^')
print(f'\033[1m{num_form}\033[m com {por}% de desconto fica: \033[1;32m{moeda.diminuir(num, por, teste)}\033[m.')
sleep(2)
print(f'\033[1m{num_form}\033[m com {por}% de juros fica: \033[1;31m{moeda.aumentar(num, por, teste)}\033[m')
sleep(2)
print('^-'*30+'^')
