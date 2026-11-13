import tkinter as tk
from tkinter import scrolledtext

def ejecutar_caso_de_uso():
    # Limpiar el área de registro de eventos
    txt_log.delete(1.0, tk.END)
    
    # Obtener valores de la interfaz
    try:
        dividendo = float(entry_dividendo.get())
        divisor = float(entry_divisor.get())
    except ValueError:
        txt_log.insert(tk.END, "Error de entrada: Por favor ingresa valores numéricos.\n")
        return

    txt_log.insert(tk.END, "=== INICIO DE EJECUCIÓN ===\n\n")

    # --- PRIMER BLOQUE TRY: Caso de uso de la división ---
    try:
        txt_log.insert(tk.END, "Ingresando al primer try\n")
        
        # Intento de división con los datos del usuario
        cociente = dividendo / divisor 
        
        # Si el divisor es 0, la siguiente línea no se ejecuta
        txt_log.insert(tk.END, f"Después de la división (Resultado: {cociente})\n")
        
    except ZeroDivisionError:
        txt_log.insert(tk.END, "División por cero\n")
        
    finally:
        txt_log.insert(tk.END, "Ingresando al primer finally\n")

    # --- SEGUNDO BLOQUE TRY: Excepción general ---
    try:
        txt_log.insert(tk.END, "Ingresando al segundo try\n")
        
        # Se simula el objeto nulo del ejercicio original
        objeto = None
        objeto.toString() # Lanza AttributeError (capturado como Exception general)
        
        txt_log.insert(tk.END, "Imprimiendo objeto\n")
        
    except ZeroDivisionError:
        txt_log.insert(tk.END, "División por cero\n")
        
    except Exception:
        txt_log.insert(tk.END, "Ocurrió una excepción\n")
        
    finally:
        txt_log.insert(tk.END, "Ingresando al segundo finally\n")

# --- CONFIGURACIÓN DE LA INTERFAZ GRÁFICA ---
ventana = tk.Tk()
ventana.title("Caso de Uso: Gestión de Excepciones")
ventana.geometry("400x500")
ventana.configure(padx=20, pady=20)

# Título
tk.Label(ventana, text="Calculadora con Gestión de Errores", font=("Arial", 12, "bold")).pack(pady=(0, 15))

# Entradas para la división
frame_inputs = tk.Frame(ventana)
frame_inputs.pack(pady=5)

tk.Label(frame_inputs, text="Dividendo:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_dividendo = tk.Entry(frame_inputs, width=15)
entry_dividendo.insert(0, "10000") # Valor por defecto del libro
entry_dividendo.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_inputs, text="Divisor:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_divisor = tk.Entry(frame_inputs, width=15)
entry_divisor.insert(0, "0") # Cero por defecto para forzar la excepción
entry_divisor.grid(row=1, column=1, padx=5, pady=5)

# Botón de ejecución
btn_ejecutar = tk.Button(ventana, text="Ejecutar División", bg="#2196F3", fg="white", font=("Arial", 10, "bold"), command=ejecutar_caso_de_uso)
btn_ejecutar.pack(pady=15)

# Consola de salida
tk.Label(ventana, text="Traza de ejecución (Diagrama de Estados):", font=("Arial", 9)).pack(anchor="w")
txt_log = scrolledtext.ScrolledText(ventana, width=45, height=12, font=("Consolas", 10), bg="#1e1e1e", fg="#00ff00")
txt_log.pack(pady=5)

ventana.mainloop()
