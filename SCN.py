# Modulos
from tkinter import *
import sqlite3
from tkinter import messagebox
import datetime
#from PIL import ImageTk,Image

# Conexion con la base de datos

conexion = sqlite3.connect('SCN.db')
cursor = conexion.cursor()

# Tablas bases de datos

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
                    nombre TEXT,
                    cantidad INTEGER,
                    fecha DATE,
                    venta REAL,
                    ganancia REAL
    )
''')


# Ventana principal

scn = Tk()
scn.geometry("925x500")
scn.title("Sofware de Control de Negocios (SCN)")
scn.config(bg='white')
scn.iconbitmap(r"E:\EMMA\imagens\icono.ico")


# Clases
class CajasDeTexto:
    def __init__(self,ubicacion,ancho,color1,color2,nombre,x,y,texto):
        
        self.ubicacion = ubicacion
        self.ancho = ancho
        self.color1 = color1
        self.color2 = color2
        self.nombre = nombre
        self.x = x
        self.y = y
        self.texto = texto

    def Caja(self):

        def on_enter(e):
            etiqueta.delete(0,'end')    
        def on_leave(e):
            if etiqueta.get()=='':   
                etiqueta.insert(0,self.texto)
        
        etiqueta = StringVar()
        etiqueta=Entry(self.ubicacion,
                        width=self.ancho,
                        fg=self.color1,
                        border=0,
                        bg=self.color2,
                        )
        etiqueta.config(font=('Microsoft YaHei UI Light',11,))
        etiqueta.bind("<FocusIn>",on_enter)
        etiqueta.bind("<FocusOut>",on_leave)
        etiqueta.insert(0,self.nombre)
        etiqueta.place(x=self.x,y=self.y)

#--------------------------------------------------------------------------------------------------------------

class BotonesDiferentes:
    def __init__(self,ubicacion,ancho,TamañoLetra,texto,color1,color2,x,y,comando):
        
        self.ubicacion  = ubicacion
        self.ancho = ancho
        self.TamañoLetra = TamañoLetra
        self.texto = texto
        self.color1 = color1
        self.color2 = color2
        self.x = x
        self.y = y
        self.comando = comando

    def Botones(self):

        def entrar(e):
            Boton["background"] = self.color2
            Boton["foreground"] = self.color1

        def salir(e):   
            Boton["background"] = self.color1
            Boton["foreground"] = self.color2
        
        Boton = Button(self.ubicacion,
                        width=self.ancho,
                        pady=self.TamañoLetra,
                        text=self.texto,
                        bg=self.color1,
                        fg=self.color2,
                        border=0,
                        activeforeground=self.color1,
                        activebackground=self.color2,
                        command=self.comando)
        Boton.place(x=self.x, y=self.y)
        Boton.bind("<Enter>", entrar)
        Boton.bind("<Leave>", salir)

#--------------------------------------------------------------------------------------------------------------
class Home:
    def __init__(self):
        

        self.home = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.home.place(x=0,y=0)

        self.home2 = Frame(self.home,width=925,
                            height=460,
                            bg="#393E46")
        self.home2.place(x=0,y=40)


        self.boton_home = BotonesDiferentes(self.home,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_agregar_producto = Label(self.home,
                                            text="Inicio",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_agregar_producto.place(x=50,y=4)
        self.eti_agregar_producto.config(font=('Microsoft YaHei UI Light', 15))


#--------------------------------------------------------------------------------------------------------------

class Menu:
    def __init__(self):
        
        def quitar_menu():
            self.menu.destroy()

        self.menu = Frame(scn,width=300,
                            height=500,
                            bg="#00ADB5")
        self.menu.place(x=0,y=0)

        self.quitar_menu = Button(self.menu,
                                    text="X",
                                    command=quitar_menu)
        self.quitar_menu.place(x=5,y=8)

        self.boton_home = BotonesDiferentes(self.menu,
                                            5,
                                            3,
                                            "X",
                                            "#00ADB5",#00ADB5
                                            '#222831',
                                            5,
                                            8,
                                            quitar_menu,)
        self.boton_home.Botones()
        
        """
        # BOTON 1 (HOME)
        self.boton_home = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "H O M E",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            80,
                                            Home)
        self.boton_home.Botones()"""

        # BOTON 2 (AGREGAR PRODUCTO)
        self.boton_Agregar_Producto = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "AGREGAR PRODUCTO",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            117,
                                            AgregarProducto)
        self.boton_Agregar_Producto.Botones()

        # BOTON 3 (LISTA DE PRODUCTOS PRODUCTO)
        self.boton_lista_Productos = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "LISTA DE PRODUCTOS",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            157,
                                            ListaProductos)
        self.boton_lista_Productos.Botones()

        # BOTON 4 (BUSCAR PRODUCTO)
        self.boton_buscar_producto = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "BUSCAR PRODUCTO",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            191,
                                            BuscarProductos)
        self.boton_buscar_producto.Botones()

        # BOTON 5 (REGISTAR VENTA DE PRODUCTO)
        self.boton_registrar_venta = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "REGISTRAR VENTA",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            228,
                                            RegistrarVenta)
        self.boton_registrar_venta.Botones()

        # BOTON 6 (VER VENTAS DEL DIA)
        self.boton_ventas_dia = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "VENTAS DEL DIA",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            265,
                                            VentasDelDia)
        self.boton_ventas_dia.Botones()

        # BOTON 7 (VER VENTAS DE DIAS ANTERIORES)
        self.boton_ventas_anteriores = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            "VENTAS ANTERIORES",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            302,
                                            VentasAnteriores)
        self.boton_ventas_anteriores.Botones()

        # BOTON 8 (AYUDA)
        self.boton_ayuda = BotonesDiferentes(self.menu,
                                            42,
                                            10,
                                            " A Y U D A ",
                                            "#00ADB5",
                                            '#2d3541',
                                            0,
                                            463,
                                            Ayuda)
        self.boton_ayuda.Botones()


#--------------------------------------------------------------------------------------------------------------
class AgregarProducto:
    def __init__(self):

        def agregar_productos_tablas():

            def quitar_frame_error():
                error.destroy()

            def quitar_frame_correcto():
                correcto.destroy()

            nombre = self.nombre.get()
            inversion = float(self.inversion.get())
            cantidad = float(self.cantidad.get())
            precio = float(self.precio.get())

            # Calcular el precio por unidad
            precio_unidad = inversion / cantidad

            cursor.execute("SELECT * FROM productos WHERE nombre = ?", (nombre,))
            existe_el_producto = cursor.fetchone()

            if existe_el_producto:

                error = Frame(self.agregar_producto,
                            width=300,
                            height=170,
                            bg="#00ADB5",
                            )
                error.place(x=330,y=150)

                eti_error = Label(error,
                                    text=("El producto ya ha sido agregado\nintentalo de nuevo"),
                                    font=('Microsoft YaHei UI Light', 15),
                                    fg="#222831",
                                    bg="#00ADB5")
                eti_error.place(x=0,y=20)

                boton_error_regresar = BotonesDiferentes(error,
                                    40,
                                    10,
                                    "REGRESAR",
                                    "#393E46",#gris
                                    '#328e93',#azul
                                    8,
                                    120,
                                    quitar_frame_error)
                boton_error_regresar.Botones()  


            else:
                cursor.execute("INSERT INTO productos (nombre, precio, inversion, cantidad, precio_unidad) VALUES (?, ?, ?, ?, ?)",
                                (nombre, precio, inversion, cantidad, precio_unidad))
                conexion.commit()

                correcto = Frame(self.agregar_producto,
                            width=300,
                            height=170,
                            bg="#00ADB5",
                            )
                correcto.place(x=330,y=150)

                eti_correcto = Label(correcto,
                                    text=("El producto ha sido agregado\n exitosamente"),
                                    font=('Microsoft YaHei UI Light', 15),
                                    fg="#222831",
                                    bg="#00ADB5")
                eti_correcto.place(x=10,y=20)

                boton_correcto_regresar = BotonesDiferentes(correcto,
                                    40,
                                    10,
                                    "REGRESAR",
                                    "#393E46",#gris
                                    '#328e93',#azul
                                    8,
                                    120,
                                    quitar_frame_correcto)
                boton_correcto_regresar.Botones()          

        #####
        self.agregar_producto = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.agregar_producto.place(x=0,y=0)

        self.agregar_producto2 = Frame(self.agregar_producto,width=925,
                            height=460,
                            bg="#393E46")
        self.agregar_producto2.place(x=0,y=40)



        self.boton_home = BotonesDiferentes(self.agregar_producto,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_agregar_producto = Label(self.agregar_producto,
                                            text="Agregar Producto",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_agregar_producto.place(x=50,y=4 )
        self.eti_agregar_producto.config(font=('Microsoft YaHei UI Light', 15))

        #1
        self.eti_agregar = Label(self.agregar_producto,
                                            text="Nombre Del Producto:",
                                            fg="#00ADB5",
                                            bg="#393E46")
        self.eti_agregar.place(x=200,y=100 )
        self.eti_agregar.config(font=('Microsoft YaHei UI Light', 15))

        self.producto=StringVar()
        self.nombre = Entry(self.agregar_producto,textvariable=self.producto,width=50)
        self.nombre.place(x=200,y=130 )
        self.nombre.config(font=('Microsoft YaHei UI Light', 15))
        self.nombre.get()

        #2
        self.eti_agregar = Label(self.agregar_producto,
                                            text="Ingresar Invercion (lote):",
                                            fg="#00ADB5",
                                            bg="#393E46")
        self.eti_agregar.place(x=200,y=170 )
        self.eti_agregar.config(font=('Microsoft YaHei UI Light', 15))
        
        self.invercion_lote=DoubleVar()
        self.inversion = Entry(self.agregar_producto,textvariable=self.invercion_lote,width=50)
        self.inversion.place(x=200,y=200 )
        self.inversion.config(font=('Microsoft YaHei UI Light', 15))
        self.inversion.get()

        #3
        self.eti_agregar = Label(self.agregar_producto,
                                            text="Productos Disponibles:",
                                            fg="#00ADB5",
                                            bg="#393E46")
        self.eti_agregar.place(x=200,y=240 )
        self.eti_agregar.config(font=('Microsoft YaHei UI Light', 15))
        
        self.pro_disponibles=DoubleVar()
        self.cantidad = Entry(self.agregar_producto,textvariable=self.pro_disponibles,width=50)
        self.cantidad.place(x=200,y=270 )
        self.cantidad.config(font=('Microsoft YaHei UI Light', 15))

        #4
        self.eti_agregar = Label(self.agregar_producto,
                                            text="Precio De Venta:",
                                            fg="#00ADB5",
                                            bg="#393E46")
        self.eti_agregar.place(x=200,y=300 )
        self.eti_agregar.config(font=('Microsoft YaHei UI Light', 15))
        
        self.precio_venta=DoubleVar()
        self.precio = Entry(self.agregar_producto,textvariable=self.precio_venta,width=50)
        self.precio.place(x=200,y=330 )
        self.precio.config(font=('Microsoft YaHei UI Light', 15))
        self.precio.get()


        self.boton = BotonesDiferentes(self.agregar_producto,
                                            40,
                                            10,
                                            "AGREGAR",
                                            "#00ADB5",#00ADB5
                                            '#222831',
                                            330,
                                            400,
                                            agregar_productos_tablas)
        self.boton.Botones()  



#--------------------------------------------------------------------------------------------------------------
class ListaProductos:
    def __init__(self):
        
        self.lista_producto = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.lista_producto.place(x=0,y=0)

        self.lista_producto2 = Frame(self.lista_producto,width=925,
                            height=460,
                            bg="#393E46")
        self.lista_producto2.place(x=0,y=40)

        self.boton_home = BotonesDiferentes(self.lista_producto,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_lista_producto = Label(self.lista_producto,
                                            text="Lista De Productos",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_lista_producto.place(x=50,y=4 )
        self.eti_lista_producto.config(font=('Microsoft YaHei UI Light', 15))

        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()

        y=100

        if productos:
            mostrar_producto= Label(self.lista_producto,text="Lista de productos:")
            mostrar_producto.place(x=50,y=50)
            for producto in productos:
                mostrar_productos_ordenados = Label(self.lista_producto,text=( f"ID: {producto[0]}Nombre: {producto[1]} - Precio comercial: {producto[2]} - Inversión: {producto[3]} - Cantidad: {producto[4]} - Precio por unidad: {producto[5]}"))
                mostrar_productos_ordenados.place(x=50,y=y)
                y = y+ 50


        else:
            no_productos= Label(self.lista_producto,"Productos no disponibles")
            no_productos.place(x=50,y=50)

#--------------------------------------------------------------------------------------------------------------
class BuscarProductos:
    def __init__(self):

        def pedir_producto():

            nombre = self.producto.get()

            cursor.execute("SELECT * FROM productos WHERE nombre=?", (nombre,))
            producto = cursor.fetchone()

            if producto:
  

                mostrar_producto=Label(self.buscar_producto,text=(f"Detalles del Producto:\nNombre: {producto[1]}\nPrecio comercial: {producto[2]}\nInversión requerida: {producto[3]}\nCantidad: {producto[4]}\nPrecio por unidad: {producto[5]} "))
                mostrar_producto.config(font=('Microsoft YaHei UI Light', 20),
                                        fg="#222831",
                                        bg="#00ADB5")
                mostrar_producto.place(x=300,y=250)
            else:

                nose_encontro=Label(self.buscar_producto,text=("El producto no se encontró en la lista.\n"))
                nose_encontro.place(x=20,y=50)

        self.buscar_producto = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.buscar_producto.place(x=0,y=0)

        self.buscar_producto2 = Frame(self.buscar_producto,width=925,
                            height=460,
                            bg="#393E46")
        self.buscar_producto2.place(x=0,y=40)

        self.boton_home = BotonesDiferentes(self.buscar_producto,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_buscar_producto = Label(self.buscar_producto,
                                            text="Buscar Productos",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_buscar_producto.place(x=50,y=4 )
        self.eti_buscar_producto.config(font=('Microsoft YaHei UI Light', 15))
        
        #1
        self.eti_agregar = Label(self.buscar_producto,
                                            text="Nombre Del Producto a Buscar:",
                                            fg="#00ADB5",
                                            bg="#393E46")
        self.eti_agregar.place(x=200,y=100 )
        self.eti_agregar.config(font=('Microsoft YaHei UI Light', 15))

        self.producto=StringVar()
        self.producto = Entry(self.buscar_producto,textvariable=self.producto,width=50)
        self.producto.place(x=200,y=130 )
        self.producto.config(font=('Microsoft YaHei UI Light', 15))
        self.producto.get()

        self.boton = BotonesDiferentes(self.buscar_producto,
                                            40,
                                            10,
                                            " BUSCAR ",
                                            "#00ADB5",#00ADB5
                                            '#222831',
                                            330,
                                            170,
                                            pedir_producto,)
        self.boton.Botones()  



#--------------------------------------------------------------------------------------------------------------
class RegistrarVenta:
    def __init__(self):
        
        def vender_producto():

            def quitar_frame_error():
                exito.destroy()

            def quitar_frame_cantidad_faltante():
                cantidad_faltante.destroy()

            def quitar_frame_no_disponible():
                no_disponible.destroy()

            nombre = self.nombre.get()
            cantidad = float(self.cantidad.get())
            fecha = datetime.date.today()

            cursor.execute("SELECT * FROM productos WHERE nombre=?", (nombre,))
            producto = cursor.fetchone()

            if producto:
                if producto[4] >= cantidad:
                    venta = cantidad * producto[2]
                    ganancia = (producto[2] * cantidad) - (producto[5]*cantidad)

                    nueva_cantidad = producto[4] - cantidad
                    cursor.execute("UPDATE productos SET cantidad=? WHERE nombre=?", (nueva_cantidad, nombre))

                    cursor.execute("INSERT INTO ventas (nombre,cantidad, fecha, ganancia, venta) VALUES ( ?, ?, ?, ?, ?)",
                                    (nombre,cantidad, fecha, ganancia, venta))
                    conexion.commit()

                    exito = Frame(self.registra_venta,
                            width=300,
                            height=170,
                            bg="#00ADB5",
                            )
                    exito.place(x=330,y=150)

                    eti_exito = Label(exito,
                                    text=(f"Venta realizada con éxito.\n Ganancia: {ganancia}"),
                                    font=('Microsoft YaHei UI Light', 15),
                                    fg="#222831",
                                    bg="#00ADB5")
                    eti_exito.place(x=30,y=20)

                    boton_exito_regresar = BotonesDiferentes(exito,
                                    40,
                                    10,
                                    "REGRESAR",
                                    "#393E46",#gris
                                    '#328e93',#azul
                                    8,
                                    120,
                                    quitar_frame_error)
                    boton_exito_regresar.Botones()  

                else:
                    cantidad_faltante = Frame(self.registra_venta,
                            width=300,
                            height=170,
                            bg="#00ADB5",
                            )
                    cantidad_faltante.place(x=330,y=150)

                    eti_cantidad_faltante = Label(cantidad_faltante,
                                    text=(f"No hay suficiente cantidad \nde producto disponible."),
                                    font=('Microsoft YaHei UI Light', 15),
                                    fg="#222831",
                                    bg="#00ADB5")
                    eti_cantidad_faltante.place(x=30,y=20)

                    boton_cantidad_faltante_regresar = BotonesDiferentes(cantidad_faltante,
                                    40,
                                    10,
                                    "REGRESAR",
                                    "#393E46",#gris
                                    '#328e93',#azul
                                    8,
                                    120,
                                    quitar_frame_cantidad_faltante)
                    boton_cantidad_faltante_regresar.Botones()  

            else:
                no_disponible = Frame(self.registra_venta,
                        width=300,
                        height=170,
                        bg="#00ADB5",
                        )
                no_disponible.place(x=330,y=150)

                eti_no_disponible = Label(no_disponible,
                                text=(f"El producto no esta \n disponible."),
                                font=('Microsoft YaHei UI Light', 15),
                                fg="#222831",
                                bg="#00ADB5")
                eti_no_disponible.place(x=60,y=20)

                boton_no_disponible_regresar = BotonesDiferentes(no_disponible,
                                40,
                                10,
                                "REGRESAR",
                                "#393E46",#gris
                                '#328e93',#azul
                                8,
                                120,
                                quitar_frame_no_disponible)
                boton_no_disponible_regresar.Botones()  
                
        

        self.registra_venta = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.registra_venta.place(x=0,y=0)

        self.registra_venta2 = Frame(self.registra_venta,width=925,
                            height=460,
                            bg="#393E46")
        self.registra_venta2.place(x=0,y=40)

        self.boton_home = BotonesDiferentes(self.registra_venta,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_registrar_venta = Label(self.registra_venta,
                                            text="Registrar Venta",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_registrar_venta.place(x=50,y=4 )
        self.eti_registrar_venta.config(font=('Microsoft YaHei UI Light', 15))

        ### 1
        self.eti_agregar_venta = Label(self.registra_venta,
                                            text="Nombre Del Producto:",
                                            fg="#00ADB5",
                                            bg="#393E46")
        self.eti_agregar_venta.place(x=200,y=100 )
        self.eti_agregar_venta.config(font=('Microsoft YaHei UI Light', 15))

        self.producto=StringVar()
        self.nombre = Entry(self.registra_venta,textvariable=self.producto,width=50)
        self.nombre.place(x=200,y=130 )
        self.nombre.config(font=('Microsoft YaHei UI Light', 15))
        self.nombre.get()

        #2
        self.eti_agregar = Label(self.registra_venta,
                                            text="Ingresar Invercion (lote):",
                                            fg="#00ADB5",
                                            bg="#393E46")
        self.eti_agregar.place(x=200,y=170 )
        self.eti_agregar.config(font=('Microsoft YaHei UI Light', 15))
        
        self.cantidad_lote=DoubleVar()
        self.cantidad = Entry(self.registra_venta,textvariable=self.cantidad_lote,width=50)
        self.cantidad.place(x=200,y=200 )
        self.cantidad.config(font=('Microsoft YaHei UI Light', 15))
        self.cantidad.get()

        self.boton = BotonesDiferentes(self.registra_venta,
                                            40,
                                            10,
                                            "AGREGAR",
                                            "#00ADB5",#00ADB5
                                            '#222831',
                                            330,
                                            400,
                                            vender_producto)
        self.boton.Botones()  

#--------------------------------------------------------------------------------------------------------------
class VentasDelDia:
    def __init__(self):
        
        self.ventas_del_dia = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.ventas_del_dia.place(x=0,y=0)

        self.ventas_del_dia2 = Frame(self.ventas_del_dia,width=925,
                            height=460,
                            bg="#393E46")
        self.ventas_del_dia2.place(x=0,y=40)

        self.boton_home = BotonesDiferentes(self.ventas_del_dia,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_ventas_del_dia = Label(self.ventas_del_dia,
                                            text="Ventas Del Dia",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_ventas_del_dia.place(x=50,y=4 )
        self.eti_ventas_del_dia.config(font=('Microsoft YaHei UI Light', 15))



        ###########

        fecha_consulta = datetime.date.today()

        cursor.execute("SELECT * FROM ventas WHERE fecha=?", (fecha_consulta,))
        ventas = cursor.fetchall()

        if ventas:
            total_ventas = sum([venta[2] for venta in ventas])
            result_fecha=Label(self.ventas_del_dia,text=(f"Ventas del día de hoy :"))
            result_fecha.config(font=('Microsoft YaHei UI Light', 13),
                                bg="#393E46",
                                fg="#00ADB5")
            result_fecha.place(x=50,y=50)
            for venta in ventas:
                mostrar_venta=Label(self.ventas_del_dia,text=( f"Num.Venta: {venta[0]}, Producto: {venta[1]}, Cantidad: {venta[2]}, Venta: {venta[4]} , Ganancia: {venta[5]} ,Fecha: {venta[3]}\n"))
                mostrar_venta.config(font=('Microsoft YaHei UI Light', 15))
                mostrar_venta.place(x=50,y=230)
            mostrar_venta2=Label(self.ventas_del_dia,text=(f"Total de ventas: {total_ventas}"))
            mostrar_venta2.place(x=50,y=260)

        else:
            mostrar_venta3=Label(self.ventas_del_dia,text="No se encontraron ventas para la fecha especificada.")
            mostrar_venta3.place(x=50,y=260)



#--------------------------------------------------------------------------------------------------------------
class VentasAnteriores:
    def __init__(self):
        
        self.ventas_anteriores = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.ventas_anteriores.place(x=0,y=0)

        self.ventas_anteriores2 = Frame(self.ventas_anteriores,width=925,
                            height=460,
                            bg="#393E46")
        self.ventas_anteriores2.place(x=0,y=40)

        self.boton_home = BotonesDiferentes(self.ventas_anteriores,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d3541
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_home.Botones()

        self.eti_ventas_anteriores = Label(self.ventas_anteriores,
                                            text="Ventas Anteriores",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_ventas_anteriores.place(x=50,y=4 )
        self.eti_ventas_anteriores.config(font=('Microsoft YaHei UI Light', 15))
#--------------------------------------------------------------------------------------------------------------
class Ayuda:
    def __init__(self):
        

        self.ayuda = Frame(scn,width=925,
                            height=500,
                            bg="#222831")
        self.ayuda.place(x=0,y=0)

        self.ayuda2 = Frame(self.ayuda,width=925,
                            height=460,
                            bg="#393E46")
        self.ayuda2.place(x=0,y=40)

        self.texto1 = Label(self.ayuda2,text="SCN\n""SCN es un software desarrollado para obtener una mejor administracion en tu negocio o comercio puesto que \n gracias a su eficiencia resulta ser muy facil de utilizar. \n \n""¡COMO USAR SCN? \n"
"------------------ \n""AGREGAR PRODUCTO:Esta opcion sirve para poder registrar los productos y sus datos principales como su nombre, \ninvercion, cantidad disponible y precio de venta. Para poder guardar estos datos se oprime al final el boton 'AGREGAR'.\n"
"------------------ \n""BUSCAR PRODUCTO:Utilice esta opcion para poder acceder a los registros de un producto en especifico, Ingrese el ID del\n producto deseado para consultar la información. \n"
"------------------ \n""LISTA DE PRODUCTOS:Consulta todos los productos registrados en el sistema hasta el momento con esta opcion.  \n"
"------------------ \n""REGISTRAR VENTA:Registrar la venta de un producto previamente registrado, unicamente necesita el ID del producto\n y la cantidad vendida. \n"
"------------------ \n""VENTAS DEL DIA:Accede a las ventas registradas del dia en curso con esta opcion. \n"
"------------------ \n""VENTAS ANTERIORES:Accede a los registros de las ventas de dias anteriores, para esto se ingresa la fecha en formato DD/MM/AAAA \ny se confirma la fecha\n"
"------------------ \n  ¡Optimiza la gestión de tu negocio con SCN, la solución eficiente y fácil de utilizar para el éxito empresarial!")

        self.texto1.configure(anchor="center",
                                font=('Microsoft YaHei UI Light', 10),
                                height=24,
                                width=115,
                                bg="#393E46",
                                fg="white")
        self.texto1.place(x=00,y=00)
        
        
        self.boton_ayuda = BotonesDiferentes(self.ayuda,
                                            5,
                                            3,
                                            "M",
                                            "#222831",#2d35419
                                            '#00ADB5',
                                            5,
                                            8,
                                            Menu,)
        self.boton_ayuda.Botones()

        self.eti_ayuda = Label(self.ayuda,
                                            text="AYUDA",
                                            fg="#EEEEEE",
                                            bg="#222831")
        self.eti_ayuda.place(x=50,y=4 )
        self.eti_ayuda.config(font=('Microsoft YaHei UI Light', 15))

        #FRAME

#--------------------------------------------------------------------------------------------------------------

class RegistrarCuenta:
    def __init__(self):

        # Frames Para registrarse
        self.registra_cuenta = Frame(scn,width=925,
                                    height=500,
                                    bg="#222831")
        self.registra_cuenta.place(x=0,y=0)
        
        #Frame para Cajas de texto registrarse
        self.cajas_registrar = Frame(self.registra_cuenta,
                                        width=350,
                                        height=350,
                                        bg="#222831")
        self.cajas_registrar.place(x=480,y=70)

        #Etiqueta "Registrarse"
        self.Etiqueta_Registrarse = Label(self.registra_cuenta,
                                            text="Registrarse",
                                            fg="#00ADB5",
                                            bg="#222831")
        self.Etiqueta_Registrarse.config(font=('Microsoft YaHei UI Light',23, 'bold'))
        self.Etiqueta_Registrarse.place(x=575,y=60)

        # Caja 1 (Usuario)
        self.Usuario = CajasDeTexto(self.cajas_registrar,
                                21,
                                "#00ADB5",
                                "#222831",
                                "Usuario",
                                30,
                                60,
                                "Usuario")
        self.Usuario.Caja()
        Frame(self.cajas_registrar,width=295,height=2,bg='white').place(x=25,y=87)

        # Caja 2 (Contraseña)
        self.Contraseña = CajasDeTexto(self.cajas_registrar,
                                21,
                                "#00ADB5",
                                "#222831",
                                "Contraseña",
                                30,
                                130,
                                "Contraseña")
        self.Contraseña.Caja()
        Frame(self.cajas_registrar,width=295,height=2,bg='white').place(x=25,y=157)

        # Caja 3 (Confirmar Contraseña)
        self.conf_contraseña = CajasDeTexto(self.cajas_registrar,
                                21,
                                "#00ADB5",
                                "#222831",
                                "Confirmar Contraseña",
                                30,
                                130+70,
                                "Confirmar Contraseña")
        self.conf_contraseña.Caja()
        Frame(self.cajas_registrar,width=295,height=2,bg='white').place(x=25,y=157+70)

        # Boton 1 (Registrarse)
        self.boton_registrarse = BotonesDiferentes(self.cajas_registrar,
                                                    39,
                                                    7,
                                                    "Registrarse",
                                                    "#00ADB5",
                                                    "#2d3541",
                                                    35,
                                                    264,
                                                    None)
        self.boton_registrarse.Botones()

        # Etiqueta Para llevar a inicio de sesion
        self.l1=Label(self.cajas_registrar,text="Ya tienes una cuenta?",fg="white",bg='#222831')
        self.l1.config(font=('Microsoft YaHei UI Light',9, ))
        self.l1.place(x=73,y=313)

        self.regresar=Button(self.cajas_registrar,
                        width=9,
                        text='Iniciar Sesion',
                        border=0,
                        bg='#222831',
                        fg='#00ADB5',
                        command=self.registra_cuenta.destroy)
        self.regresar.place(x=200,y=313)

#--------------------------------------------------------------------------------------------------------------

class InicioSesion:
    def __init__(self,principal):

        self.principal = principal
        self.inicio_sesion = Frame(scn,width=925,
                                height=500,
                                bg='#222831')
        self.inicio_sesion.place(x=0,y=0)

        # Etiqueta "Inicia Sesion"
        self.Eti_Inicia_Sesion = Label(scn,text="Inicia sesión", fg='#00ADB5', bg='#222831')
        self.Eti_Inicia_Sesion.config(font=('Microsoft YaHei UI Light', 24, 'bold'))
        self.Eti_Inicia_Sesion.place(x=570, y=60)

        # Frame para las cajas de texto
        self.Cajas_Texto=Frame(self.inicio_sesion,width=350,height=350,bg='#222831')
        self.Cajas_Texto.place(x=480,y=100)

        # Caja 1 (Usuario)
        self.Usuario = CajasDeTexto(self.Cajas_Texto,
                                21,
                                "#00ADB5",
                                "#222831",
                                "Usuario",
                                30,
                                60,
                                "Usuario")
        self.Usuario.Caja()
        Frame(self.Cajas_Texto, width=295, height=2, bg='WHITE').place(x=25, y=87)


        # Caja 2 (Contraseña)
        self.Contraseña = CajasDeTexto(self.Cajas_Texto,
                                21,
                                "#00ADB5",
                                "#222831",
                                "Contraseña",
                                30,
                                130,
                                "Contraseña")
        self.Contraseña.Caja()
        Frame(self.Cajas_Texto,width=295,height=2,bg='white').place(x=25,y=157)


        # Boton 1 (Inicio de sesion)
        self.boton_inicio_sesion = BotonesDiferentes(self.Cajas_Texto,
                                                    39,
                                                    7,
                                                    "Inicia Sesion",
                                                    "#00ADB5",
                                                    "#2d3541",
                                                    35,
                                                    204,
                                                    Home)
        self.boton_inicio_sesion.Botones()

        #imagen
        self.img1 = PhotoImage(file=(r"E:\EMMA\imagens\01.png"))
        Label(self.inicio_sesion,image=self.img1,border=0,bg='#222831').place(x=50,y=50)

        # Etiqueta si no tiene cuenta (Registrarse)
        self.l1=Label(self.Cajas_Texto,text="No tienes cuenta?",fg="white",bg='#222831')
        self.l1.config(font=('Microsoft YaHei UI Light',9, ))
        self.l1.place(x=95,y=250)

        self.b2=Button(self.Cajas_Texto,
                        width=8,
                        text='Registrate',
                        border=0,
                        bg='#222831',
                        fg='#00ADB5',
                        command=RegistrarCuenta)
        self.b2.place(x=200,y=250)


inicio_sesion_obj = InicioSesion(scn)


scn.mainloop()