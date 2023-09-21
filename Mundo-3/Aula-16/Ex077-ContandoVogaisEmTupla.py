# Com um banco de dados contendo algumas palaras, mostra as vogais usadas em cada uma delas (incluindo as usadas no lugar das letras ramistas).
palavras_latim=('iuuenis', 'domum', 'puer', 'femina', 'crustulum',
                'unde', 'salvete', 'dormire', 'iupiter', 'uxor')
vogais=('a','e','i','o','u')
print(f'{"PALAVRAS EM LATIM":-^70}')
for p in palavras_latim:
    vogais_atuais=''
    for letra in p:
        if letra in vogais:
            vogais_atuais+=letra
    num_vogais_atuais=len(vogais_atuais)
    print(f'Na palavra \033[1m"{p}"\033[m, há \033[1m{num_vogais_atuais}\033[m vogais, sendo elas: ',end='')
    for c in range(num_vogais_atuais):
        if num_vogais_atuais-2!=c!=num_vogais_atuais-1:
            print(f'\033[1m{vogais_atuais[c]}\033[m, ',end='')
        elif c==num_vogais_atuais-2:
            print(f'\033[1m{vogais_atuais[c]}\033[m e ',end='')
        elif c==num_vogais_atuais-1:
            print(f'\033[1m{vogais_atuais[c]}\033[m.')
print('-'*70)