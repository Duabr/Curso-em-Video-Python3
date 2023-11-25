# Programa principal.
# Com funções vindas de outro arquivo (módulo), faz alguns cálculos com um preço lido:
# aumento de 10%; diminuição de 15%; dobramento do preço; divisão por 2 do preço.
import moeda

num = float(input('Digite um preço: R$'))

print(f'Com um aumento de 10%: R${moeda.aumentar(num, 10):.2f}')
print(f'Com 15% de desconto: R${moeda.diminuir(num, 15):.2f}')
print(f'Dobro do preço: R${moeda.dobro(num):.2f}')
print(f'Metade do preço: R${moeda.metade(num):.2f}')
