import pdfplumber
import os
import json

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
        
        # Save raw text to file for reference
        with open("resume_raw.txt", "w", encoding="utf-8") as f:
            f.write(full_text)
        print("\n\n[Raw text saved to resume_raw.txt]")
else:
    print(f"File not found: {pdf_path}")
