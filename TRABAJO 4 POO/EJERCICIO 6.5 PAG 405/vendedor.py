import tkinter as tk
from tkinter import ttk, messagebox

class Vendedor:
    def __init__(self, nombre: str, apellidos: str, edad: int):
        self.nombre = nombre
        self.apellidos = apellidos
        
        # 1. Validar primero si es negativa o fuera del límite máximo (115)
        if edad < 0 or edad >= 115:
            raise ValueError("La edad no debe de ser negativa, ni mayor o igual a 115")
            
        # 2. Validar después si es menor de edad (entre 0 y 17)
        if edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
            
        # Si pasa ambas validaciones, se asigna la edad
        self.edad = edad

    def __str__(self):
        return f"Vendedor creado: {self.nombre} {self.apellidos}, Edad: {self.edad}"

# Ejercicio 2: Tabla ASCII con métodos get y set
class TablaAscii:
    def __init__(self):
        self.tabla = {}

    def set_simbolo(self, simbolo: str, numero: int):
        if not simbolo:
            raise ValueError("El parámetro símbolo no puede ser nulo o vacío.")
        self.tabla[simbolo] = numero

    def get_simbolo(self, simbolo: str) -> int:
        if not simbolo:
            raise ValueError("El parámetro símbolo no puede ser nulo o vacío.")
        if simbolo not in self.tabla:
            raise KeyError(f"El símbolo '{simbolo}' es inexistente.")
        return self.tabla[simbolo]



class AplicacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Resolución de Ejercicios - Excepciones")
        self.root.geometry("420x350")
        
        self.tabla_ascii = TablaAscii()

        # Crear pestañas
        notebook = ttk.Notebook(root)
        notebook.pack(pady=10, expand=True, fill='both')

        # Pestaña 1: Vendedor
        frame_vendedor = ttk.Frame(notebook)
        frame_vendedor.pack(fill='both', expand=True)
        notebook.add(frame_vendedor, text='1. Vendedor')

        # Pestaña 2: Tabla ASCII
        frame_ascii = ttk.Frame(notebook)
        frame_ascii.pack(fill='both', expand=True)
        notebook.add(frame_ascii, text='2. Tabla ASCII')

        self.construir_pestana_vendedor(frame_vendedor)
        self.construir_pestana_ascii(frame_ascii)

    # --- UI Pestaña Vendedor ---
    def construir_pestana_vendedor(self, frame):
        ttk.Label(frame, text="Nombre:").grid(row=0, column=0, padx=10, pady=15, sticky="e")
        self.entry_nombre = ttk.Entry(frame, width=30)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=15)

        ttk.Label(frame, text="Apellidos:").grid(row=1, column=0, padx=10, pady=15, sticky="e")
        self.entry_apellidos = ttk.Entry(frame, width=30)
        self.entry_apellidos.grid(row=1, column=1, padx=10, pady=15)

        ttk.Label(frame, text="Edad:").grid(row=2, column=0, padx=10, pady=15, sticky="e")
        self.entry_edad = ttk.Entry(frame, width=30)
        self.entry_edad.grid(row=2, column=1, padx=10, pady=15)

        btn_crear = ttk.Button(frame, text="Crear Vendedor", command=self.crear_vendedor)
        btn_crear.grid(row=3, column=0, columnspan=2, pady=25)

    def crear_vendedor(self):
        nombre = self.entry_nombre.get()
        apellidos = self.entry_apellidos.get()
        
        try:
            edad = int(self.entry_edad.get())
            # Controlador de excepciones que captura el error del constructor
            vendedor = Vendedor(nombre, apellidos, edad)
            messagebox.showinfo("Éxito", str(vendedor))
        except ValueError as e:
            # Captura errores de conversión (letras en vez de números) y las reglas de edad
            if "invalid literal" in str(e):
                messagebox.showerror("Error de tipo", "La edad debe ser un número entero.")
            else:
                messagebox.showerror("IllegalArgumentException", str(e))

    # --- UI Pestaña Tabla ASCII ---
    def construir_pestana_ascii(self, frame):
        ttk.Label(frame, text="Símbolo:").grid(row=0, column=0, padx=10, pady=20, sticky="e")
        self.entry_simbolo = ttk.Entry(frame, width=30)
        self.entry_simbolo.grid(row=0, column=1, padx=10, pady=20)

        ttk.Label(frame, text="Número (para Set):").grid(row=1, column=0, padx=10, pady=20, sticky="e")
        self.entry_numero = ttk.Entry(frame, width=30)
        self.entry_numero.grid(row=1, column=1, padx=10, pady=20)

        frame_botones = ttk.Frame(frame)
        frame_botones.grid(row=2, column=0, columnspan=2, pady=30)

        btn_set = ttk.Button(frame_botones, text="Set (Guardar)", command=self.guardar_simbolo)
        btn_set.pack(side="left", padx=10)

        btn_get = ttk.Button(frame_botones, text="Get (Recuperar)", command=self.recuperar_simbolo)
        btn_get.pack(side="right", padx=10)

    def guardar_simbolo(self):
        simbolo = self.entry_simbolo.get()
        try:
            numero = int(self.entry_numero.get())
            self.tabla_ascii.set_simbolo(simbolo, numero)
            messagebox.showinfo("Éxito", f"Símbolo '{simbolo}' guardado con el valor {numero}.")
        except ValueError as e:
            if "invalid literal" in str(e):
                messagebox.showerror("Error", "El valor numérico debe ser un entero.")
            else:
                messagebox.showerror("Error", str(e))

    def recuperar_simbolo(self):
        simbolo = self.entry_simbolo.get()
        try:
            valor = self.tabla_ascii.get_simbolo(simbolo)
            messagebox.showinfo("Resultado", f"El valor numérico de '{simbolo}' es: {valor}")
        except (ValueError, KeyError) as e:
            messagebox.showerror("Excepción Capturada", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionGUI(root)
    root.mainloop()
