import pdfplumber
import os

pdf_path = r"C:\Users\671893\OneDrive - Epiq Inc\Desktop\Portfolio\Gudelli_Srikanth_kumar .pdf"

if os.path.exists(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        full_text = ""
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            if text:
                full_text += f"\n--- PAGE {i+1} ---\n"
                full_text += text
        print(full_text)
else:
    print(f"File not found: {pdf_path}")
