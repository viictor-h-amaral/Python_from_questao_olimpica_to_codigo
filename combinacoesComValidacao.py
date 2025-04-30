import copy
import validacaso
import algoritmoCombinacoes as combinacoes
import tkinter as itk
import time
import math

contador_caso = [0]
casosValidos = []
caso = []

def CombinarComValidacao(quantidadeElementosATomar, listaElementos, parte_completa ,barra_progresso):
    LimparCache()
    return RetornarPrimeiroCasoValidoCombinacaoComControleRecursivo(1, quantidadeElementosATomar, listaElementos, parte_completa, barra_progresso)


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

def RetornarPrimeiroCasoValidoCombinacaoComControleRecursivo(numeroDoElementoAtual, quantidadeElementosATomar, listaElementos, parte_completa, barra_progresso):

    total_casos = combinacoes.CalculaQuantidadeCombinacoes(quantidadeElementosATomar, 27)
    for index in range(len(listaElementos)):
        InsertAppendEmCaso(listaElementos[index], numeroDoElementoAtual)
        if (quantidadeElementosATomar > numeroDoElementoAtual):
            proximoElemento = numeroDoElementoAtual+1
            sublista = listaElementos[(index+1):len(listaElementos)]
            retornoInterno = RetornarPrimeiroCasoValidoCombinacaoComControleRecursivo( proximoElemento, quantidadeElementosATomar , sublista, parte_completa, barra_progresso)
            if(len(retornoInterno) > 0):
                return retornoInterno
        else:
            contador_caso[0] += 1
            AtualizarTamanhoBarraProgresso(contador_caso[0], total_casos, parte_completa, barra_progresso)
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
    contador_caso = 0

def AtualizarTamanhoBarraProgresso(numeroDoCaso, totalCasos, parte_completa, barra_progresso):
    
    relacao_casos_calculados = numeroDoCaso / totalCasos
    percentual_casos_calculados = round( 100*relacao_casos_calculados, 2)
    
    parte_completa.config(text = str(percentual_casos_calculados)+'%')
    parte_completa.place_configure(relwidth=relacao_casos_calculados)
    
    barra_progresso.update()