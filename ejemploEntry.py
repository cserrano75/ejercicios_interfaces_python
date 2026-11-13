from tkinter import *
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

nombreLabel=Label(miFrame,text="Nombre")
nombreLabel.grid(row=0,column=0,sticky="w", padx="5",pady="1")

apellidoLabel=Label(miFrame,text="Apellido")
apellidoLabel.grid(row=1,column=0,sticky="w", padx="5",pady="1")

passwordLabel=Label(miFrame,text="Password")
passwordLabel.grid(row=2,column=0,sticky="w", padx="5",pady="1")

direccionLabel=Label(miFrame,text="Direccion")
direccionLabel.grid(row=3,column=0,sticky="w", padx="5",pady="1")

def alternar_visibilidad():
    # Verificamos qué valor tiene actualmente 'show'
    if cuadroPassword.cget('show') == '*':
        cuadroPassword.config(show='')  # Muestra el texto real
        btn_mostrar.config(text='Ocultar')
    else:
        cuadroPassword.config(show='*')  # Oculta con asteriscos
        btn_mostrar.config(text='Mostrar')

btn_mostrar =raiz.Button(raiz, text="Mostrar", command=alternar_visibilidad)
btn_mostrar.pack()

raiz.mainloop()


