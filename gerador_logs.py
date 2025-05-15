import time
import math

def GeraLogCompleto(log_simples, casoValido, casosCalculados):
    log_completo = []
    log_completo.append(log_simples)
    log_completo.append('Quantidade de casos calculados: ' + str(casosCalculados)) #adicionar total de casos

    if(len(casoValido) > 0):
        casoValido = 'Primeiro caso válido encontrado: '+ str(casoValido)
    else:
        casoValido = 'Não há casos válidos...'

    log_completo.append(casoValido)

    return log_completo

def GeraLog(tempo_inicio, numeroAlunos):
    tempo_de_execucao = time.time() - tempo_inicio
    log = 'Tempo de execução para ' + str(numeroAlunos) + ' alunos foi de ' + str(TempoLog(tempo_de_execucao))
    print(log)
    return log


def TempoLog(tempo_total_em_segundos):

    tempo_em_horas = int(tempo_total_em_segundos // 3600)
    tempo_em_minutos = int( (tempo_total_em_segundos - tempo_em_horas*3600) // 60)
    tempo_em_segundos = tempo_total_em_segundos - tempo_em_horas*3600 - tempo_em_minutos*60

    tmp_em_seg_eh_inteiro = tempo_em_segundos == math.floor(tempo_em_segundos)
    if( (tempo_em_horas == 0 and tempo_em_minutos == 0) and (tempo_em_segundos > 0.001) and (not tmp_em_seg_eh_inteiro) ):
        tempo_em_segundos = round( tempo_em_segundos, 3 )
    else:
        tempo_em_segundos = int( math.floor(tempo_em_segundos) )

    tempo_escrito = ''

    if (tempo_em_horas > 0):
        tempo_escrito = tempo_escrito + str(tempo_em_horas) + 'h '
    if (tempo_em_minutos > 0):
        tempo_escrito = tempo_escrito + str(tempo_em_minutos) + 'min '
    if(tempo_em_segundos < 10):
        tempo_escrito = tempo_escrito + '0'+str(tempo_em_segundos) + 'seg'
    tempo_escrito = tempo_escrito.replace(".", ",")

    return tempo_escrito
