import tkinter as tk
from tkinter import messagebox
import math


class CompiladorFigurasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Compilador de Figuras Geométricas en 2D")

        self.canvas = tk.Canvas(self.root, width=600, height=600, bg="white")
        self.canvas.grid(row=2, column=0, columnspan=2, pady=10)

        self.instruccion_label = tk.Label(self.root, text="Ingresa la instrucción:")
        self.instruccion_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.instruccion_entry = tk.Entry(self.root, width=50)
        self.instruccion_entry.grid(row=0, column=1, padx=10, pady=10)

        self.ejecutar_button = tk.Button(self.root, text="Ejecutar", command=self.ejecutar_instruccion)
        self.ejecutar_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.colores_validos = {
            "rojo": "red",
            "verde": "green",
            "azul": "blue",
            "amarillo": "yellow",
            "negro": "black",
            "blanco": "white",
            "naranja": "orange",
            "morado": "purple",
            "gris": "gray",
            "cyan": "cyan",
            "magenta": "magenta"
        }

    def ejecutar_instruccion(self):
        instruccion = self.instruccion_entry.get()
        try:
            self.procesar_instruccion(instruccion)
        except Exception as e:
            messagebox.showerror("Error", f"Instrucción inválida: {e}")

    def procesar_instruccion(self, instruccion):
        tokens = instruccion.split()
        if len(tokens) < 5:
            raise ValueError("La instrucción debe tener al menos 5 elementos para figuras básicas o 6 para rectángulos.")
        
        figura = tokens[0].upper()
        
        if figura == "RECT":
            if len(tokens) != 6:
                raise ValueError("La instrucción para RECT debe tener exactamente 6 parámetros: RECT X Y ANCHO ALTO COLOR.")
            try:
                x = int(tokens[1])
                y = int(tokens[2])
                ancho = int(tokens[3])
                alto = int(tokens[4])
                color = tokens[5].lower()
            except ValueError:
                raise ValueError("Coordenadas y dimensiones deben ser números enteros.")
            
            if color not in self.colores_validos:
                raise ValueError(f"Color '{color}' no reconocido. Usa un color válido como: {', '.join(self.colores_validos.keys())}")

            color_traducido = self.colores_validos[color]
            self.dibujar_rectangulo(x, y, ancho, alto, color_traducido)
        
        else:
            if len(tokens) < 5:
                raise ValueError("La instrucción debe tener al menos 5 elementos para figuras básicas.")
            try:
                x = int(tokens[1])
                y = int(tokens[2])
                tamaño = int(tokens[3])
                color = tokens[4].lower()
            except ValueError:
                raise ValueError("Coordenadas y dimensiones deben ser números enteros.")

            if color not in self.colores_validos:
                raise ValueError(f"Color '{color}' no reconocido. Usa un color válido como: {', '.join(self.colores_validos.keys())}")

            color_traducido = self.colores_validos[color]

            if figura == "CIRCULO":
                self.dibujar_circulo(x, y, tamaño, color_traducido)
            elif figura == "CUADRADO":
                self.dibujar_cuadrado(x, y, tamaño, color_traducido)
            elif figura == "PENTAGONO":
                self.dibujar_pentagono(x, y, tamaño, color_traducido)
            elif figura == "ESTRELLA":
                self.dibujar_estrella(x, y, tamaño, color_traducido)
            else:
                raise ValueError(f"Figura '{figura}' no soportada o sintaxis incorrecta.")

    def dibujar_circulo(self, x, y, radio, color):
        self.canvas.create_oval(x - radio, y - radio, x + radio, y + radio, fill=color)

    def dibujar_cuadrado(self, x, y, lado, color):
        self.canvas.create_rectangle(x, y, x + lado, y + lado, fill=color)

    def dibujar_rectangulo(self, x, y, ancho, alto, color):
        self.canvas.create_rectangle(x, y, x + ancho, y + alto, fill=color)

    def dibujar_pentagono(self, x, y, longitud, color):
        puntos = []
        for i in range(5):
            angulo = math.radians(72 * i - 90)
            puntos.append((x + longitud * math.cos(angulo), y + longitud * math.sin(angulo)))
        self.canvas.create_polygon(puntos, fill=color)

    def dibujar_estrella(self, x, y, radio, color):
        puntos = []
        for i in range(16):
            angulo = math.radians(360 / 16 * i - 90)
            r = radio if i % 2 == 0 else radio / 2
            puntos.append((x + r * math.cos(angulo), y + r * math.sin(angulo)))
        self.canvas.create_polygon(puntos, fill=color)


if __name__ == "__main__":
    root = tk.Tk()
    app = CompiladorFigurasApp(root)
    root.mainloop()
