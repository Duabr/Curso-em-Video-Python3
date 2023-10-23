# Lê um número entre 0 e 20 e mostra na tela esse número por extenso (ex: 0, 'zero'; 1, 'um').
n_extenso=('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez',
           'onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

contador=int(input('Quantos números você deseja escrever? R: '))-1
n_escolha=int(input('Digite um dos números, entre 0 e 20: '))

print(f'O número \033[1m{n_escolha}\033[m, escrito por extenso, fica \033[1m{n_extenso[n_escolha]}\033[m.')
for i in range(contador):
    n_escolha=int(input('Digite mais um número, entre 0 e 20: '))
    while n_escolha<0 or n_escolha>20:
        n_escolha=int(input('\033[1;31mNúmero inválido!\033[m Digite um número entre 0 e 20: '))
    print(f'O número \033[1m{n_escolha}\033[m, escrito por extenso, fica \033[1m{n_extenso[n_escolha]}\033[m.')

print('\033[1;32mObrigado por usar meu código :)\033[m')