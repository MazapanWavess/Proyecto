import tkinter as tk
from datetime import datetime, timedelta

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Ejemplo de Frame Temporal")

        self.frame_temporal = tk.Frame(root, width=200, height=100, bg="lightblue")
        self.frame_temporal.pack(padx=10, pady=10)

        # Obtener el tiempo actual
        self.tiempo_inicial = datetime.now()

        # Llama a la función para comprobar si se debe ocultar el frame cada 1000 milisegundos (1 segundo)
        self.root.after(1000, self.verificar_ocultar_frame)

    def verificar_ocultar_frame(self):
        tiempo_actual = datetime.now()

        # Calcula la diferencia de tiempo desde el inicio
        diferencia_tiempo = tiempo_actual - self.tiempo_inicial

        # Si han pasado más de 3000 milisegundos (3 segundos), oculta el frame
        if diferencia_tiempo.total_seconds() >= 3:
            self.frame_temporal.pack_forget()
        else:
            # Programa una nueva llamada después de 1000 milisegundos (1 segundo) para verificar nuevamente
            self.root.after(1000, self.verificar_ocultar_frame)

# Crear la ventana principal
root = tk.Tk()
app = VentanaPrincipal(root)
root.mainloop()
