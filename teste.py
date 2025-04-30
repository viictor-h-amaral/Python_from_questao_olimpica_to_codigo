import tkinter as tk
from tkinter import ttk

# Função para configurar o canvas e o frame
def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

# Criação da janela principal
root = tk.Tk()
root.title("Exemplo de Scroll Lateral")

# Criação do canvas
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Adicionando a barra de rolagem horizontal
scrollbar_x = ttk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
canvas.configure(xscrollcommand=scrollbar_x.set)

# Criação do frame dentro do canvas
frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

# Configuração do canvas para ajustar o frame
#frame.bind("<Configure>", lambda event, canvas=canvas: on_frame_configure(canvas))

# Adicionando widgets ao frame
for i in range(50):
    ttk.Label(frame, text=f"Label {i}").grid(row=0, column=i, padx=5, pady=5)

# Iniciando o loop principal
root.mainloop()
