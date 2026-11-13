import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

class LectorArchivosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lector de archivos TXT")
        # Tamaño inicial de la ventana
        self.root.geometry("650x450")
        self.root.minsize(550, 350)
        
        # --- Parte Superior: Selección de Archivo ---
        frame_superior = tk.Frame(root)
        frame_superior.pack(fill=tk.X, padx=15, pady=15)
        
        # Campo de entrada (Desactivado para imitar la visualización)
        self.entrada_ruta = tk.Entry(frame_superior, font=("Arial", 10), bg="#f0f0f0")
        self.entrada_ruta.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10), ipady=3)
        
        # Botón para seleccionar el archivo
        self.btn_seleccionar = tk.Button(
            frame_superior, 
            text="Seleccionar archivo", 
            font=("Arial", 9),
            command=self.seleccionar_archivo
        )
        self.btn_seleccionar.pack(side=tk.RIGHT, ipadx=5)
        
        # --- Parte Central: Área de Visualización ---
        self.area_texto = tk.Text(
            root, 
            font=("Consolas", 10), 
            wrap=tk.WORD, 
            bd=2, 
            relief="sunken"
        )
        self.area_texto.pack(fill=tk.BOTH, expand=True, padx=15, pady=(0, 10))
        
        # --- Parte Inferior: Botones de Acción ---
        frame_inferior = tk.Frame(root)
        frame_inferior.pack(pady=(0, 15))
        
        # Botón de Lectura Regular (Ejercicio 1)
        self.btn_leer = tk.Button(
            frame_inferior, 
            text="Leer archivo", 
            font=("Arial", 9),
            command=lambda: self.procesar_archivo(convertir_mayusculas=False)
        )
        self.btn_leer.pack(side=tk.LEFT, padx=5, ipadx=10, ipady=2)
        
        # Botón de Lectura en Mayúsculas (Ejercicio 2 propuesto)
        self.btn_leer_mayusculas = tk.Button(
            frame_inferior, 
            text="Leer en Mayúsculas", 
            font=("Arial", 9),
            command=lambda: self.procesar_archivo(convertir_mayusculas=True)
        )
        self.btn_leer_mayusculas.pack(side=tk.LEFT, padx=5, ipadx=10, ipady=2)

    def seleccionar_archivo(self):
        """Abre el diálogo de búsqueda para archivos TXT, tal como image_4.png"""
        ruta = filedialog.askopenfilename(
            title="Seleccionar archivo TXT",
            filetypes=[("Archivos de texto (*.txt)", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if ruta:
            # Reemplazar diagonales para que se vea con formato de Windows (como en la imagen)
            ruta_adaptada = ruta.replace("/", "\\")
            self.entrada_ruta.delete(0, tk.END)
            self.entrada_ruta.insert(0, ruta_adaptada)

    def procesar_archivo(self, convertir_mayusculas=False):
        """Lee el archivo seleccionado o procesa excepciones (image_5.png e image_6.png)"""
        ruta = self.entrada_ruta.get().strip()
        
        # 1. Validación de Selección (Igual a image_5.png)
        if not ruta:
            messagebox.showwarning(
                "Advertencia", 
                "Primero debes seleccionar un archivo."
            )
            return
            
        # 2. Intento de lectura con captura de IOException/FileNotFound (Igual a image_6.png)
        try:
            with open(ruta, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
                
                # Transformación de datos si se pide en mayúsculas (Ejercicio 2)
                if convertir_mayusculas:
                    contenido = contenido.upper()
                
                # Limpiar y mostrar resultado
                self.area_texto.delete(1.0, tk.END)
                self.area_texto.insert(tk.END, contenido)
                
        except (FileNotFoundError, OSError) as e:
            # Mensaje de error personalizado idéntico al solicitado (image_6.png)
            mensaje_error = f"No se pudo leer el archivo: {ruta} (El sistema no puede encontrar el archivo especificado)"
            messagebox.showerror("IOException", mensaje_error)


if __name__ == "__main__":
    ventana = tk.Tk()
    # Ejecuta la App con el diseño tradicional
    app = LectorArchivosApp(ventana)
    ventana.mainloop()
