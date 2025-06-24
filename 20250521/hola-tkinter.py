import tkinter as tk

def saludar():
    print('Holaaaa!')

import datetime

tiempo_actual = datetime.datetime.now()
print(tiempo_actual)

# clase (molde, formato) == instanciar/crear ==> objeto

# clases tienen: atributos y funciones/metodos

ventana = tk.Tk()
ventana.title("Mi primera venta con Tkinter")
ventana.geometry("800x600")

texto =tk.Label(ventana, text='Hola desde Tkinter', font=('Arial', 20))
texto.pack()

boton = tk.Button(ventana, text='Saludar', font=('Arial', 20), command=saludar)
boton.pack()

ventana.mainloop()
