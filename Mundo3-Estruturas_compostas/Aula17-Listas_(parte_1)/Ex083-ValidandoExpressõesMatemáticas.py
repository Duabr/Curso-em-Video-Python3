# Lê uma expressão matemática qualquer e analisa se os parênteses dela estão corretos.
expressao = input('Digite uma expressão matemática qualquer: ')
parenteses=[]
for l in expressao:
    if l==')' or l=='(':
        parenteses.append(l)

if parenteses.count('(')!=parenteses.count(')') or parenteses[-1]=='(' or parenteses[0]==')':
    print('Os \033[1mparênteses\033[m da expressão matemática estão colocados de forma \033[1;31mIncorreta!\033[m')
else:
    print('Os \033[1mparênteses\033[m da expressão matemática estão colocados de forma \033[1;32mcorreta!\033[m')