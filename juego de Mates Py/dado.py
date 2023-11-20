import tkinter as tk
from tkinter import Label, Button, font
import random


class SimuladorDado:
    def __init__(self, master):
        self.master = master
        master.title("Dado")

        self.font_size = font.nametofont("TkDefaultFont").copy()
        self.font_size.configure(size=36)

        self.etiqueta = Label(master, text="Tira el Dado!", font=self.font_size)
        self.etiqueta.pack()

        self.boton_tirar_dado = Button(
            master, text="Tirar Dado", command=self.tirar_dado
        )
        self.boton_tirar_dado.pack()

    def tirar_dado(self):
        resultado = random.randint(1, 6)
        mensaje = f"Resultado: {resultado}"
        self.etiqueta.config(text=mensaje)

root = tk.Tk()
root.geometry("500x150")
simulador = SimuladorDado(root)
root.mainloop()
