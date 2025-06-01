import time
import math

def gera_log_completo(log_simples, caso_valido, casos_calculados):
    log_completo = []
    log_completo.append(log_simples)
    log_completo.append('Quantidade de casos calculados: ' + str(casos_calculados)) #adicionar total de casos

    if(len(caso_valido) > 0):
        caso_valido = 'Primeiro caso válido encontrado: '+ str(caso_valido)
    else:
        caso_valido = 'Não há casos válidos...'

    log_completo.append(caso_valido)

    return log_completo

def gera_log(tempo_inicio, numero_alunos):
    tempo_de_execucao = time.perf_counter() - tempo_inicio
    log = 'Tempo de execução para ' + str(numero_alunos) + ' alunos foi de ' + str(tempo_log(tempo_de_execucao))
    print(log)
    return log


def tempo_log(tempo_total_em_segundos):

    tempo_em_horas = int(tempo_total_em_segundos // 3600)
    tempo_em_minutos = int( (tempo_total_em_segundos - tempo_em_horas*3600) // 60)
    tempo_em_segundos = tempo_total_em_segundos - tempo_em_horas*3600 - tempo_em_minutos*60

    tempo_em_segundos_nao_eh_int = tempo_em_segundos != math.floor(tempo_em_segundos)
    if( (tempo_em_horas == 0 and tempo_em_minutos == 0) and (tempo_em_segundos > 0.001) and tempo_em_segundos_nao_eh_int):
        tempo_em_segundos = round( tempo_em_segundos, 3 )
    else:
        tempo_em_segundos = int( math.floor(tempo_em_segundos) )

    tempo_escrito = ''

    if (tempo_em_horas > 0):
        tempo_escrito = tempo_escrito + str(tempo_em_horas) + 'h '

    if (tempo_em_minutos > 0):
        tempo_escrito = tempo_escrito + str(tempo_em_minutos) + 'min '

    if(tempo_em_segundos < 10 and tempo_em_segundos != 0):
        tempo_escrito = tempo_escrito + '0'+str(tempo_em_segundos) + 'seg'
    else:
        tempo_escrito = tempo_escrito + str(tempo_em_segundos) + 'seg'
    
    tempo_escrito = tempo_escrito.replace(".", ",")

    return tempo_escrito

def tempo_log_sem_segundos(tempo_total_em_segundos):
    tempo_em_horas = int(tempo_total_em_segundos // 3600)
    tempo_em_minutos = int( (tempo_total_em_segundos - tempo_em_horas*3600) // 60)
    tempo_em_segundos = tempo_total_em_segundos - tempo_em_horas*3600 - tempo_em_minutos*60

    tempo_em_segundos_nao_eh_int = tempo_em_segundos != math.floor(tempo_em_segundos)
    if( (tempo_em_horas == 0 and tempo_em_minutos == 0) and (tempo_em_segundos > 0.001) and tempo_em_segundos_nao_eh_int):
        tempo_em_segundos = round( tempo_em_segundos, 3 )
    else:
        tempo_em_segundos = int( math.floor(tempo_em_segundos) )

    tempo_escrito = ''

    if (tempo_em_horas > 0):
        tempo_escrito = tempo_escrito + str(tempo_em_horas) + 'h '

    if (tempo_em_minutos > 0):
        tempo_escrito = tempo_escrito + str(tempo_em_minutos) + 'min '
    elif(tempo_em_horas == 0):
        if(tempo_em_segundos < 10 and tempo_em_segundos != 0):
            tempo_escrito = tempo_escrito + '0'+str(tempo_em_segundos) + 'seg'
        else:
            tempo_escrito = tempo_escrito + str(tempo_em_segundos) + 'seg'
    
    tempo_escrito = tempo_escrito.replace(".", ",")

    return tempo_escrito