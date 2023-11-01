# Simplesmente roda um arquivo de áudio com a biblioteca "playsound".
# Essa biblioteca é muito mais simples que a "pygame", proposta na resolução da aula,
# porém não faz mais nada além de reproduzir um áudio.
from playsound import playsound# A biblioteca "playsound" não está sendo encontrada. Porque o python tenha atualizado talvez? Preciso tentar baixar de novo o módulo.
from time import sleep

print('\033[1;31mPATOMOSTIO INTENSIFIES\033[m')
sleep(0.5)
playsound('C:\Trabaio\Curso-em-Video-Python3\Mundo-1\Aula-08\Ex021-audio.wav')
# É necessário apenas colocar o caminho do áudio como argumento na única função da biblioteca, chamada "Playsound".