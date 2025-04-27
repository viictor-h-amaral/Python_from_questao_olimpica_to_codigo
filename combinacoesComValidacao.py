import copy
import validacaso

casosValidos = []
caso = []

def CombinarComValidacao(quantidadeElementosATomar, listaElementos):
    LimparCache()
    #return CombinarComControleRecursivoEValidacao(1, quantidadeElementosATomar, listaElementos)
    return RetornarPrimeiroCasoValidoCombinacaoComControleRecursivo(1, quantidadeElementosATomar, listaElementos)


def CombinarComControleRecursivoEValidacao(numeroDoElementoAtual, quantidadeElementosATomar, listaElementos):
    for index in range(len(listaElementos)):
        InsertAppendEmCaso(listaElementos[index], numeroDoElementoAtual)
        if (quantidadeElementosATomar > numeroDoElementoAtual):
            proximoElemento = numeroDoElementoAtual+1
            CombinarComControleRecursivoEValidacao( proximoElemento, quantidadeElementosATomar , listaElementos[(index+1):len(listaElementos)])
        else:
            copiaCaso = copy.deepcopy(caso)
            if(validacaso.CasoEhValido(copiaCaso)):
                casosValidos.append(copiaCaso)

    return casosValidos

def RetornarPrimeiroCasoValidoCombinacaoComControleRecursivo(numeroDoElementoAtual, quantidadeElementosATomar, listaElementos):
    for index in range(len(listaElementos)):
        InsertAppendEmCaso(listaElementos[index], numeroDoElementoAtual)
        if (quantidadeElementosATomar > numeroDoElementoAtual):
            proximoElemento = numeroDoElementoAtual+1
            retornoInterno = RetornarPrimeiroCasoValidoCombinacaoComControleRecursivo( proximoElemento, quantidadeElementosATomar , listaElementos[(index+1):len(listaElementos)])
            if(len(retornoInterno) > 0):
                return retornoInterno
        else:
            copiaCaso = copy.deepcopy(caso)
            if(validacaso.CasoEhValido(copiaCaso)):
                return copiaCaso
    return []

def InsertAppendEmCaso(elementoASerInserido, posicaoASerInserido):
    if( len(caso) < posicaoASerInserido ):
        caso.append(elementoASerInserido)
    else:
        posicao = posicaoASerInserido - 1
        caso[posicao] = elementoASerInserido
    return

def LimparCache():
    casosValidos.clear()
    caso.clear()