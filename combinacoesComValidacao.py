import copy
import validacaso
import algoritmoCombinacoes as combinacoes
import tkinter as itk


casosValidos = []
caso = []

def CombinarComValidacao(quantidadeElementosATomar, listaElementos, parte_completa ,barra_progresso, janela_principal):
    LimparCache()
    #return CombinarComControleRecursivoEValidacao(1, quantidadeElementosATomar, listaElementos)
    return RetornarPrimeiroCasoValidoCombinacaoComControleRecursivo(1, quantidadeElementosATomar, listaElementos, parte_completa, barra_progresso, janela_principal)


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

def RetornarPrimeiroCasoValidoCombinacaoComControleRecursivo(numeroDoElementoAtual, quantidadeElementosATomar, listaElementos, parte_completa, barra_progresso, janela_principal):
    #from solucao_otimizada import AtualizarTamanhoBarraProgresso
    contador_caso = 0
    total_casos = combinacoes.CalculaQuantidadeCombinacoes(quantidadeElementosATomar, 27)
    for index in range(len(listaElementos)):
        InsertAppendEmCaso(listaElementos[index], numeroDoElementoAtual)
        if (quantidadeElementosATomar > numeroDoElementoAtual):
            proximoElemento = numeroDoElementoAtual+1
            retornoInterno = RetornarPrimeiroCasoValidoCombinacaoComControleRecursivo( proximoElemento, quantidadeElementosATomar , listaElementos[(index+1):len(listaElementos)], parte_completa, barra_progresso, janela_principal)
            if(len(retornoInterno) > 0):
                return retornoInterno
        else:
            contador_caso += 1
            AtualizarTamanhoBarraProgresso(contador_caso, total_casos, parte_completa, barra_progresso, janela_principal)
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

def AtualizarTamanhoBarraProgresso(numeroDoCaso, totalCasos, parte_completa, barra_progresso, janela_principal):
    
    percentual_casos_calculados = numeroDoCaso / totalCasos
    parte_completa.place_configure(relwidth=percentual_casos_calculados, relheight=1.0)
    janela_principal.update()