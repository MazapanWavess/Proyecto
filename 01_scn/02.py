import sqlite3
import datetime
import tkinter as tk
from tkinter import messagebox

conexion = sqlite3.connect('a.db')
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS productos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT,
                    precio REAL,
                    inversion REAL,
                    cantidad INTEGER,
                    precio_unidad REAL
                )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ventas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    producto_id INTEGER,
                    cantidad INTEGER,
                    fecha DATE,
                    venta REAL,
                    ganancia REAL,
                    FOREIGN KEY (producto_id) REFERENCES productos(id)
                )''')

def agregar_producto():
    nombre = entry_nombre.get()
    precio = float(entry_precio.get())
    inversion = float(entry_inversion.get())
    cantidad = int(entry_cantidad.get())
    precio_unidad = inversion / cantidad

    cursor.execute("INSERT INTO productos (nombre, precio, inversion, cantidad, precio_unidad) VALUES (?, ?, ?, ?, ?)",
                    (nombre, precio, inversion, cantidad, precio_unidad))
    conexion.commit()
    messagebox.showinfo("Éxito", "Producto agregado con éxito.")

def listar_productos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if productos:
        result_text.set("\nLista de productos:\n")
        for producto in productos:
            result_text.set(result_text.get() + f"ID: {producto[0]}\nNombre: {producto[1]}\nPrecio comercial: {producto[2]}\nInversión: {producto[3]}\nCantidad: {producto[4]}\nPrecio por unidad: {producto[5]}\n-------------------------\n")
    else:
        result_text.set("No hay productos registrados.")

def ver_producto():
    id_producto = int(entry_id_producto.get())

    cursor.execute("SELECT * FROM productos WHERE id=?", (id_producto,))
    producto = cursor.fetchone()

    if producto:
        result_text.set(f"\nDetalles del Producto:\nNombre: {producto[1]}\nPrecio comercial: {producto[2]}\nInversión requerida: {producto[3]}\nCantidad: {producto[4]}\nPrecio por unidad: {producto[5]} ")
    else:
        result_text.set("El producto no se encontró en la lista.\n")

def vender_producto():
    id_producto = int(entry_id_vender.get())
    cantidad = int(entry_cantidad_vender.get())
    fecha = datetime.date.today()

    cursor.execute("SELECT * FROM productos WHERE id=?", (id_producto,))
    producto = cursor.fetchone()

    if producto:
        if producto[4] >= cantidad:
            venta = cantidad * producto[2]
            ganancia = (producto[2] * cantidad) - (producto[5]*cantidad)

            nueva_cantidad = producto[4] - cantidad
            cursor.execute("UPDATE productos SET cantidad=? WHERE id=?", (nueva_cantidad, id_producto))

            cursor.execute("INSERT INTO ventas (producto_id, cantidad, fecha, ganancia, venta) VALUES (?, ?, ?, ?, ?)",
                            (id_producto, cantidad, fecha, ganancia, venta))
            conexion.commit()
            result_text.set(f"Venta realizada con éxito. Ganancia: {ganancia}")
        else:
            result_text.set("No hay suficiente cantidad de producto disponible.\n")
    else:
        result_text.set("El producto no se encontró en la lista.\n")

def ver_ventas_dia():
    fecha_consulta = datetime.date.today()

    cursor.execute("SELECT * FROM ventas WHERE fecha=?", (fecha_consulta,))
    ventas = cursor.fetchall()

    if ventas:
        total_ventas = sum([venta[2] for venta in ventas])
        result_text.set(f"\nVentas del día {fecha_consulta}:\n")
        for venta in ventas:
            result_text.set(result_text.get() + f"ID: {venta[0]}, Producto ID: {venta[1]}, Cantidad: {venta[2]}, Venta: {venta[4]} , Ganancia: {venta[5]} ,Fecha: {venta[3]}\n")
        result_text.set(result_text.get() + f"Total de ventas: {total_ventas}")
    else:
        result_text.set("No se encontraron ventas para la fecha especificada.")

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Control de Productos")

# Variables de entrada
entry_nombre = tk.Entry(root)
entry_precio = tk.Entry(root)
entry_inversion = tk.Entry(root)
entry_cantidad = tk.Entry(root)

entry_id_producto = tk.Entry(root)
entry_id_vender = tk.Entry(root)
entry_cantidad_vender = tk.Entry(root)

# Variable para mostrar resultados
result_text = tk.StringVar()
result_text.set("")

# Funciones de botones
def btn_agregar_producto():
    agregar_producto()

def btn_listar_productos():
    listar_productos()

def btn_ver_producto():
    ver_producto()

def btn_vender_producto():
    vender_producto()

def btn_ver_ventas_dia():
    ver_ventas_dia()

# Botones y etiquetas en la ventana
label_nombre = tk.Label(root, text="Nombre del Producto:")
label_precio = tk.Label(root, text="Precio del Producto:")
label_inversion = tk.Label(root, text="Inversión del Producto:")
label_cantidad = tk.Label(root, text="Cantidad Comprada:")

label_id_producto = tk.Label(root, text="ID del Producto:")
label_id_vender = tk.Label(root, text="ID del Producto a Vender:")
label_cantidad_vender = tk.Label(root, text="Cantidad a Vender:")

btn_agregar = tk.Button(root, text="Agregar Producto", command=btn_agregar_producto)
btn_listar = tk.Button(root, text="Listar Productos", command=btn_listar_productos)
btn_ver = tk.Button(root, text="Ver Detalles", command=btn_ver_producto)
btn_vender = tk.Button(root, text="Vender Producto", command=btn_vender_producto)
btn_ver_ventas = tk.Button(root, text="Ver Ventas del Día", command=btn_ver_ventas_dia)

label_nombre.grid(row=0, column=0, padx=10, pady=10)
label_precio.grid(row=1, column=0, padx=10, pady=10)
label_inversion.grid(row=2, column=0, padx=10, pady=10)
label_cantidad.grid(row=3, column=0, padx=10, pady=10)

entry_nombre.grid(row=0, column=1, padx=10, pady=10)
entry_precio.grid(row=1, column=1, padx=10, pady=10)
entry_inversion.grid(row=2, column=1, padx=10, pady=10)
entry_cantidad.grid(row=3, column=1, padx=10, pady=10)

btn_agregar.grid(row=4, column=0, columnspan=2, pady=10)

label_id_producto.grid(row=5, column=0, padx=10, pady=10)
entry_id_producto.grid(row=5, column=1, padx=10, pady=10)
btn_ver.grid(row=6, column=0, columnspan=2, pady=10)

label_id_vender.grid(row=7, column=0, padx=10, pady=10)
entry_id_vender.grid(row=7, column=1, padx=10, pady=10)
label_cantidad_vender.grid(row=8, column=0, padx=10, pady=10)
entry_cantidad_vender.grid(row=8, column=1, padx=10, pady=10)
btn_vender.grid(row=9, column=0, columnspan=2, pady=10)

btn_ver_ventas.grid(row=10, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, textvariable=result_text)
label_result.grid(row=11, column=0, columnspan=2, pady=10)

root.mainloop()

conexion.close()
