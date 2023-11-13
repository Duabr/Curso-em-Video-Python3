# Com uma função (obviamente) chamada "voto", lê o ano de idacimento de uma pessoa e
# indica se o voto dela é opcional, obrigatório ou proibido.
# Com menos de 16 anos, o voto é proibido. Entre 16 e 17 anos, é opcional. Dos 18 aos 17 anos é obrogatório e com mais de 70 é opcional novamente.
from datetime import date

def voto(ida):# "ida" significa idade.
    if ida<16:
        return 'PROIBIDO'
    elif 16<=ida<18 or ida>70:
        return 'OPCIONAL'
    elif 18<=ida<=70:
        return 'OBRIGATÓRIO'


nas = int(input('Em que ano você nasceu? R: '))
teste=''
while 'N'!=teste!='S':
    teste=input('Você já fez aniversário esse ano? Digite S ou N: ').strip().upper()
    if teste=='N':
        nas+=1
ano_atual=date.today().year
ida = ano_atual-nas

print(f'Com \033[1m{ida}\033[m anos de idade, votar é \033[1m{voto(ida)}\033[m.')
