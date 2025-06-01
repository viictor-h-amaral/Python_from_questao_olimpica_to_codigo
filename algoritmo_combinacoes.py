import copy
import math

casos = []
caso = []


def combinar(quantidade_elementos_tomar, lista_elementos):
    limpar_cache()
    return copy.deepcopy(combinar_com_controle_recursivo(1, quantidade_elementos_tomar, lista_elementos))


def combinar_com_controle_recursivo(numero_elemento_atual, quantidade_elementos_tomar, lista_elementos):
    for index in range(len(lista_elementos)):
        insert_append_em_caso(lista_elementos[index], numero_elemento_atual) 
        if (quantidade_elementos_tomar > numero_elemento_atual):
            proximo_elemento = numero_elemento_atual+1
            combinar_com_controle_recursivo( proximo_elemento, quantidade_elementos_tomar , lista_elementos[(index+1):len(lista_elementos)]) 
        else:
            casos.append(copy.deepcopy(caso))
    return casos


def insert_append_em_caso(elemento_inserido, posicao_insercao):
    if( len(caso) < posicao_insercao ):
        caso.append(elemento_inserido)
    else:
        posicao = posicao_insercao - 1
        caso[posicao] = elemento_inserido


def calcula_quantidade_combinacoes(quantidade_tomar, numero_total_elementos):
    calculo = math.factorial(numero_total_elementos)/(math.factorial(quantidade_tomar)*math.factorial(numero_total_elementos - quantidade_tomar))
    return calculo 


def limpar_cache():
    casos.clear()
    caso.clear()


#quantATomar = 3
#lista = [1, 2, 3, 4, 5]
#listaCaso = Combinar(quantATomar, lista)
#print('quantidade de casos:', len(casos))
#quantidadeCalculada = math.factorial(len(lista)) / ( math.factorial(quantATomar)*math.factorial(len(lista) - quantATomar)) 
#print('quantidade calculada:', quantidadeCalculada)
#print('combinações: ', listaCaso)