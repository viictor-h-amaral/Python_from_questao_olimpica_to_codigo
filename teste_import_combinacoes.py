import sys
sys.path.append('C:/Users/Usuario/AppData/Local/Programs/Python/Python313')

import time
import combinacoes

numeroATomar = 1
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27]

inicio_do_incio = time.time()

while numeroATomar <= 10:
    inicio_loop = time.time()
    listaCasos = combinacoes.Combinar(numeroATomar, lista)
    #print(listaCasos)
    fim_loop = time.time()
    print('tempo no loop:', numeroATomar, (fim_loop - inicio_loop), 'segundos')
    numeroATomar = numeroATomar + 1

fim_do_fim = time.time()
print('tempo total:', (fim_do_fim - inicio_do_incio), 'segundos')
