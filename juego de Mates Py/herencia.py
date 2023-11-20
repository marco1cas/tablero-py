import tkinter as tk
from tkinter import messagebox

class form1(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Form1 (padre)")

        btn_base = tk.Button(self, text="Botón form1", command=self.btn_base_click)

        btn_base.pack(pady=20)

    def btn_base_click(self):
        messagebox.showinfo("form1", "Haz clic en el botón en form1")


class hijo_form1(form1):
    def __init__(self):
        super().__init__()

        self.title("Formulario Hijo")

        btn_hijo = tk.Button(self, text="Botón en hijo_form1", command=self.btn_hijo)

        btn_hijo.pack(pady=20)

    def btn_hijo(self):
        messagebox.showinfo("hijo_form1", "Haz clic en el botón en hijo de form1")


if __name__ == "__main__":
    form_base = form1()

    form_base.mainloop()

    form_hijo = hijo_form1()

    form_hijo.mainloop()
