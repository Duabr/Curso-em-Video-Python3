# Lê o nome e a média de um aluno, calcula, de acordo com a média, se o aluno está aproado ou reprovado
# e guarda todas essas informações em um dicionário.
from time import sleep
aluno={}
aluno['nome']=f"\033[1m{input('Nome do aluno: ')}\033[m"
aluno['media']=float(input('Média do aluno: '))
if aluno['media']>=7:
    aluno['situaçao']='\033[1;32maprovado(a)\033[m'
elif 5<=aluno['media']<7:
    aluno['situaçao']='\033[1;33mem recuperação\033[m'
elif aluno['media']<5:
    aluno['situaçao']='\033[1;31mreprovado(a)\033[m'

print('\033[1mAnalizando...\033[m')
sleep(2)
print(f'O/A aluno(a) {aluno["nome"]} está com média \033[1m{aluno["media"]:.1f}\033[m, portanto está {aluno["situaçao"]}.')