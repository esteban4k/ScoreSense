import tkinter as tk
from tkinter import messagebox

def calcular_promedio():
    # Obtener los valores ingresados por el usuario
    notas = []
    porcentajes = []

    for i in range(len(entry_notas)):
        nota = float(entry_notas[i].get())
        porcentaje = float(entry_porcentajes[i].get())

        notas.append(nota)
        porcentajes.append(porcentaje)

    # Verificar que se hayan ingresado notas
    if len(notas) == 0:
        messagebox.showwarning("Advertencia", "No se ingresaron notas.")
        return

    # Calcular el promedio teniendo en cuenta los porcentajes
    total_porcentaje = sum(porcentajes)
    promedio = sum(notas[i] * (porcentajes[i] / total_porcentaje) for i in range(len(notas)))

    # Calcular la nota necesaria para aprobar
    nota_necesaria_aprobacion = (3.0 - (promedio * total_porcentaje)) / (1 - total_porcentaje)

    # Calcular la nota necesaria para no perder
    nota_necesaria_no_perder = (2.0 - (promedio * total_porcentaje)) / (1 - total_porcentaje)

    # Mostrar el resultado en una ventana de mensaje
    if promedio >= 3.0:
        mensaje = f"El promedio es: {promedio:.2f}\n¡Aprobado!"
    else:
        mensaje = f"El promedio es: {promedio:.2f}\n¡Reprobado!\n\n"
        mensaje += f"Para aprobar necesitas una nota mínima de: {nota_necesaria_aprobacion:.2f}\n"
        mensaje += f"Para no perder necesitas una nota mínima de: {nota_necesaria_no_perder:.2f}"
    messagebox.showinfo("Resultado", mensaje)

def agregar_notas():
    # Obtener la cantidad de notas ingresadas por el usuario
    cantidad_notas = int(entry_cantidad.get())

    # Limpiar las notas existentes y los campos de entrada
    for entry in entry_notas:
        entry.destroy()
    for entry in entry_porcentajes:
        entry.destroy()
    entry_notas.clear()
    entry_porcentajes.clear()

    # Crear los campos de entrada para las nuevas notas y porcentajes
    for i in range(cantidad_notas):
        label_nota = tk.Label(ventana, text=f"Nota {i+1}:")
        label_nota.grid(row=i+3, column=0, padx=10, pady=5)
        entry_nota = tk.Entry(ventana)
        entry_nota.grid(row=i+3, column=1, padx=10, pady=5)
        entry_notas.append(entry_nota)

        label_porcentaje = tk.Label(ventana, text=f"Porcentaje {i+1}:")
        label_porcentaje.grid(row=i+3, column=2, padx=10, pady=5)
        entry_porcentaje = tk.Entry(ventana)
        entry_porcentaje.grid(row=i+3, column=3, padx=10, pady=5)
        entry_porcentajes.append(entry_porcentaje)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Promedio")

# Crear los elementos de la interfaz
label_cantidad = tk.Label(ventana, text="Cantidad de notas:")
label_cantidad.grid(row=0, column=0, padx=10, pady=5)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.grid(row=0, column=1, padx=10, pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_notas)
boton_agregar.grid(row=0, column=2, padx=10, pady=5)

entry_notas = []
entry_porcentajes = []
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular_promedio)
boton_calcular.grid(row=1, column=0, columnspan=4, padx=10, pady=5)

# Iniciar el bucle principal de la ventana
ventana.mainloop()
