import tkinter as itk
import tkinter.font as tkFont
from PIL import Image
import math


#configuracao da janela principal
janela_principal = itk.Tk()
janela_principal.title("Status da Execução")
janela_principal.geometry("1500x500")

fonte_padrao = tkFont.Font(family="Arial", size=14)
cinza_padrao = "#5E5E5E"
verde_padrao = "#00AE28"



#configuracao primeiro frame janela principal
frame_logs = itk.Frame(janela_principal, bg= cinza_padrao)
frame_logs.pack(side="top", fill="both", expand=True, pady=5, padx=10)

botao1 = itk.Button(frame_logs, text="tempo de execução para 1 aluno: 0seg", width=10, foreground = verde_padrao, font = fonte_padrao, bg = cinza_padrao, anchor="w", padx=10 )
botao1.pack(side="top", fill="x", anchor="w", pady=2, padx=5)

botao2 = itk.Button(frame_logs, text="tempo de execução para 2 alunos: 0seg", width=10, foreground = verde_padrao, font = fonte_padrao, bg = cinza_padrao, anchor="w", padx=10)
botao2.pack(side="top", fill="x", anchor="w", pady=2, padx=5)



#configuracao segundo frame janela principal
frame_progresso = itk.Frame(janela_principal, bg= cinza_padrao)
frame_progresso.pack(side="bottom", fill="both", expand=True, pady=5, padx=10)

barra_progresso = itk.Frame(frame_progresso, height=60)
barra_progresso.pack(side="bottom", padx=10, pady=15, fill="x")

    #BARRA DE PROGRESSO
percentual_casos_calculados = 0.6
parte_completa = itk.Label(barra_progresso, bg = "green", text=str(percentual_casos_calculados*100)+'%', font=fonte_padrao)
parte_completa.place(relwidth=percentual_casos_calculados, relheight=1.0)

#loop para manter aberta a janela principal
janela_principal.mainloop()