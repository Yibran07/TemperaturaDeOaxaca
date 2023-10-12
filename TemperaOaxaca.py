import tkinter as tk
from tkinter import messagebox
from datetime import date
from statistics import mean
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import matplotlib.dates as mdates

class DatosClima:
    def __init__(self, fecha, temperatura):
        self.fecha = fecha
        self.temperatura = temperatura

class Almacenamiento:
    def __init__(self):
        self.datos = []
        self.fechas = set()

    def agregar_datos(self, datos):
        if datos.fecha in self.fechas:
            messagebox.showinfo("Error", "La fecha ya ha sido registrada anteriormente.")
        else:
            self.datos.append(datos)
            self.fechas.add(datos.fecha) 
            messagebox.showinfo("Éxito", "Datos registrados correctamente.")


    def obtener_datos(self):
        return self.datos

class Principal:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Recopilación de Datos Climáticos")
        self.ventana.geometry("500x300")
        self.ventana.config(bg='bisque2')

        self.etiqueta_fecha = tk.Label(ventana, text="Fecha (Formato: AAAA-MM-DD):", bg="bisque2")
        self.etiqueta_fecha.pack()
        self.entrada_fecha = tk.Entry(ventana)
        self.entrada_fecha.pack(pady="10")

        self.etiqueta_temperatura = tk.Label(ventana, text="Temperatura (°C):", bg="bisque2")
        self.etiqueta_temperatura.pack()
        self.entrada_temperatura = tk.Entry(ventana)
        self.entrada_temperatura.pack(pady="10")

        self.boton_registrar = tk.Button(ventana, text="Registrar Datos", command=self.registrar_datos)
        self.boton_registrar.pack(pady="10")

        self.boton_visualizar = tk.Button(ventana, text="Visualizar Datos", command=self.visualizar_datos)
        self.boton_visualizar.pack(pady="10")

        self.boton_estadisticas = tk.Button(ventana, text="Calcular Estadísticas", command=self.calcular_estadisticas)
        self.boton_estadisticas.pack(pady="10")

        self.almacenamiento = Almacenamiento()

    def registrar_datos(self):

        fecha = self.entrada_fecha.get()
        temperatura = self.entrada_temperatura.get() 

        try:
            fecha = date.fromisoformat(fecha)
            temperatura = float(temperatura)
                    
        except ValueError:
            messagebox.showerror("Error", "Ingrese una fecha válida o temperatura numérica.")
            return

        datos = DatosClima(fecha, temperatura)
        self.almacenamiento.agregar_datos(datos)

    def visualizar_datos(self):
        fechas = [date2num(datos.fecha) for datos in self.almacenamiento.obtener_datos()]
        temperaturas = [datos.temperatura for datos in self.almacenamiento.obtener_datos()]

        fig, ax = plt.subplots(figsize=(10, 6))
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.plot_date(fechas, temperaturas, '-o', label='Temperatura (°C)')
        plt.title('Datos Climáticos')
        plt.xlabel('Fecha')
        plt.ylabel('Temperatura (°C)')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()

    def calcular_estadisticas(self):
        temperaturas = [datos.temperatura for datos in self.almacenamiento.obtener_datos()]
        if temperaturas:
            temperatura_promedio = mean(temperaturas)
            temperatura_maxima = max(temperaturas)
            temperatura_minima = min(temperaturas)
            messagebox.showinfo("Estadísticas Climáticas", f"Temperatura Promedio: {temperatura_promedio}°C\nTemperatura Máxima: {temperatura_maxima}°C\nTemperatura Mínima: {temperatura_minima}°C")

if __name__ == "__main__":
    ventana_principal = tk.Tk()
    app = Principal(ventana_principal)
    ventana_principal.mainloop()
