import tkinter as tk
from tkinter.scrolledtext import ScrolledText

root = tk.Tk()
root.geometry("400x300")

# Crea un cuadro de texto con scroll vertical integrado de fábrica
mi_texto = ScrolledText(root, wrap=tk.WORD, width=40, height=10)
mi_texto.pack(padx=10, pady=10)

# Para insertar texto:
mi_texto.insert(tk.END, "Este es un texto largo que demuestra cómo el ScrolledText maneja el scroll automáticamente sin código adicional...")

root.mainloop()