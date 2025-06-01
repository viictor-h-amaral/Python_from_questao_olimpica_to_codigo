import sys
sys.path.append('C:/Users/Usuario/AppData/Local/Programs/Python/Python313')

import time
import copy
import math
import tkinter as itk
import tkinter.font as tkFont
import threading
from gerador_logs import *


#region JANELA PRINCIPAL

janela_principal = itk.Tk()
janela_principal.minsize(800, 0)
janela_principal.title("Status da Execução")
janela_principal.iconbitmap("recursos/iconeAlgoritmo.ico")

#endregion JANELA PRINCIPAL

#region CORES/FONTES

fonte_padrao = tkFont.Font(family="Helvetica", size=14)
fonte_barra_progresso = tkFont.Font(family="Helvetica", size=10)
fonte_label_logs = tkFont.Font(family="Helvetica", weight="bold", size=14)

cinza_padrao = "#1a1a1a"
verde_padrao = "#4dff00"
verde_barra_progresso = "#3bc202"

#endregion CORES/FONTES

#region FRAME_LOGS

frame_logs = itk.Frame(janela_principal, bg= cinza_padrao)
frame_logs.pack(side="top", fill="both", expand=True, pady=5, padx=10)

def gera_botoes(numero_alunos, logs, logs_completos):

    for widget in frame_logs.winfo_children():
        widget.destroy()
        #frame_logs.update()

    label_logs = itk.Label(frame_logs, text='Logs dos casos executados. Clique para maior detalhamento ...')
    label_logs.configure(width=10, bg = cinza_padrao, fg = verde_padrao, font=fonte_label_logs, anchor="w", padx=10)
    label_logs.pack(side="top", fill="x", anchor="center", pady=2, padx=0)

    for aluno in range(numero_alunos):
        
        botao_log = itk.Button(frame_logs, text=logs[aluno], bg = cinza_padrao, fg = verde_padrao)
        botao_log.configure(width=10,  font=fonte_padrao, anchor="w", padx=10, command=lambda p1=(aluno), p2=(logs_completos[aluno]):abrir_janela_log_completo(p1, p2))
        botao_log.pack(side="top", fill="x", anchor="w", pady=2, padx=5)
        janela_principal.update()

def abrir_janela_log_completo(numero_alunos, logs):
    janela_logs_completos = itk.Toplevel()
    janela_logs_completos.title("Recurso de logs")
    janela_logs_completos.iconbitmap("recursos/iconeAlgoritmo.ico")

    label_main = itk.Label(janela_logs_completos, text="Log para "+str(numero_alunos+1)+" alunos")
    label_main.configure(font=fonte_label_logs, fg=verde_padrao, bg=cinza_padrao, anchor="center")
    label_main.pack(side="top", fill="x", anchor="w", pady=2, padx=5)

    for log in logs:
        label_log = itk.Label(janela_logs_completos, text=log.replace("[", "(").replace("]", ")"))
        label_log.configure(font=fonte_padrao, fg=verde_padrao, bg=cinza_padrao, anchor="w")
        label_log.pack(side="top", fill="x", anchor="w", pady=2, padx=5)
        janela_logs_completos.update()

#endregion FRAME_QUE_CONTEM_OS_LOGS

#region FRAME_PROGRESSO

frame_progresso = itk.Frame(janela_principal, bg= cinza_padrao)
frame_progresso.pack(side="bottom", fill="both", expand=True, pady=5, padx=10)

barra_progresso = itk.Frame(frame_progresso, height=60)
barra_progresso.pack(side="bottom", padx=10, pady=15, fill="x")

info_barra_progresso = itk.Frame(frame_progresso, height=60, bg= cinza_padrao)
info_barra_progresso.pack(side="top", padx=10, pady=15, fill="x")

label_info_barra_progresso = itk.Label(info_barra_progresso, bg=cinza_padrao, fg=verde_padrao , font=fonte_label_logs)
label_info_barra_progresso.configure(text='Executando algoritmo para 1 aluno', anchor="w")
label_info_barra_progresso.grid(column=0, row=0, sticky="w")

label_log_tempo = itk.Label(info_barra_progresso, bg=cinza_padrao, fg=verde_padrao , font=fonte_padrao)
label_log_tempo.configure(text='', anchor="w")
label_log_tempo.grid(column=0, row=1, sticky="w")

parte_completa = itk.Label(barra_progresso, bg=verde_barra_progresso, fg=cinza_padrao, font=fonte_barra_progresso)
parte_completa.place(relwidth=0, relheight=1.0)

def atualizar_tamanho_barra_progresso_e_label(numero_alunos, numeroDoCaso, totalCasos):
    
    percentual_casos_calculados = numeroDoCaso / totalCasos

    novo_texto = f'Executando algoritmo para {str(numero_alunos)} alunos'
    label_info_barra_progresso.config(text = novo_texto)

    parte_completa.config(text='100%')
    parte_completa.place_configure(relwidth=percentual_casos_calculados)
    janela_principal.update()
    
#endregion FRAME_PROGRESSO

#region METODOS_ALGORITMO

def gera_provas():
    provas = []
    
    Questoes = [1, 2, 3]
    Notas = [0, 1, 2]

    for nota_questao1 in Notas:
        for nota_questao2 in Notas:
            for nota_questao3 in Notas:
                provas.append([nota_questao1, nota_questao2, nota_questao3])
    return provas


def gera_combinacoes_validas(numero_alunos, lista_provas, parte_completa, barra_progresso , label_log_tempo,  tempo_inicio):
    from combinacoes_com_validacao import combinar_com_validacao
    return combinar_com_validacao(numero_alunos, lista_provas, parte_completa, barra_progresso, label_log_tempo, tempo_inicio )
            

def gera_combinacoes(numero_alunos, lista_provas):
    from combinacoes_com_validacao import combinar_com_validacao
    return combinar_com_validacao(numero_alunos, lista_provas)

#endregion METODOS_ALGORITMO

def main():

    inicio = time.perf_counter()
    provas = gera_provas()
    numero_alunos = 0
    log = []
    logs_completos = []

    while (True):
        numero_alunos = numero_alunos + 1
        tempo_inicio = time.perf_counter()

        caso_valido, casos_calculados = gera_combinacoes_validas( numero_alunos, provas, parte_completa, barra_progresso, label_log_tempo, tempo_inicio) 
    
        log_desse_aluno = gera_log(tempo_inicio, numero_alunos)
        log.append(log_desse_aluno)
        log_completo_desse_aluno = gera_log_completo( log_desse_aluno , caso_valido , casos_calculados )
        logs_completos.append(log_completo_desse_aluno)

        time.sleep(0.3)
        
        gera_botoes(numero_alunos, log, logs_completos)
        atualizar_tamanho_barra_progresso_e_label(numero_alunos+1, 1, 1)
        
        time.sleep(0.5)
        
        if(len(caso_valido) == 0): 
            #print('E a resposta é ...', numero_alunos - 1)
            break
            
        print(caso_valido)
    fim = time.perf_counter()
    #print('tempo total de execução:', TempoLog(fim - inicio))

def main_thread():
    thread = threading.Thread(target=main)
    thread.start()


main_thread()
janela_principal.mainloop()