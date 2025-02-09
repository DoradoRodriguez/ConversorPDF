# Convertidor TXT a PDF

Aplicación portable para convertir archivos de texto a PDF.

## Uso
1. Ejecute `ConvertidorPDF.exe` (Windows) o `ConvertidorPDF` (Unix)
2. Seleccione su archivo TXT
3. El PDF se generará en la ubicación que elija

## Características
- Portable (no requiere instalación)
- Interfaz gráfica intuitiva
- Soporte para caracteres especiales
- Vista previa automática del PDF generado

## Para Desarrolladores
1. Crear entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # o 'venv\Scripts\activate' en Windows
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Construir ejecutable:
   ```bash
   python build.py
   ```

El ejecutable se creará en la carpeta `ConversorPDF`. 