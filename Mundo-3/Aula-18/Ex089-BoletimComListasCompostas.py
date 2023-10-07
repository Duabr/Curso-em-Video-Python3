# Guarda nomes e notas de diversos alunos e, no final, mostra a média de cada aluno, podendo também
# mostrar cada uma das duas notas individualmente.
print('Cadastre o nome e duas notas de diversos alunos;')
alunos=[]
teste='S'
c=0
while teste=='S':
    teste=''
    c+=1
    nome=input(f'\033[mNome do {c}º/ª aluno(a): \033[1m')
    notas=[float(input('\033[mPrimeira nota: \033[1m')), float(input('\033[mSegunda nota: \033[1m'))]
    media=f'{(notas[0]+notas[1])/2:.1f}'
    alunos.append([nome, notas, media])
    while 'N'!=teste!='S':
        teste=input('\033[mDeseja cadastrar mais um aluno? [S/N]: \033[1m').strip().upper()

print('-'*30)
print(f"{'  NOME':<13}{'MÉDIA'}")
for c, al in enumerate(alunos):
    print(f"{f'{c+1} {al[0]}: ':<13}{al[2]}")
print('-'*30, '\033[m')

while True:
    teste=-2
    while teste!=-1 and (1>teste or teste>len(alunos)):
        teste=int(input('Deseja ver as notas separadas de qual aluno? Digite o número do aluno, ou -1 para terminar: '))
        if teste!=-1 and (1>teste or teste>len(alunos)):
            print('\033[1;31mNúmero inválido. Digite o número do aluno que deseja ver suas notas ou digite -1 para parar a execução\033[m')
    if teste==-1:
        break
    print(f'''Aluno \033[1m{alunos[teste-1][0]}\033[m:
Nota 1: \033[1m{alunos[teste-1][1][0]}\033[m
Nota 2: \033[1m{alunos[teste-1][1][1]}\033[m''')

print('\033[1mFIM DO PROGRAMA\033[M')