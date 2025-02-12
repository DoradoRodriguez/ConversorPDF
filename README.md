# TXT to PDF Converter

Portable application to convert text files to PDF.

## Usage
1. Run `ConvertidorPDF.exe` (Windows) or `ConvertidorPDF` (Unix)
2. Select your TXT file
3. The PDF will be generated in your chosen location

## Features
- Portable (no installation required)
- Intuitive graphical interface
- Special characters support
- Automatic preview of generated PDF

## For Developers
1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or 'venv\Scripts\activate' on Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Build executable:
   ```bash
   python build.py
   ```

The executable will be created in the `ConversorPDF` folder. 