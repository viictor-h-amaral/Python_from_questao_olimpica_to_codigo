import copy
import valida_caso
import algoritmo_combinacoes as combinacoes
import tkinter as itk
import time
from gerador_logs import *

contador_caso = 0
casos_validos = []
caso = []

def combinar_com_validacao(quantidade_elementos_a_tomar, lista_elementos, parte_completa , barra_progresso, label_log_tempo, tempo_inicio):
    limpar_cache()
    return retornar_primeiro_caso_valido_combinacao_com_controle_recursivo(1, quantidade_elementos_a_tomar, lista_elementos, parte_completa, barra_progresso,label_log_tempo, tempo_inicio)


def combinar_com_controle_recursivo_e_validacao(numero_do_elemento_atual, quantidade_elementos_a_tomar, lista_elementos):
    for index in range(len(lista_elementos)):
        insert_append_em_caso(lista_elementos[index], numero_do_elemento_atual)
        
        if (quantidade_elementos_a_tomar > numero_do_elemento_atual):
            proximo_elemento = numero_do_elemento_atual+1
            sublista = lista_elementos[(index+1):len(lista_elementos)]
            combinar_com_controle_recursivo_e_validacao( proximo_elemento, quantidade_elementos_a_tomar , sublista)
            
        elif(valida_caso.caso_eh_valido(caso)):
            casos_validos.append(copy.deepcopy(caso))

    return casos_validos

def retornar_primeiro_caso_valido_combinacao_com_controle_recursivo(numero_do_elemento_atual, quantidade_elementos_a_tomar, lista_elementos, parte_completa, barra_progresso, label_log_tempo,  tempo_inicio):

    for index in range(len(lista_elementos)):

        insert_append_em_caso(lista_elementos[index], numero_do_elemento_atual)
        
        if (quantidade_elementos_a_tomar > numero_do_elemento_atual):
            
            proximo_elemento = numero_do_elemento_atual+1
            sublista = lista_elementos[(index+1):len(lista_elementos)]
            retorno_interno = retornar_primeiro_caso_valido_combinacao_com_controle_recursivo(proximo_elemento, quantidade_elementos_a_tomar, sublista, parte_completa, barra_progresso, label_log_tempo, tempo_inicio)
            if(len(retorno_interno) > 0):
                return retorno_interno
        else:
            global contador_caso
            contador_caso += 1
            total_casos = combinacoes.calcula_quantidade_combinacoes(quantidade_elementos_a_tomar, 27)
            tempo_estimativa = gerar_estimativa_tempo_restante(contador_caso, total_casos, tempo_inicio)
            atualizar_tamanho_barra_progresso(contador_caso , total_casos , parte_completa , barra_progresso , label_log_tempo , tempo_inicio, tempo_estimativa)
            copia_caso = copy.deepcopy(caso)
            if(valida_caso.caso_eh_valido(copia_caso)):
                return copia_caso, contador_caso

    return []

def insert_append_em_caso(elemento_inserido, posicao_insercao):
    if( len(caso) < posicao_insercao ):
        caso.append(elemento_inserido)
    else:
        posicao = posicao_insercao - 1
        caso[posicao] = elemento_inserido
    return

def limpar_cache():
    casos_validos.clear()
    caso.clear()
    contador_caso = 0

def atualizar_tamanho_barra_progresso(numero_do_caso, total_casos, parte_completa, barra_progresso, label_log_tempo, tempo_inicio, tempo_restante):
    
    relacao_casos_calculados = numero_do_caso / total_casos
    percentual_casos_calculados = round( 100*relacao_casos_calculados, 2)
    
    tempo_executado = tempo_log(round((time.perf_counter() - tempo_inicio), 0))
    label_log_tempo.config(text=f'Executando há {tempo_executado}. Estimativa de {tempo_restante} restantes ...')


    parte_completa.config(text = f'{percentual_casos_calculados}%')
    parte_completa.place_configure(relwidth=relacao_casos_calculados)
    
    barra_progresso.update()


def gerar_estimativa_tempo_restante(casos_calculados_para_numeroAlunos, total_casos_numeroAlunos, tempo_inicio):
    duracao_execucao = time.perf_counter() - tempo_inicio #t1

    total_casos_faltantes_para_numeroAlunos = total_casos_numeroAlunos - casos_calculados_para_numeroAlunos #d2

    taxa_inversa_execucao = duracao_execucao / casos_calculados_para_numeroAlunos #t1/d1 = v^(-1)

    tempo_faltante = taxa_inversa_execucao*total_casos_faltantes_para_numeroAlunos
    tempo_faltante = tempo_log_sem_segundos(round(tempo_faltante, 0))
    return tempo_faltante #segundos
