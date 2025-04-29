import sys
sys.path.append('C:/Users/Usuario/AppData/Local/Programs/Python/Python313')
import combinacoesComValidacao
import time
import math
from tkinter import *


def GeraProvas():
    provas = []
    
    Questoes = [1, 2, 3]
    Notas = [0, 1, 2]

    for notaQuestao1 in Notas:
        for notaQuestao2 in Notas:
            for notaQuestao3 in Notas:
                provas.append([notaQuestao1, notaQuestao2, notaQuestao3])
    return provas


def GeraCombinacoesValidas(numeroAlunos, listaProvas):
    return combinacoesComValidacao.CombinarComValidacao(numeroAlunos, listaProvas)
            

def GeraCombinacoes(numeroAlunos, listaProvas):
    return combinacoesComValidacao.CombinarComValidacao(numeroAlunos, listaProvas)


def GeraLog(tempo_inicio, numeroAlunos, casosValidos):
    tempo_de_execucao = time.time() - tempo_inicio
    print('tempo de execução para', numeroAlunos, 'alunos foi de', TempoLog(tempo_de_execucao))
    print('Caso válido encontrado:', casosValidos)


def TempoLog(tempo_total_em_segundos):

    tempo_em_horas = tempo_total_em_segundos // 3600
    tempo_em_minutos = tempo_total_em_segundos // 60
    tempo_em_segundos = tempo_total_em_segundos - tempo_em_horas*3600 - tempo_em_minutos*60

    if( (tempo_em_horas == 0 and tempo_em_minutos == 0) and not(tempo_em_segundos <= 0.001) ):
        tempo_em_segundos = round( tempo_em_segundos, 3 )
    else:
        tempo_em_segundos = int( math.floor(tempo_em_segundos) )

    tempo_escrito = ''

    if (tempo_em_horas > 0):
        tempo_escrito = tempo_escrito + str(tempo_em_horas) + 'h '
    if (tempo_em_minutos > 0):
        tempo_escrito = tempo_escrito + str(tempo_em_minutos) + 'min '
    tempo_escrito = tempo_escrito + str(tempo_em_segundos) + 'seg'

    return tempo_escrito


def main():
    inicio = time.time()
    provas = GeraProvas()
    numeroAlunos = 0
    while (True):
        numeroAlunos = numeroAlunos + 1
        tempo_inicio = time.time()
        casosValidos = GeraCombinacoesValidas(numeroAlunos, provas)
        GeraLog(tempo_inicio, numeroAlunos, casosValidos)
        if(len(casosValidos) == 0): 
            print('E a resposta é ...', numeroAlunos - 1)
            break
    fim = time.time()
    print('tempo total de execução:', TempoLog(fim - inicio))


main()