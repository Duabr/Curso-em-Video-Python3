# Armazena carnes e seus respectivos preços em uma tupla e mostra, de forma tabelada, os detalhes de cada produto.
carnes = ('Coxão mole',37.50, 'Patinho',34.50, 'Carne bovina moída',29.90,
          'Bisteca suína',16.80, 'Pernil suíno',14.50, 'Pé de porco',7.99,
          'Linguiçinha pura',25.30, 'Coxinha das asas',13.99)

print(f'{"AÇOUGUE PALMEIRA":-^50}')
c=0
for _ in range(len(carnes)//2):
    print(f'{carnes[c]:_<30}',end='')
    c+=1
    print(f'R${carnes[c]:.2f}')
    c+=1
print('-'*50)
