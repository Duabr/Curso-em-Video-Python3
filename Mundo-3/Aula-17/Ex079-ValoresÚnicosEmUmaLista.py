# Lê diversos números e adiciona-los em uma lista, mas somente caso esse número não tenha sido adicionado antes.
# No final, mostra todos os números digitados (tirando os números repeditos, como dito anteriormente).
from time import sleep
lista=[]
teste='S'
while teste=='S':
    teste=''
    num=int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
        print('\033[1;32mNúmero adicionado na lista!\033[m')
    else:
        print('\033[1;31mO número digitado já está na lista, então ele não foi adicionado.\033[m')
    while 'N'!=teste!='S':
        print('Quer adicionar mais um número para a lista?')
        teste=input('Digite S para sim ou N para não: ').upper().strip()

print('Agora que você terminou de digitar todos os valores, aqui estão todos eles em ordem crescente:')
sleep(3)
lista.sort()
for c, n in enumerate(lista):
    print(f'{c+1}º Número: {n}')