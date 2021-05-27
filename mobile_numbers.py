import tkinter as tk
from tkinter import  ttk
from tkinter import messagebox
import phonenumbers
from phonenumbers import carrier, geocoder
from tkinter import *

class app():

    def __init__(self):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {@Malgun Gothic} -size 14"
        font12 = "-family {@Malgun Gothic} -size 13 -weight bold"
        font13 = "-family {@Malgun Gothic} -size 11 -weight bold"

        self.root = tk.Tk()
        self.root.geometry("525x236")
        self.root.resizable(0, 0)
        self.root.title("Formato: + (código país) (número de teléfono)")
        self.root.iconbitmap('contacto_1.ico')
        self.root.configure(background="#ffc58a")

        self.L1 = tk.Label(self.root)
        self.L1.place(relx=0.076, rely=0.070, height=42, width=421)
        self.L1.configure(background="#ffc58a")
        self.L1.configure(disabledforeground="#a3a3a3")
        self.L1.configure(font=font10)
        self.L1.configure(foreground="#000000")
        self.L1.configure(text='''IDENTIFICADOR DE PAIS Y OPERADOR''')

        self.L2 = tk.Label(self.root)
        self.L2.place(relx=0.220, rely=0.200, height=51, width=264)
        self.L2.configure(background="#ffc58a")
        self.L2.configure(disabledforeground="#a3a3a3")
        self.L2.configure(font=font12)
        self.L2.configure(foreground="#000000")
        self.L2.configure(text='''Ingresa un numero de telefono:''')

        self.L3 = tk.Label(self.root)
        self.L3.place(relx=0, rely=0.480, height=95, width=525)
        self.L3.configure(background="#ffc58a")
        self.L3.configure(disabledforeground="#a3a3a3")
        self.L3.configure(font=font12)
        self.L3.configure(foreground="#000000")

        self.borrar = StringVar()
        self.Entry1 = tk.Entry(self.root,textvariable=self.borrar)
        self.Entry1.place(relx=0.300, rely=0.400,height=30, relwidth=0.35)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.B1 = tk.Button(self.root, command=lambda : self.validar(self.Entry1.get()))
        self.B1.place(relx=0.370, rely=0.580, height=44, width=107)
        self.B1.configure(activebackground="#ececec")
        self.B1.configure(activeforeground="#000000")
        self.B1.configure(background="#9d9dce")
        self.B1.configure(disabledforeground="#a3a3a3")
        self.B1.configure(font=font13)
        self.B1.configure(foreground="#000000")
        self.B1.configure(highlightbackground="#d9d9d9")
        self.B1.configure(highlightcolor="black")
        self.B1.configure(pady="0")
        self.B1.configure(text='''VALIDAR''')
    
        self.root.mainloop()

    def crear_boton1(self):
        font13 = "-family {@Malgun Gothic} -size 11 -weight bold"
        
        self.B2 = tk.Button(self.root, command=self.crear_widgets)
        self.B2.place(relx=0.300, rely=0.300, height=44, width=180)
        self.B2.configure(activebackground="#ececec")
        self.B2.configure(activeforeground="#000000")
        self.B2.configure(background="#9d9dce")
        self.B2.configure(disabledforeground="#a3a3a3")
        self.B2.configure(font=font13)
        self.B2.configure(foreground="#000000")
        self.B2.configure(highlightbackground="#d9d9d9")
        self.B2.configure(highlightcolor="black")
        self.B2.configure(pady="0")
        self.B2.configure(text='''Validar otro numero''')

    def eliminar_widgets(self):
        self.B1.destroy()
        self.Entry1.destroy()
        self.L2.destroy()

    def crear_widgets(self):
        font12 = "-family {@Malgun Gothic} -size 13 -weight bold"
        font13 = "-family {@Malgun Gothic} -size 11 -weight bold"

        self.L3.config(text='')

        self.L2 = tk.Label(self.root)
        self.L2.place(relx=0.220, rely=0.200, height=51, width=264)
        self.L2.configure(background="#ffc58a")
        self.L2.configure(disabledforeground="#a3a3a3")
        self.L2.configure(font=font12)
        self.L2.configure(foreground="#000000")
        self.L2.configure(text='''Ingresa un numero de telefono:''')

        self.borrar = StringVar()
        self.Entry1 = tk.Entry(self.root,textvariable=self.borrar)
        self.Entry1.place(relx=0.300, rely=0.400,height=30, relwidth=0.35)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        
        self.B1 = tk.Button(self.root, command=lambda : self.validar(self.Entry1.get()))
        self.B1.place(relx=0.370, rely=0.580, height=44, width=107)
        self.B1.configure(activebackground="#ececec")
        self.B1.configure(activeforeground="#000000")
        self.B1.configure(background="#9d9dce")
        self.B1.configure(disabledforeground="#a3a3a3")
        self.B1.configure(font=font13)
        self.B1.configure(foreground="#000000")
        self.B1.configure(highlightbackground="#d9d9d9")
        self.B1.configure(highlightcolor="black")
        self.B1.configure(pady="0")
        self.B1.configure(text='''VALIDAR''')

    def num_valido(self, numero):
        self.numero_valido = phonenumbers.is_valid_number(numero)
        return self.numero_valido

    def validar(self, numerotelefono):

        if numerotelefono == '':
            messagebox.showwarning('Aviso', 'Debes ingresar un numero telefonico')

        else:
            if numerotelefono.startswith('+'): 
                self.info = []

                try:
                    self.numero =  phonenumbers.parse(numerotelefono)
                    self.validar_numero = self.num_valido(self.numero)

                    if not self.validar_numero:
                        messagebox.showerror('Error', 'El número que ingresaste no es valido, el formato deber +(CountryCode)(número telefónico)')
                    
                    else:
                        self.info.append(geocoder.description_for_number(self.numero, 'es'))
                        self.info.append(carrier.name_for_number(self.numero,'es'))
                        self.pais = 'País: ' + self.info[0]
                        self.operador = 'Operador: ' + self.info[1]
                        self.eliminar_widgets()
                        self.L3.config(text=numerotelefono + '\n' + self.pais + '\n' + self.operador)
                        self.crear_boton1()
                
                except:
                    messagebox.showwarning('Aviso','Verifica el número ingresado')

            else:
                numerotelefono = '+' + numerotelefono
                self.info = []

                try:
                    self.numero =  phonenumbers.parse(numerotelefono)
                    self.validar_numero = self.num_valido(self.numero)

                    if not self.validar_numero:
                        messagebox.showerror('Error', 'El número que ingresaste no es valido, el formato deber +(CountryCode)(número telefónico)')
                    
                    else:
                        self.info.append(geocoder.description_for_number(self.numero, 'es'))
                        self.info.append(carrier.name_for_number(self.numero,'es'))
                        self.pais = 'País: ' + self.info[0]
                        self.operador = 'Operador: ' + self.info[1]
                        self.eliminar_widgets()
                        self.L3.config(text=numerotelefono + '\n' + self.pais + '\n' + self.operador)
                        self.crear_boton1()
                
                except:
                    messagebox.showwarning('Aviso','Verifica el número ingresado')

if __name__ == "__main__":
    app()




