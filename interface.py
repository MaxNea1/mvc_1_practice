import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

from connexion import *

class Form_Users:
    global base
    base = None
    global groupBox
    groupBox = None
    global txtbox_id
    txtbox_id = None
    global txtbox_name
    txtbox_name = None
    global txtbox_lastname
    txtbox_lastname = None
    global txtbox_gender
    txtbox_gender = None
    global txtbox_age
    txtbox_age = None
    global combo
    combo = None
    global tree
    tree = None

def Form():

    global txtbox_id
    global txtbox_name
    global txtbox_lastname
    global txtbox_gender
    global txtbox_age
    global combo
    global tree
    global base
    global groupBox


    base = Tk()
    base.geometry('1450x300')
    base.title('CRUD Python + SQLserver')

    groupBox = LabelFrame(base, text="Datos del usuario", padx=5, pady=5)
    groupBox.grid(row=0, column=0, padx=10, pady=10)

    LabelId = Label(groupBox, text="Id:", width=13, font=('arial', 12)).grid(row=0, column=0)
    textBoxId = Entry(groupBox)
    textBoxId.grid(row=0, column=1)
    
    LabelName = Label(groupBox, text="Nombres:", width=13, font=('arial', 12)).grid(row=1, column=0)
    textBoxName = Entry(groupBox)
    textBoxName.grid(row=1, column=1)

    LabelLastName = Label(groupBox, text="Apellidos:", width=13, font=('arial', 12)).grid(row=2, column=0)
    textBoxLastName  = Entry(groupBox)
    textBoxLastName.grid(row=2, column=1)

    LabelGender = Label(groupBox, text="Género:", width=13, font=('arial', 12)).grid(row=3, column=0)
    selectGender = tk.StringVar()
    combo = ttk.Combobox(groupBox, values=["Masculino", "Femenino"], textvariable=selectGender)
    combo.grid(row=3, column=1)
    selectGender.set("Masculino")

    LabelAge = Label(groupBox, text="Edad:", width=13, font=('arial', 12)).grid(row=4, column=0)
    textBoxAge  = Entry(groupBox)
    textBoxAge.grid(row=4, column=1)

    Button(groupBox, text="Guardar", width=10).grid(row=5, column=0)
    Button(groupBox, text="Modificar", width=10).grid(row=5, column=1)
    Button(groupBox, text="Eliminar", width=10).grid(row=5, column=2)

    groupBox = LabelFrame(base,  text="Lista de usuarios", padx=5, pady=5)
    groupBox.grid(row=0, column=1, padx=5, pady=5)

    tree = ttk.Treeview(groupBox, columns=('Id', 'Nombre', 'Apellidos', 'Genero', 'Edad'), show='headings', height=5,)
    tree.column('#1', anchor=CENTER)
    tree.heading('#1', text='Id')
    tree.column('#2', anchor=CENTER)
    tree.heading('#2', text='Nombre')
    tree.column('#3', anchor=CENTER)
    tree.heading('#3', text='Apellidos')
    tree.column('#4', anchor=CENTER)
    tree.heading('#4', text='Género')
    tree.column('#5', anchor=CENTER)
    tree.heading('#5', text='Edad')

    vsb = Scrollbar(groupBox, orient='vertical', command=tree.yview)
    tree.configure(yscrollcommand=vsb.set)
    tree.pack(side=LEFT, fill=BOTH, expand=True)
    vsb.pack(side=RIGHT, fill=Y)
    

    base.mainloop()#para que se dibuje
Form()

