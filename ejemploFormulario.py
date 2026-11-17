# Genero un formario principal con un frame lateral, otro central y uno superior
# emulando los formularios con el menu en un side bar

from tkinter import *
from tkinter import messagebox

root = Tk()

# Variables de opciones
varOpcion=IntVar()
lunOption=IntVar()
marOption=IntVar()

texto = """Esta es la primera línea

esta es la segunda línea

esta es la tercera linea"""

def infoAdicional():
    messagebox.showinfo("Titulo form",texto,icon="warning",)

def mostrarOpcion():

    if varOpcion.get()==1:
        etiqueta.config(text="Masculino")
    else:
        etiqueta.config(text="Femenino")

def opcionDia():

    diaEscogido=""

    if (lunOption.get()==1):
        diaEscogido+=" Lunes"
    if (marOption.get()==1):
        diaEscogido+=" Martes"

    textoDiaSemana.config(text=diaEscogido)

def cerrarAplicacion():
    valor=messagebox.askquestion("Cerrar","Desea cerrar la aplicacion?")

    if valor=="yes":
        root.destroy()

root.geometry("600x400")
root.minsize(400, 300)

# ---------------- Barra Menu -------------------------------------
barraMenu=Menu(root)
root.config(menu=barraMenu)

# Menu principal de la opcion Archivo
archivoMenu=Menu(barraMenu,tearoff=0)
archivoMenu.add_command(label="Nuevo",state="disabled")
archivoMenu.add_command(label="Abrir")

# Sub Menu de la opcion Archivo/Abrir
submenuAbrirUno=Menu(archivoMenu,tearoff=0)
archivoMenu.add_cascade(label="Abrir mas",menu=submenuAbrirUno)

#Agrego los comandos al submenu
submenuAbrirUno.add_command(label="Sub opcion uno")
submenuAbrirUno.add_command(label="Sub opcion dos")

archivoMenu.add_separator()
archivoMenu.add_command(label="Cerrar",command=cerrarAplicacion)


edicionMenu=Menu(barraMenu,tearoff=0)
edicionMenu.add_command(label="Cortar")
edicionMenu.add_command(label="Copiar")
edicionMenu.add_command(label="Pegar")

herramientasMenu=Menu(barraMenu)

ayudaMenu=Menu(barraMenu,tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...",command=infoAdicional)

barraMenu.add_cascade(label="Archivo",menu=archivoMenu)
barraMenu.add_cascade(label="Edicion",menu=edicionMenu)
barraMenu.add_cascade(label="Herramientas",menu=herramientasMenu)
barraMenu.add_cascade(label="Ayuda",menu=ayudaMenu)

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

# Creamos options buttons
# opcionLunes=Checkbutton(frameContenido,text="Lunes",variable=lunOption,onvalue=1,offvalue=0,command="opcionDia")
# opcionLunes.pack(padx=5,pady=5)

# opcionMartes=Checkbutton(frameContenido,text="Martes",onvalue=1,offvalue=0,command="opcionDia")
# opcionMartes.pack(padx=5,pady=5,side="left")

Checkbutton(frameContenido,text="Lunes", variable=lunOption, onvalue=1, offvalue=0, command=opcionDia).pack(padx=5,pady=5,side="left")
Checkbutton(frameContenido,text="Martes", variable=marOption, onvalue=1, offvalue=0, command=opcionDia).pack(padx=5,pady=5,side="left")

textoDiaSemana=Label(frameContenido)
textoDiaSemana.pack(side="bottom")

root.mainloop()
