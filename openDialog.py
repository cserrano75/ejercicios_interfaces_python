from tkinter import *
from tkinter import filedialog

root=Tk()

def abreFichero():
    fichero=filedialog.askopenfilename(title="Abrir",    
        filetypes=(
            ("Archivos de texto", "*.txt"),
            ("Archivos de Python", ("*.py", "*.pyx")),
            ("Todos los archivos", "*.*")
        )
    ,initialdir="C:/Users/CSERRANO/Desktop/Desarrollo")
    
    print(fichero)

Button (root,text="Abrir fichero",command=abreFichero).pack()

root.mainloop()
