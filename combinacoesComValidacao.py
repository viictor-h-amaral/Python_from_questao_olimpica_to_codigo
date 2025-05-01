import copy
import validacaso
import algoritmoCombinacoes as combinacoes
import tkinter as itk
import time
import math

contador_caso = [0] # gambis braba: [0]->total de casos para esse numero de alunos e [1]->total de casos de tudo até agora
casosValidos = []
caso = []

def CombinarComValidacao(quantidadeElementosATomar, listaElementos, parte_completa ,barra_progresso, tempo_inicio):
    LimparCache()
    return RetornarPrimeiroCasoValidoCombinacaoComControleRecursivo(1, quantidadeElementosATomar, listaElementos, parte_completa, barra_progresso, tempo_inicio)


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

def RetornarPrimeiroCasoValidoCombinacaoComControleRecursivo(numeroDoElementoAtual, quantidadeElementosATomar, listaElementos, parte_completa, barra_progresso,  tempo_inicio):

    total_casos = combinacoes.CalculaQuantidadeCombinacoes(quantidadeElementosATomar, 27) #executa muitas vezes, deve executar somente uma!
    for index in range(len(listaElementos)):

        InsertAppendEmCaso(listaElementos[index], numeroDoElementoAtual)
        if (quantidadeElementosATomar > numeroDoElementoAtual):
            proximoElemento = numeroDoElementoAtual+1
            sublista = listaElementos[(index+1):len(listaElementos)]
            retornoInterno = RetornarPrimeiroCasoValidoCombinacaoComControleRecursivo(proximoElemento, quantidadeElementosATomar,sublista, parte_completa, barra_progresso, tempo_inicio)
            if(len(retornoInterno) > 0):
                return retornoInterno
        else:
            contador_caso[0] += 1
            #contador_caso[1] += 1
            tempo_estimativa_segundos = GerarEstimativaTempoRestante(quantidadeElementosATomar, contador_caso[0], total_casos, tempo_inicio)
            AtualizarTamanhoBarraProgresso(contador_caso[0], total_casos, parte_completa, barra_progresso)
            copiaCaso = copy.deepcopy(caso)
            if(validacaso.CasoEhValido(copiaCaso)):
                return copiaCaso, contador_caso[0]

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
    contador_caso[0] = 0

def AtualizarTamanhoBarraProgresso(numeroDoCaso, totalCasos, parte_completa, barra_progresso):
    
    relacao_casos_calculados = numeroDoCaso / totalCasos
    percentual_casos_calculados = round( 100*relacao_casos_calculados, 2)
    
    parte_completa.config(text = f'{percentual_casos_calculados}%')
    parte_completa.place_configure(relwidth=relacao_casos_calculados)
    
    barra_progresso.update()


def GerarEstimativaTempoRestante(numeroAlunos, casos_ja_calculados_para_numeroAlunos, total_casos_numeroAlunos, tempo_inicio):
    duracao_execucao = time.time() - tempo_inicio #t1

    calculoTotalCombinacoes = CalcularTotalCombinacoes(numeroAlunos-1)

    todos_casos_calculados =  calculoTotalCombinacoes + casos_ja_calculados_para_numeroAlunos #d1
    total_casos_faltantes_para_numeroAlunos = total_casos_numeroAlunos - casos_ja_calculados_para_numeroAlunos #d2

    taxa_inversa_execucao = duracao_execucao / todos_casos_calculados #v^(-1)

    tempo_faltante = taxa_inversa_execucao*total_casos_faltantes_para_numeroAlunos
    return tempo_faltante #segundos


def CalcularTotalCombinacoes(quantidade_maxima_a_tomar):
    total_combinacoes_soma = 0
    for a_tomar in range(1, quantidade_maxima_a_tomar+1):
        total_combinacoes_soma += combinacoes.CalculaQuantidadeCombinacoes(a_tomar, 27)
    return total_combinacoes_soma