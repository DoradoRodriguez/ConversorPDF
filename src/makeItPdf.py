import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF
import sys

class ConvertidorPDF:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Convertidor de TXT a PDF")
        self.root.geometry("800x300")
        self.root.minsize(750, 250)
        
        # Establecer el ícono de la ventana
        try:
            if getattr(sys, 'frozen', False):
                # Si es ejecutable
                base_path = sys._MEIPASS
            else:
                # Si es script
                base_path = os.path.abspath(".")

            if sys.platform.startswith('win'):
                self.root.iconbitmap(os.path.join(base_path, 'assets', 'icon.ico'))
            else:
                img = tk.PhotoImage(file=os.path.join(base_path, 'assets', 'icon.png'))
                self.root.iconphoto(True, img)
        except Exception as e:
            print(f"No se pudo cargar el ícono: {e}")
        
        # Variables para las rutas de archivo
        self.input_file_path = tk.StringVar()
        self.output_file_path = tk.StringVar()
        
        self.create_widgets()
    
    def browse_input_file(self):
        filename = filedialog.askopenfilename(
            title="Seleccionar archivo TXT",
            filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
        )
        if filename:
            self.input_file_path.set(filename)
            # Sugerir nombre de salida
            suggested_output = os.path.splitext(filename)[0] + '.pdf'
            self.output_file_path.set(suggested_output)
    
    def browse_output_file(self):
        filename = filedialog.asksaveasfilename(
            title="Guardar PDF como",
            defaultextension=".pdf",
            initialfile=os.path.basename(self.output_file_path.get()) if self.output_file_path.get() else "documento.pdf",
            filetypes=[("Archivos PDF", "*.pdf")]
        )
        if filename:
            self.output_file_path.set(filename)
    
    def convert_to_pdf(self):
        if not self.input_file_path.get():
            messagebox.showerror("Error", "Por favor seleccione un archivo TXT")
            return
        
        if not self.output_file_path.get():
            messagebox.showerror("Error", "Por favor seleccione dónde guardar el PDF")
            return
        
        try:
            # Crear PDF con configuración específica
            pdf = FPDF(format='A4')
            pdf.set_margins(20, 20, 20)
            pdf.add_page()
            pdf.set_font('Arial', size=10)
            
            # Calcular el ancho efectivo de la página
            effective_width = pdf.w - 2 * pdf.l_margin
            
            # Leer archivo
            with open(self.input_file_path.get(), 'r', encoding='utf-8') as file:
                for line in file:
                    try:
                        text = line.strip()
                        if text:
                            words = text.split()
                            current_line = ""
                            
                            for word in words:
                                clean_word = ''.join(char if ord(char) < 128 else ' ' for char in word)
                                test_line = current_line + " " + clean_word if current_line else clean_word
                                
                                if pdf.get_string_width(test_line) < effective_width:
                                    current_line = test_line
                                else:
                                    if current_line:
                                        pdf.multi_cell(effective_width, 5, current_line)
                                    current_line = clean_word
                            
                            if current_line:
                                pdf.multi_cell(effective_width, 5, current_line)
                            pdf.ln(2)
                            
                    except Exception as e:
                        print(f"Warning: Problema al procesar línea: {str(e)}")
                        continue
            
            # Guardar PDF
            pdf.output(self.output_file_path.get())
            messagebox.showinfo("Éxito", "¡PDF creado correctamente!")
            
            # Abrir el PDF
            if sys.platform.startswith('win'):
                os.startfile(self.output_file_path.get())
            elif sys.platform.startswith('darwin'):
                os.system(f'open "{self.output_file_path.get()}"')
            else:
                os.system(f'xdg-open "{self.output_file_path.get()}"')
            
        except Exception as e:
            messagebox.showerror("Error", f"Error al crear el PDF: {str(e)}")
    
    def create_widgets(self):
        # Crear widgets
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True, fill='both')
        
        tk.Label(frame, text="Convertidor de TXT a PDF", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Frame para archivo de entrada
        input_frame = tk.Frame(frame)
        input_frame.pack(fill='x', pady=5)
        
        tk.Label(input_frame, text="Archivo de entrada:").pack(side='left')
        tk.Entry(input_frame, textvariable=self.input_file_path, width=50).pack(side='left', padx=5)
        tk.Button(input_frame, text="Buscar", command=self.browse_input_file).pack(side='left')
        
        # Frame para archivo de salida
        output_frame = tk.Frame(frame)
        output_frame.pack(fill='x', pady=5)
        
        tk.Label(output_frame, text="Guardar PDF como:").pack(side='left')
        tk.Entry(output_frame, textvariable=self.output_file_path, width=50).pack(side='left', padx=5)
        tk.Button(output_frame, text="Guardar", command=self.browse_output_file).pack(side='left')
        
        # Botón de conversión
        tk.Button(frame, text="Convertir a PDF", command=self.convert_to_pdf).pack(pady=10)

def main():
    app = ConvertidorPDF()
    app.root.mainloop()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", f"Error fatal: {e}")