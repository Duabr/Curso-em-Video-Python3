# Lê uma URL e testa se ela está acessível no momento do código com a biblioteca "requests"
import requests

url = input('Digite uma URL de um site para verificar se ele está acessível no momento: ')

try:
    response = requests.get(url)
    print('\033[1;34mSite está funcionando corretamente.\033[m')
except:
    print('''\033[1;30mO site não está acessível no momento. Verifique se você digitou a URL corretamente
e sua conexão com a internet. Se ainda não funcionar, talvez o site não exista.\033[m''')