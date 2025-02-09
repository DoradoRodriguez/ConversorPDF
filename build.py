import PyInstaller.__main__
import os
import sys
import shutil
from PIL import Image, ImageDraw, ImageFont

def create_icon():
    """Crear ícono base y convertirlo según la plataforma"""
    print("Creando ícono...")
    
    # Crear imagen base
    size = 512
    image = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Dibujar círculo azul
    margin = size // 8
    draw.ellipse([margin, margin, size - margin, size - margin], fill="#4A90E2")
    
    # Agregar texto "PDF"
    font_size = size // 3
    try:
        font = ImageFont.truetype("Arial", font_size)
    except:
        font = ImageFont.load_default()
    
    text = "PDF"
    bbox = draw.textbbox((0, 0), text, font=font)
    x = (size - (bbox[2] - bbox[0])) // 2
    y = (size - (bbox[3] - bbox[1])) // 2
    draw.text((x, y), text, font=font, fill="white")
    
    # Guardar según plataforma
    if not os.path.exists('assets'):
        os.makedirs('assets')
        
    if sys.platform.startswith('win'):
        image.save('assets/icon.ico', format='ICO', sizes=[(256, 256), (128, 128), (64, 64), (32, 32), (16, 16)])
    else:
        image.save('assets/icon.png', format='PNG')

def build():
    """Construir ejecutable portable"""
    # Limpiar directorios anteriores
    for dir_name in ['build', 'dist']:
        if os.path.exists(dir_name):
            print(f"Limpiando {dir_name}/...")
            shutil.rmtree(dir_name)
    
    # Crear ícono
    create_icon()
    
    # Configurar argumentos según plataforma
    icon_path = 'assets/icon.ico' if sys.platform.startswith('win') else 'assets/icon.png'
    separator = ';' if sys.platform.startswith('win') else ':'
    
    # Construir ejecutable
    PyInstaller.__main__.run([
        'src/makeItPdf.py',
        '--onefile',
        '--noconsole',
        '--name=ConvertidorPDF',
        '--distpath=ConvertidorPDF',
        f'--icon={icon_path}',
        f'--add-data=assets{separator}assets',
        '--clean'
    ])
    
    print("\n✓ Construcción completada")
    print(f"El ejecutable está en: ConvertidorPDF/ConvertidorPDF{'exe' if sys.platform.startswith('win') else ''}")

if __name__ == "__main__":
    build() 