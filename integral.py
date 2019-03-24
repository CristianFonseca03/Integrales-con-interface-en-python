from sympy import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

x = Symbol('x')

raiz = Tk()
raiz.title("INTEGRALES")
raiz.resizable(0, 0)
miFrame = Frame(raiz)
miFrame.pack()

textIntegral = StringVar()
limSup = StringVar()
limInf = StringVar()
Resultado = StringVar()

cuadroIntegral = Entry(miFrame, textvariable=textIntegral)
cuadroIntegral.grid(row=0, column=1, padx=10, pady=10)

cuadroLimSuperior = Entry(miFrame, textvariable=limSup)
cuadroLimSuperior.grid(row=1, column=1, padx=10, pady=10)

cuadroLimInferior = Entry(miFrame, textvariable=limInf)
cuadroLimInferior.grid(row=2, column=1, padx=10, pady=10)

nombreCuadroIntegral = Label(miFrame, text="Ingrese la integral")
nombreCuadroIntegral.grid(row=0, column=0, padx=10, pady=10)

nombreCuadroLimsup = Label(miFrame, text="Ingrese el limite superior")
nombreCuadroLimsup.grid(row=1, column=0, padx=10, pady=10)

nombreCuadroLiminf = Label(miFrame, text="Ingrese el limite inferior")
nombreCuadroLiminf.grid(row=2, column=0, padx=10, pady=10)

resultado = Label(miFrame, text="RESULTADO: ")
resultado.grid(row=3, column=0, padx=10, pady=10)

rs = Entry(miFrame, textvariable=Resultado)
rs.grid(row=3, column=1, padx=10, pady=10)


def clicked():
    a = integrate(textIntegral.get(), (x, limInf.get(), limSup.get()))
    Resultado.set(a)
    print(a)


btn = Button(miFrame, text='Integrar', command=clicked)
btn.grid(column=0, row=4, columnspan=2, padx=10, pady=10)

raiz.mainloop()
