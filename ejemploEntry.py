from tkinter import *
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
raiz=Tk()

miFrame=Frame(raiz,width=1200,height=600)
miFrame.pack()

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0,column=1)
cuadroNombre.config(fg="lightgreen",justify="left")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1,column=1)

cuadroPassword=Entry(miFrame)
cuadroPassword.grid(row=2,column=1)
cuadroPassword.config(show="*")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3,column=1)

textoComentarios=Text(miFrame,width=16,height=5)
textoComentarios.grid(row=4,column=1)
scrollVert=Scrollbar(miFrame,command=textoComentarios.yview)
scrollVert.grid(row=4,column=2,sticky="nwse")

textoComentarios.config(yscrollcommand=scrollVert.set)

nombreLabel=Label(miFrame,text="Nombre")
nombreLabel.grid(row=0,column=0,sticky="w", padx="5",pady="1")

apellidoLabel=Label(miFrame,text="Apellido")
apellidoLabel.grid(row=1,column=0,sticky="w", padx="5",pady="1")

passwordLabel=Label(miFrame,text="Password")
passwordLabel.grid(row=2,column=0,sticky="w", padx="5",pady="1")

direccionLabel=Label(miFrame,text="Direccion")
direccionLabel.grid(row=3,column=0,sticky="w", padx="5",pady="1")

comentariosLabel=Label(miFrame,text="Comentarios")
comentariosLabel.grid(row=4,column=0,sticky="w", padx="5",pady="1")


def mostrarMensaje():

    messagebox.showinfo(message="Este es un mensaje", title="Atención")

botonEnvio=Button(raiz,text="Enviar",command=mostrarMensaje)
# botonEnvio.grid(row=5,column=1)
# botonEnvio.config(justify="center")
botonEnvio.pack()


raiz.mainloop()


