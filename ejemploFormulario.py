# Genero un formario principal con un frame lateral, otro central y uno superior
# emulando los formularios con el menu en un side bar

from tkinter import *

root = Tk()

varOpcion=IntVar()

def mostrarOpcion():

    if varOpcion.get()==1:
        etiqueta.config(text="Masculino")
    else:
        etiqueta.config(text="Femenino")

root.geometry("600x400")
root.minsize(400, 300)

# 1. Frame lateral (izquierda, ancho fijo, alto dinámico)
frameLateral = Frame(root, width=120, bd=2, relief="solid")
frameLateral.pack_propagate(False)
frameLateral.pack(side=LEFT, fill=Y, padx=5, pady=5)

optMasculino=Radiobutton(frameLateral,text="Masculino",variable=varOpcion,value=1,command=mostrarOpcion)
optMasculino.pack(fill=X,padx=5,pady=5)

optFemenino=Radiobutton(frameLateral,text="Femenino",variable=varOpcion,value=2,command=mostrarOpcion)
optFemenino.pack(fill=X,padx=5,pady=5)

btnLateral = Button(frameLateral, text="Opción 1")
btnLateral.pack(fill=X, padx=5, pady=5) # Lo empaquetamos DENTRO del frame lateral

etiqueta=Label(frameLateral)
etiqueta.pack(fill=X, padx=5, pady=5)

# 2. Frame superior (arriba del contenido principal, ej: la pantalla de la calculadora)
# Usamos fill=X para que se estire a lo ancho, pero SIN expand=True para que no crezca hacia abajo.
frameSuperior = Frame(root, height=80, bd=2, relief="solid")
frameSuperior.pack_propagate(False) # Opcional si quieres mantener una altura fija para la pantalla
frameSuperior.pack(side=TOP, fill=X, padx=5, pady=5)

# --- 3. FRAME DE CONTENIDO ---
frameContenido = Frame(root, bd=2, relief="solid")
frameContenido.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)

# Creamos un campo de texto (Entry) cuyo padre es 'frameContenido'
txtContenido = Entry(frameContenido)
txtContenido.pack(padx=10, pady=10)

root.mainloop()
