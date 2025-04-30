import sys
sys.path.append('C:/Users/Usuario/AppData/Local/Programs/Python/Python313')

import time
import math
import tkinter as itk
import tkinter.font as tkFont


#region JANELA PRINCIPAL

janela_principal = itk.Tk()
janela_principal.title("Status da Execução")
janela_principal.geometry("1000x500")

#endregion JANELA PRINCIPAL

#region CORES/FONTES

fonte_padrao = tkFont.Font(family="Arial", size=14)
fonte_barra_progresso = tkFont.Font(family="Arial", size=10)
cinza_padrao = "#1a1a1a"
verde_padrao = "#4dff00"
verde_barra_progresso = "#3bc202"

#endregion CORES/FONTES

#region FRAME_LOGS

frame_logs = itk.Frame(janela_principal, bg= cinza_padrao)
frame_logs.pack(side="top", fill="both", expand=True, pady=5, padx=10)

def Gera_Botoes(numeroAlunos, logs):

    for widget in frame_logs.winfo_children():
        widget.destroy()
        #frame_logs.update()

    for aluno in range(numeroAlunos):
        
        botao_log = itk.Button(frame_logs, text=logs[aluno])
        botao_log.configure(width=10, bg = cinza_padrao, fg = verde_padrao, font=fonte_padrao, anchor="w", padx=10)
        botao_log.pack(side="top", fill="x", anchor="w", pady=2, padx=5)
        janela_principal.update()

#endregion FRAME_QUE_CONTEM_OS_LOGS

#region FRAME_PROGRESSO

frame_progresso = itk.Frame(janela_principal, bg= cinza_padrao)
frame_progresso.pack(side="bottom", fill="both", expand=True, pady=5, padx=10)

barra_progresso = itk.Frame(frame_progresso, height=60)
barra_progresso.pack(side="bottom", padx=10, pady=15, fill="x")

parte_completa = itk.Label(barra_progresso, bg=verde_barra_progresso, fg=cinza_padrao ,text=str(0*100)+'%', font=fonte_barra_progresso)
parte_completa.place(relwidth=0, relheight=1.0)

def AtualizarTamanhoBarraProgresso(numeroDoCaso, totalCasos):
    
    percentual_casos_calculados = numeroDoCaso / totalCasos
    parte_completa.config(text = '100%')
    parte_completa.place_configure(relwidth=percentual_casos_calculados)
    janela_principal.update()
    
#endregion FRAME_PROGRESSO

#region METODOS_ALGORITMO

def GeraProvas():
    provas = []
    
    Questoes = [1, 2, 3]
    Notas = [0, 1, 2]

    for notaQuestao1 in Notas:
        for notaQuestao2 in Notas:
            for notaQuestao3 in Notas:
                provas.append([notaQuestao1, notaQuestao2, notaQuestao3])
    return provas


def GeraCombinacoesValidas(numeroAlunos, listaProvas, parte_completa, barra_progresso):
    from combinacoesComValidacao import CombinarComValidacao
    return CombinarComValidacao(numeroAlunos, listaProvas, parte_completa, barra_progresso)
            

def GeraCombinacoes(numeroAlunos, listaProvas):
    from combinacoesComValidacao import CombinarComValidacao
    return CombinarComValidacao(numeroAlunos, listaProvas)

#endregion METODOS_ALGORITMO

#region LOGS

def GeraLog(tempo_inicio, numeroAlunos, casosValidos):
    tempo_de_execucao = time.time() - tempo_inicio
    log = 'Tempo de execução para ' + str(numeroAlunos) + ' alunos foi de ' + str(TempoLog(tempo_de_execucao))
    print(log)
    return log


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
    tempo_escrito = tempo_escrito.replace(".", ",")

    return tempo_escrito

#endregion LOGS

def main():

    inicio = time.time()
    provas = GeraProvas()
    numeroAlunos = 0
    log = []

    while (True):
        #janela_principal.update()
        numeroAlunos = numeroAlunos + 1
        tempo_inicio = time.time()
        casosValidos = GeraCombinacoesValidas(numeroAlunos, provas, parte_completa, barra_progresso)
        
        time.sleep(0.3)
        
        log.append(GeraLog(tempo_inicio, numeroAlunos, casosValidos))
        Gera_Botoes(numeroAlunos, log)
        AtualizarTamanhoBarraProgresso(1,1)
        
        time.sleep(0.5)
        
        if(len(casosValidos) == 0): 
            print('E a resposta é ...', numeroAlunos - 1)
            break
    fim = time.time()
    print('tempo total de execução:', TempoLog(fim - inicio))


main()
janela_principal.mainloop()