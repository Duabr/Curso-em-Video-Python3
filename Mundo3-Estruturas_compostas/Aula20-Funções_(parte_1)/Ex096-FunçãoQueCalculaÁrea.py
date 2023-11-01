# Utilizando-se de uma função, calcula a área de um terreno de acordo com sua largura e seu comprimento.
from time import sleep

def area(lar, com):
    print(f'A área do terreno \033[1m{lar}m X {com}m\033[m é de \033[1m{lar*com:.2f}m²\033[m.')


print(f'\033[1m{'Cálculo de área de terreno':-^70}\033[m')  
area(float(input('Digite a \033[1mlargura\033[m do terreno (em metros): ')), float(input('Agora digite o \033[1mcomprimento\033[m (em metros): ')))