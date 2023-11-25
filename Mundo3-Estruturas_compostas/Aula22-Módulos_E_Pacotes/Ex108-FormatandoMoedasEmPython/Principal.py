# Nova versão do "Ex107-ExercitandoMódulosEmPython.py", adicionando um nova função "moeda" ao módulo "moeda"
# que formata o valor dado para moeda em real. Ex: de "108" para "R$108,00".
from moeda import moeda, metade, dobro, aumentar, diminuir
from time import sleep

val = float(input('Digite um valor qualquer: '))
sleep(1)

print(f'\n\033[1m{moeda(val)}\033[m dividido por 2 fica: \033[1;32m{moeda(metade(val))}\033[m.')
sleep(2)
print(f'O dobro de \033[1m{moeda(val)}\033[m é igual à \033[1;31m{moeda(dobro(val))}\033[m.')
sleep(2)

por = float(input('\nDigite um número para porcentagem: '))
print(f'\033[1m{moeda(val)}\033[m com {por}% de desconto fica \033[1;32m{moeda(diminuir(val, por))}\033[m.')
sleep(2)
print(f'\033[1m{moeda(val)}\033[m com {por}% de juros fica \033[1;31m{moeda(aumentar(val, por))}\033[m.')