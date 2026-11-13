import math
import tkinter as tk
from tkinter import ttk, messagebox


class CalculosNumericos:
    """
    Clase que agrupa operaciones matemáticas con manejo de múltiples excepciones:
    - Logaritmo neperiano y raíz cuadrada (Ejercicio 6.6).
    - Pendiente y punto medio de una recta (Ejercicios propuestos).
    - Raíces de una ecuación cuadrática (Ejercicio propuesto).
    - Conversión de base 10 a base b (Ejercicio propuesto).
    """

    @staticmethod
    def calcular_logaritmo_neperiano(valor_str: str) -> tuple[bool, str]:
        estado = "Operación completada"
        try:
            valor = float(valor_str)
            if valor <= 0:
                raise ArithmeticError("El valor debe ser un número positivo (mayor que 0).")
            resultado = math.log(valor)
            return True, f"Logaritmo neperiano ln({valor}) = {resultado:.6f}"
        except ValueError:
            estado = "Excepción de entrada capturada"
            return False, "Error (ValueError): El valor debe ser numérico para calcular el logaritmo."
        except ArithmeticError as e:
            estado = "Excepción aritmética capturada"
            return False, f"Error (ArithmeticError): {e}"
        finally:
            print(f"[Logaritmo Neperiano] {estado}")

    @staticmethod
    def calcular_raiz_cuadrada(valor_str: str) -> tuple[bool, str]:
        estado = "Operación completada"
        try:
            valor = float(valor_str)
            if valor < 0:
                raise ArithmeticError("El valor debe ser mayor o igual a cero para calcular la raíz cuadrada.")
            resultado = math.sqrt(valor)
            return True, f"Raíz cuadrada √({valor}) = {resultado:.6f}"
        except ValueError:
            estado = "Excepción de entrada capturada"
            return False, "Error (ValueError): El valor debe ser numérico para calcular la raíz cuadrada."
        except ArithmeticError as e:
            estado = "Excepción aritmética capturada"
            return False, f"Error (ArithmeticError): {e}"
        finally:
            print(f"[Raíz Cuadrada] {estado}")

    @staticmethod
    def calcular_pendiente(x1_str: str, y1_str: str, x2_str: str, y2_str: str) -> tuple[bool, str]:
        estado = "Operación completada"
        try:
            x1, y1 = float(x1_str), float(y1_str)
            x2, y2 = float(x2_str), float(y2_str)
            denominador = x2 - x1
            if denominador == 0:
                raise ZeroDivisionError("x₂ - x₁ es igual a 0; la pendiente es indefinida (recta vertical).")
            pendiente = (y2 - y1) / denominador
            return True, f"Pendiente de la recta (m) = {pendiente:.6f}"
        except ValueError:
            estado = "Excepción de entrada capturada"
            return False, "Error (ValueError): Todas las coordenadas (x₁, y₁, x₂, y₂) deben ser numéricas."
        except ZeroDivisionError as e:
            estado = "Excepción de división por cero capturada"
            return False, f"Error (ZeroDivisionError): {e}"
        except ArithmeticError as e:
            estado = "Excepción aritmética capturada"
            return False, f"Error (ArithmeticError): {e}"
        finally:
            print(f"[Pendiente Recta] {estado}")

    @staticmethod
    def calcular_punto_medio(x1_str: str, y1_str: str, x2_str: str, y2_str: str) -> tuple[bool, str]:
        estado = "Operación completada"
        try:
            x1, y1 = float(x1_str), float(y1_str)
            x2, y2 = float(x2_str), float(y2_str)
            xm = (x1 + x2) / 2
            ym = (y1 + y2) / 2
            if math.isinf(xm) or math.isinf(ym):
                raise OverflowError("El cálculo excede el rango numérico permitido.")
            return True, f"Punto medio M = ({xm:.4f}, {ym:.4f})"
        except ValueError:
            estado = "Excepción de entrada capturada"
            return False, "Error (ValueError): Todas las coordenadas (x₁, y₁, x₂, y₂) deben ser numéricas."
        except ArithmeticError as e:
            estado = "Excepción aritmética capturada"
            return False, f"Error (ArithmeticError): {e}"
        finally:
            print(f"[Punto Medio] {estado}")

    @staticmethod
    def calcular_raices_cuadraticas(a_str: str, b_str: str, c_str: str) -> tuple[bool, str]:
        estado = "Operación completada"
        try:
            a, b, c = float(a_str), float(b_str), float(c_str)
            if a == 0:
                raise ZeroDivisionError("El coeficiente 'a' no puede ser 0 en una ecuación cuadrática.")
            discriminante = (b ** 2) - (4 * a * c)
            if discriminante < 0:
                raise ArithmeticError(f"Discriminante negativo (Δ = {discriminante:.4f}); no existen raíces reales.")
            if discriminante == 0:
                x = -b / (2 * a)
                return True, f"Raíz real única: x = {x:.6f}"
            x1 = (-b + math.sqrt(discriminante)) / (2 * a)
            x2 = (-b - math.sqrt(discriminante)) / (2 * a)
            return True, f"Raíces reales:  x₁ = {x1:.6f}   |   x₂ = {x2:.6f}"
        except ValueError:
            estado = "Excepción de entrada capturada"
            return False, "Error (ValueError): Los coeficientes a, b y c deben ser numéricos."
        except ZeroDivisionError as e:
            estado = "Excepción de división por cero capturada"
            return False, f"Error (ZeroDivisionError): {e}"
        except ArithmeticError as e:
            estado = "Excepción aritmética capturada"
            return False, f"Error (ArithmeticError): {e}"
        finally:
            print(f"[Ecuación Cuadrática] {estado}")

    @staticmethod
    def convertir_base(numero_str: str, base_str: str) -> tuple[bool, str]:
        estado = "Operación completada"
        try:
            numero = int(numero_str)
            base = int(base_str)
            if base < 2 or base > 36:
                raise ArithmeticError("La base destino 'b' debe estar comprendida entre 2 y 36.")
            if numero == 0:
                return True, f"0 en base 10 = 0 (base {base})"

            digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            signo = "-" if numero < 0 else ""
            n = abs(numero)
            conversion = ""
            while n > 0:
                conversion = digitos[n % base] + conversion
                n //= base

            return True, f"{numero} (base 10)  =  {signo}{conversion} (base {base})"
        except ValueError:
            estado = "Excepción de entrada capturada"
            return False, "Error (ValueError): El número y la base deben ser valores enteros."
        except ArithmeticError as e:
            estado = "Excepción aritmética capturada"
            return False, f"Error (ArithmeticError): {e}"
        finally:
            print(f"[Conversión de Base] {estado}")


class InterfazCalculosNumericos(tk.Tk):
    """Interfaz gráfica de usuario para ejecutar los métodos de CalculosNumericos."""

    def __init__(self):
        super().__init__()
        self.title("Cálculos Numéricos y Manejo de Excepciones")
        self.geometry("620x440")
        self.resizable(False, False)
        self.configure(bg="#f4f6f9")

        self._configurar_estilos()
        self._construir_ui()

    def _configurar_estilos(self):
        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("TFrame", background="#f4f6f9")
        style.configure("TLabel", background="#f4f6f9", font=("Segoe UI", 10))
        style.configure("Header.TLabel", font=("Segoe UI", 13, "bold"), foreground="#1e293b")
        style.configure("Sub.TLabel", font=("Segoe UI", 9), foreground="#475569")
        style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
        style.configure("TNotebook", background="#f4f6f9")
        style.configure("TNotebook.Tab", font=("Segoe UI", 9, "bold"), padding=[10, 5])

    def _construir_ui(self):
        # Encabezado
        header_frame = ttk.Frame(self, padding=(15, 12, 15, 5))
        header_frame.pack(fill="x")
        ttk.Label(header_frame, text="Cálculos Numéricos — Gestión de Excepciones", style="Header.TLabel").pack(anchor="w")
        ttk.Label(
            header_frame,
            text="Ejercicio 6.6 y ejercicios propuestos con captura de ValueError, ZeroDivisionError y ArithmeticError.",
            style="Sub.TLabel",
        ).pack(anchor="w")

        # Contenedor de pestañas
        notebook = ttk.Notebook(self)
        notebook.pack(fill="both", expand=True, padx=15, pady=10)

        self.tab_basico = ttk.Frame(notebook, padding=15)
        self.tab_recta = ttk.Frame(notebook, padding=15)
        self.tab_cuadratica = ttk.Frame(notebook, padding=15)
        self.tab_base = ttk.Frame(notebook, padding=15)

        notebook.add(self.tab_basico, text="1. Logaritmo y Raíz")
        notebook.add(self.tab_recta, text="2. Recta (Pendiente / P. Medio)")
        notebook.add(self.tab_cuadratica, text="3. Ecuación Cuadrática")
        notebook.add(self.tab_base, text="4. Conversión de Base")

        self._crear_tab_basico()
        self._crear_tab_recta()
        self._crear_tab_cuadratica()
        self._crear_tab_base()

        # Panel de salida global
        salida_frame = tk.LabelFrame(
            self,
            text=" Resultado / Excepción Capturada ",
            bg="#ffffff",
            fg="#1e293b",
            font=("Segoe UI", 9, "bold"),
            padx=12,
            pady=10,
        )
        salida_frame.pack(fill="x", padx=15, pady=(0, 15))

        self.lbl_resultado = tk.Label(
            salida_frame,
            text="Ingrese los datos en la pestaña deseada y presione calcular.",
            bg="#ffffff",
            fg="#334155",
            font=("Consolas", 10),
            justify="left",
            wraplength=560,
        )
        self.lbl_resultado.pack(anchor="w")

    def _mostrar_respuesta(self, exito: bool, mensaje: str):
        if exito:
            self.lbl_resultado.config(text=mensaje, fg="#0f766e")
        else:
            self.lbl_resultado.config(text=mensaje, fg="#b91c1c")
            messagebox.showerror("Excepción Capturada", mensaje)

    # --- PESTAÑA 1: Logaritmo Neperiano y Raíz Cuadrada ---
    def _crear_tab_basico(self):
        ttk.Label(self.tab_basico, text="Valor numérico:").grid(row=0, column=0, sticky="w", pady=8)
        self.ent_valor = ttk.Entry(self.tab_basico, width=25, font=("Segoe UI", 10))
        self.ent_valor.grid(row=0, column=1, sticky="w", padx=10, pady=8)

        btn_frame = ttk.Frame(self.tab_basico)
        btn_frame.grid(row=1, column=0, columnspan=2, sticky="w", pady=12)

        ttk.Button(btn_frame, text="Logaritmo Neperiano", command=self._accion_logaritmo).pack(side="left", padx=(0, 8))
        ttk.Button(btn_frame, text="Raíz Cuadrada", command=self._accion_raiz).pack(side="left", padx=(0, 8))
        ttk.Button(btn_frame, text="Calcular Ambos", command=self._accion_ambos_basicos).pack(side="left")

    def _accion_logaritmo(self):
        exito, msg = CalculosNumericos.calcular_logaritmo_neperiano(self.ent_valor.get())
        self._mostrar_respuesta(exito, msg)

    def _accion_raiz(self):
        exito, msg = CalculosNumericos.calcular_raiz_cuadrada(self.ent_valor.get())
        self._mostrar_respuesta(exito, msg)

    def _accion_ambos_basicos(self):
        ok_log, msg_log = CalculosNumericos.calcular_logaritmo_neperiano(self.ent_valor.get())
        ok_raiz, msg_raiz = CalculosNumericos.calcular_raiz_cuadrada(self.ent_valor.get())
        self._mostrar_respuesta(ok_log and ok_raiz, f"{msg_log}\n{msg_raiz}")

    # --- PESTAÑA 2: Pendiente y Punto Medio de una Recta ---
    def _crear_tab_recta(self):
        ttk.Label(self.tab_recta, text="Punto 1 — x₁:").grid(row=0, column=0, sticky="w", pady=6)
        self.ent_x1 = ttk.Entry(self.tab_recta, width=14)
        self.ent_x1.grid(row=0, column=1, padx=(5, 20), pady=6)

        ttk.Label(self.tab_recta, text="y₁:").grid(row=0, column=2, sticky="w", pady=6)
        self.ent_y1 = ttk.Entry(self.tab_recta, width=14)
        self.ent_y1.grid(row=0, column=3, padx=5, pady=6)

        ttk.Label(self.tab_recta, text="Punto 2 — x₂:").grid(row=1, column=0, sticky="w", pady=6)
        self.ent_x2 = ttk.Entry(self.tab_recta, width=14)
        self.ent_x2.grid(row=1, column=1, padx=(5, 20), pady=6)

        ttk.Label(self.tab_recta, text="y₂:").grid(row=1, column=2, sticky="w", pady=6)
        self.ent_y2 = ttk.Entry(self.tab_recta, width=14)
        self.ent_y2.grid(row=1, column=3, padx=5, pady=6)

        btn_frame = ttk.Frame(self.tab_recta)
        btn_frame.grid(row=2, column=0, columnspan=4, sticky="w", pady=14)

        ttk.Button(btn_frame, text="Calcular Pendiente", command=self._accion_pendiente).pack(side="left", padx=(0, 8))
        ttk.Button(btn_frame, text="Calcular Punto Medio", command=self._accion_punto_medio).pack(side="left", padx=(0, 8))
        ttk.Button(btn_frame, text="Calcular Ambos", command=self._accion_ambos_recta).pack(side="left")

    def _accion_pendiente(self):
        exito, msg = CalculosNumericos.calcular_pendiente(
            self.ent_x1.get(), self.ent_y1.get(), self.ent_x2.get(), self.ent_y2.get()
        )
        self._mostrar_respuesta(exito, msg)

    def _accion_punto_medio(self):
        exito, msg = CalculosNumericos.calcular_punto_medio(
            self.ent_x1.get(), self.ent_y1.get(), self.ent_x2.get(), self.ent_y2.get()
        )
        self._mostrar_respuesta(exito, msg)

    def _accion_ambos_recta(self):
        ok_p, msg_p = CalculosNumericos.calcular_pendiente(
            self.ent_x1.get(), self.ent_y1.get(), self.ent_x2.get(), self.ent_y2.get()
        )
        ok_m, msg_m = CalculosNumericos.calcular_punto_medio(
            self.ent_x1.get(), self.ent_y1.get(), self.ent_x2.get(), self.ent_y2.get()
        )
        self._mostrar_respuesta(ok_p and ok_m, f"{msg_p}\n{msg_m}")

    # --- PESTAÑA 3: Ecuación Cuadrática ---
    def _crear_tab_cuadratica(self):
        ttk.Label(self.tab_cuadratica, text="Ecuación de la forma:  ax² + bx + c = 0").grid(
            row=0, column=0, columnspan=6, sticky="w", pady=(0, 10)
        )

        ttk.Label(self.tab_cuadratica, text="a:").grid(row=1, column=0, sticky="w")
        self.ent_a = ttk.Entry(self.tab_cuadratica, width=10)
        self.ent_a.grid(row=1, column=1, padx=(4, 15))

        ttk.Label(self.tab_cuadratica, text="b:").grid(row=1, column=2, sticky="w")
        self.ent_b = ttk.Entry(self.tab_cuadratica, width=10)
        self.ent_b.grid(row=1, column=3, padx=(4, 15))

        ttk.Label(self.tab_cuadratica, text="c:").grid(row=1, column=4, sticky="w")
        self.ent_c = ttk.Entry(self.tab_cuadratica, width=10)
        self.ent_c.grid(row=1, column=5, padx=4)

        ttk.Button(
            self.tab_cuadratica, text="Calcular Raíces", command=self._accion_cuadratica
        ).grid(row=2, column=0, columnspan=6, sticky="w", pady=15)

    def _accion_cuadratica(self):
        exito, msg = CalculosNumericos.calcular_raices_cuadraticas(
            self.ent_a.get(), self.ent_b.get(), self.ent_c.get()
        )
        self._mostrar_respuesta(exito, msg)

    # --- PESTAÑA 4: Conversión de Base 10 a Base b ---
    def _crear_tab_base(self):
        ttk.Label(self.tab_base, text="Número entero (base 10):").grid(row=0, column=0, sticky="w", pady=6)
        self.ent_num_base10 = ttk.Entry(self.tab_base, width=20)
        self.ent_num_base10.grid(row=0, column=1, sticky="w", padx=10, pady=6)

        ttk.Label(self.tab_base, text="Base destino b (2 - 36):").grid(row=1, column=0, sticky="w", pady=6)
        self.ent_base_destino = ttk.Entry(self.tab_base, width=20)
        self.ent_base_destino.grid(row=1, column=1, sticky="w", padx=10, pady=6)

        ttk.Button(
            self.tab_base, text="Convertir a Base b", command=self._accion_convertir_base
        ).grid(row=2, column=0, columnspan=2, sticky="w", pady=12)

    def _accion_convertir_base(self):
        exito, msg = CalculosNumericos.convertir_base(
            self.ent_num_base10.get(), self.ent_base_destino.get()
        )
        self._mostrar_respuesta(exito, msg)


if __name__ == "__main__":
    app = InterfazCalculosNumericos()
    app.mainloop()
