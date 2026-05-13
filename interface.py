import tkinter as tk
from tkinter import messagebox
from tkinter import *
from tkinter import ttk

from connexion import *
from clients import *

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
    try:

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
        txtbox_id = Entry(groupBox)
        txtbox_id.grid(row=0, column=1)
        
        LabelName = Label(groupBox, text="Nombres:", width=13, font=('arial', 12)).grid(row=1, column=0)
        txtbox_name = Entry(groupBox)
        txtbox_name.grid(row=1, column=1)

        LabelLastName = Label(groupBox, text="Apellidos:", width=13, font=('arial', 12)).grid(row=2, column=0)
        txtbox_lastname  = Entry(groupBox)
        txtbox_lastname.grid(row=2, column=1)

        LabelGender = Label(groupBox, text="Género:", width=13, font=('arial', 12)).grid(row=3, column=0)
        selectGender = tk.StringVar()
        combo = ttk.Combobox(groupBox, values=["Masculino", "Femenino"], textvariable=selectGender)
        combo.grid(row=3, column=1)
        selectGender.set("Masculino")

        LabelAge = Label(groupBox, text="Edad:", width=13, font=('arial', 12)).grid(row=4, column=0)
        txtbox_age  = Entry(groupBox)
        txtbox_age.grid(row=4, column=1)

        Button(groupBox, text="Guardar", width=10, command=guardarRegistros).grid(row=5, column=0)
        Button(groupBox, text="Modificar", width=10, command=updateRegistros).grid(row=5, column=1)
        Button(groupBox, text="Eliminar", width=10, command=deleteRegistros).grid(row=5, column=2)

        groupBox = LabelFrame(base,  text="Lista de usuarios", padx=5, pady=5)
        groupBox.grid(row=0, column=1, padx=5, pady=5)

        tree = ttk.Treeview(groupBox, columns=('Id', 'Nombre', 'Apellidos', 'Genero', 'Edad'), show='headings', height=5,)
        tree.column('# 1', anchor=CENTER)
        tree.heading('# 1', text='Id')
        tree.column('# 2', anchor=CENTER)
        tree.heading('# 2', text='Nombre')
        tree.column('# 3', anchor=CENTER)
        tree.heading('# 3', text='Apellidos')
        tree.column('# 4', anchor=CENTER)
        tree.heading('# 4', text='Género')
        tree.column('# 5', anchor=CENTER)
        tree.heading('# 5', text='Edad')

        vsb = Scrollbar(groupBox, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        tree.pack(side=LEFT, fill=BOTH, expand=True)
        vsb.pack(side=RIGHT, fill=Y)

        #Mostrar datos en la tabla

        for row in Clients.mostrarClientes():
            tree.insert("", "end", values=tuple(row))

        tree.bind("<<TreeviewSelect>>", selection)

        base.mainloop()#para que se dibuje
    except ValueError as error:
        print('Error al mostrar interfaz: ', error)

def guardarRegistros():
        global txtbox_name
        global txtbox_lastname
        global txtbox_age
        global combo

        try:
            if txtbox_name is None or txtbox_lastname is None or txtbox_age is None or combo is None: 
                print('Los Widgets no han sido inicializados')
                return


            name = txtbox_name.get()
            last_name = txtbox_lastname.get()
            age = txtbox_age.get()
            combo = combo.get()
        
            Clients.ingresarClientes(name, last_name, combo,age)
            messagebox.showinfo("Información", "Registro guardado correctamente")

            actualizarTabla()

            txtbox_name.delete(0, END)
            txtbox_lastname.delete(0, END)  
            txtbox_age.delete(0, END)
        
        except Exception as e:
            print("Error", f"No se pudo guardar: {e}")
            messagebox.showerror("Error", "No se pudo guardar el registro")

def actualizarTabla():
    global tree

    try:
        tree.delete(*tree.get_children())

        datos = Clients.mostrarClientes()

        for row in datos:
            tree.insert("", "end", values=tuple(row))
    except Exception as e:
        print('Error al actualizar tabla: ', e)
        messagebox.showerror("Error", "No se pudo actualizar la tabla")

def selection(event):
    try:
        item = tree.focus()
        if item:
            values = tree.item(item)['values']

            txtbox_id.delete(0, END)
            txtbox_id.insert(0, values[0])
            txtbox_name.delete(0, END)
            txtbox_name.insert(0, values[1])
            txtbox_lastname.delete(0, END)
            txtbox_lastname.insert(0, values[2])    

            combo.set(values[3])
            txtbox_age.delete(0, END)
            txtbox_age.insert(0, values[4])

    except Exception as e:
        print('Error al seleccionar registro: ', e)
        messagebox.showerror("Error", "No se pudo seleccionar el registro")

def updateRegistros():
        global txtbox_id
        global txtbox_name
        global txtbox_lastname
        global txtbox_age
        global combo

        try:
            if txtbox_id is None or txtbox_name is None or txtbox_lastname is None or txtbox_age is None or combo is None: 
                print('Los Widgets no han sido inicializados')
                return


            name = txtbox_name.get()
            last_name = txtbox_lastname.get()
            age = txtbox_age.get()
            combo = combo.get()
            id = txtbox_id.get()
        
            Clients.update(id, name, last_name, combo,age)
            messagebox.showinfo("Información", "Registro guardado correctamente")

            actualizarTabla()

            txtbox_id.delete(0, END)
            txtbox_name.delete(0, END)
            txtbox_lastname.delete(0, END)  
            txtbox_age.delete(0, END)

            combo.set("Masculino")
        
        except Exception as e:
            print("Error", f"No se pudo guardar: {e}")
            messagebox.showerror("Error", "No se pudo guardar el registro")

def deleteRegistros():
        global txtbox_id
        global txtbox_name
        global txtbox_lastname
        global txtbox_age
        global combo

        try:
            if txtbox_id is None: 
                print('Los Widgets no han sido inicializados')
                return

            id = txtbox_id.get()
        
            Clients.delete(id)
            messagebox.showinfo("Información", "Registro eliminado correctamente")

            actualizarTabla()

            txtbox_id.delete(0, END)
            txtbox_name.delete(0, END)
            txtbox_lastname.delete(0, END)  
            txtbox_age.delete(0, END)
            combo.set("Masculino")
        
        except Exception as e:
            print("Error", f"No se pudo guardar: {e}")
            messagebox.showerror("Error", "No se pudo guardar el registro")

Form()

