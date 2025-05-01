import copy
import math

casos = []
caso = []


def Combinar(quantidadeElementosATomar, listaElementos):
    LimparCache()
    return copy.deepcopy(CombinarComControleRecursivo(1, quantidadeElementosATomar, listaElementos))


def CombinarComControleRecursivo(numeroDoElementoAtual, quantidadeElementosATomar, listaElementos):
    for index in range(len(listaElementos)):
        InsertAppendEmCaso(listaElementos[index], numeroDoElementoAtual) 
        if (quantidadeElementosATomar > numeroDoElementoAtual):
            proximoElemento = numeroDoElementoAtual+1
            CombinarComControleRecursivo( proximoElemento, quantidadeElementosATomar , listaElementos[(index+1):len(listaElementos)]) 
        else:
            casos.append(copy.deepcopy(caso))
    return casos


def InsertAppendEmCaso(elementoASerInserido, posicaoASerInserido):
    if( len(caso) < posicaoASerInserido ):
        caso.append(elementoASerInserido)
    else:
        posicao = posicaoASerInserido - 1
        caso[posicao] = elementoASerInserido
    return


def CalculaQuantidadeCombinacoes(quantidadeATomar, numeroTotalElementos):
    calculo = math.factorial(numeroTotalElementos)/(math.factorial(quantidadeATomar)*math.factorial(numeroTotalElementos-quantidadeATomar))
    return calculo 


def LimparCache():
    casos.clear()
    caso.clear()


#quantATomar = 3
#lista = [1, 2, 3, 4, 5]
#listaCaso = Combinar(quantATomar, lista)
#print('quantidade de casos:', len(casos))
#quantidadeCalculada = math.factorial(len(lista)) / ( math.factorial(quantATomar)*math.factorial(len(lista) - quantATomar)) 
#print('quantidade calculada:', quantidadeCalculada)
#print('combinações: ', listaCaso)