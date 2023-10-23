# Lê o nome, ano de nascimento e a carteira de trabalho, cadastrando-os com a idade e, caso a CTPS (Carteira de Trabalho e Providência Social)
# for diferente de 0, lê também o ano de contratação e o salário de uma pessoa.
# No fim, calcula e mostra com quantos anos essa pessoa poderá se aposentar (apenas considerando que são necessários 35 anos de carteira assinada para isso ocorrer).
from time import sleep
from datetime import date# Faz tempo que não uso essa biblioteca, tinha até esquecido como usa
ano_atual=date.today().year
print('\033[1mCadastrando um trabalhador:\033[m')
sleep(2)
cadastro={'nome':input('Nome: '),
          'nascimento':int(input('Data de nascimento: ')),
          'ctps':int(input('Carteira de trabalho (0 caso não tenha): '))}
if cadastro['ctps']!=0:
    cadastro['contratação']=int(input('Ano de contratação: '))
    cadastro['salário']=float(input('Salário mensal: R$'))

print('-='*35)
print(f"o/a trabalhador(a) \033[1m{cadastro['nome']}\033[m tem cerca de \033[1m{ano_atual-cadastro['nascimento']}\033[m anos de idade;")
sleep(2)
if cadastro['ctps']==0:
    print('Por enquanto, ele(a) \033[1mnão possui carteira assinada\033[m.')
    sleep(2)
else:
    print(f"Com o número de CTPS \033[1m{cadastro['ctps']}\033[m, ele(a) recebe \033[1m{cadastro['salário']}R$\033[m por mês;")
    sleep(2)
    print(f"E, com \033[1m{ano_atual-cadastro['contratação']} anos\033[m de carteira assinada, ",end='')
    if ano_atual-cadastro['contratação']<35:
        print(f"poderá se aposentar aos \033[1m{cadastro['contratação']+35-cadastro['nascimento']} anos\033[m.")
    else:
        print(f"\033[1mJá pode se aposentar!\033[m")
    sleep(2)
print('-='*35)