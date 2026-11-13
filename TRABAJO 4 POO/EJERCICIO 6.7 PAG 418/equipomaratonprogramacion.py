import tkinter as tk
from tkinter import messagebox
import re

class Programador:
    """Clase que modela un integrante del equipo de programadores."""
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos


class EquipoMaratonProgramacion:
    """Clase que modela un equipo de maratón de programación."""
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = []
        self.tamano_equipo = 0
        self.max_integrantes = 3

    def esta_lleno(self):
        return self.tamano_equipo == self.max_integrantes

    def anadir(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)
        self.tamano_equipo += 1


def validar_campo(campo, tipo_campo):
    """Valida que los nombres y apellidos no tengan números ni excedan 20 caracteres."""
    if not campo:
        raise ValueError(f"El campo '{tipo_campo}' no puede estar vacío.")
    
    for caracter in campo:
        if caracter.isdigit():
            raise ValueError(f"El {tipo_campo} no puede tener dígitos.")
            
    if len(campo) > 20:
        raise ValueError(f"La longitud de '{tipo_campo}' no debe ser superior a 20 caracteres.")


def validar_contrasena(pwd1, pwd2):
    """Valida los requisitos de la contraseña según el ejercicio propuesto."""
    if len(pwd1) < 8:
        raise ValueError("La contraseña debe tener mínimo 8 caracteres.")
    if " " in pwd1:
        raise ValueError("La contraseña no debe tener espacios en blanco.")
    if not re.search(r'[a-z]', pwd1):
        raise ValueError("La contraseña debe tener por lo menos un carácter en minúscula.")
    if not re.search(r'[A-Z]', pwd1):
        raise ValueError("La contraseña debe tener por lo menos un carácter en mayúscula.")
    if not re.search(r'\d', pwd1):
        raise ValueError("La contraseña debe tener por lo menos un número.")
    if not re.search(r'[^a-zA-Z0-9\s]', pwd1):
        raise ValueError("La contraseña debe tener por lo menos un carácter especial.")
    if pwd1 != pwd2:
        raise ValueError("Las contraseñas no coinciden.")


class AppMaraton(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Registro - Maratón de Programación")
        self.geometry("450x650")
        self.configure(padx=20, pady=20)
        
        # --- Datos del equipo ---
        tk.Label(self, text="Datos del Equipo", font=("Arial", 12, "bold")).pack(anchor="w")
        
        self.entry_equipo = self.crear_input("Nombre del equipo:")
        self.entry_univ = self.crear_input("Universidad:")
        self.entry_lenguaje = self.crear_input("Lenguaje de programación:")
        
        # --- Contraseña (Ejercicio propuesto) ---
        tk.Label(self, text="Seguridad del Equipo", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10,0))
        self.entry_pwd1 = self.crear_input("Contraseña:", show="*")
        self.entry_pwd2 = self.crear_input("Confirmar contraseña:", show="*")
        
        # --- Datos de los integrantes ---
        tk.Label(self, text="Integrantes (Máximo 3)", font=("Arial", 12, "bold")).pack(anchor="w", pady=(10,0))
        
        self.integrantes_entries = []
        for i in range(3):
            frame = tk.Frame(self)
            frame.pack(fill="x", pady=2)
            tk.Label(frame, text=f"Prog {i+1} - Nombre:").grid(row=0, column=0, sticky="w")
            ent_nombre = tk.Entry(frame, width=15)
            ent_nombre.grid(row=0, column=1, padx=5)
            
            tk.Label(frame, text="Apellido:").grid(row=0, column=2, sticky="w")
            ent_apellido = tk.Entry(frame, width=15)
            ent_apellido.grid(row=0, column=3, padx=5)
            
            self.integrantes_entries.append((ent_nombre, ent_apellido))
            
        # --- Botón Registrar ---
        tk.Button(self, text="Registrar Equipo", command=self.registrar_equipo, bg="green", fg="white", font=("Arial", 10, "bold")).pack(pady=20)

    def crear_input(self, label_text, show=None):
        frame = tk.Frame(self)
        frame.pack(fill="x", pady=2)
        tk.Label(frame, text=label_text, width=20, anchor="w").pack(side="left")
        entry = tk.Entry(frame, show=show)
        entry.pack(side="left", expand=True, fill="x")
        return entry

    def registrar_equipo(self):
        try:
            # 1. Validar contraseñas
            validar_contrasena(self.entry_pwd1.get(), self.entry_pwd2.get())
            
            # 2. Crear equipo
            nombre_equipo = self.entry_equipo.get()
            universidad = self.entry_univ.get()
            lenguaje = self.entry_lenguaje.get()
            
            if not nombre_equipo or not universidad or not lenguaje:
                raise ValueError("Los datos del equipo no pueden estar vacíos.")
                
            equipo = EquipoMaratonProgramacion(nombre_equipo, universidad, lenguaje)
            
            # 3. Validar y añadir programadores
            for i, (ent_nom, ent_ape) in enumerate(self.integrantes_entries):
                nom = ent_nom.get()
                ape = ent_ape.get()
                
                validar_campo(nom, f"Nombre del programador {i+1}")
                validar_campo(ape, f"Apellido del programador {i+1}")
                
                prog = Programador(nom, ape)
                equipo.anadir(prog)
            
            # Si todo está correcto
            messagebox.showinfo("Éxito", f"El equipo '{equipo.nombre_equipo}' con {equipo.tamano_equipo} integrantes ha sido registrado correctamente.")
            
        except Exception as e:
            # Muestra las excepciones generadas en una ventana de error
            messagebox.showerror("Error de Validación", str(e))


if __name__ == "__main__":
    app = AppMaraton()
    app.mainloop()
