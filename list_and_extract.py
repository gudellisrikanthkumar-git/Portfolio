import os
import sys

directory = r"C:\Users\671893\OneDrive - Epiq Inc\Desktop\Portfolio"
print(f"Current directory: {directory}")
print(f"Directory exists: {os.path.exists(directory)}")
print("\nFiles in directory:")

if os.path.exists(directory):
    for item in os.listdir(directory):
        full_path = os.path.join(directory, item)
        print(f"  {item} (exists: {os.path.exists(full_path)})")
        
        # Check for PDF files
        if item.lower().endswith('.pdf'):
            print(f"    -> Found PDF file, attempting to open...")
            try:
                import pdfplumber
                with pdfplumber.open(full_path) as pdf:
                    print(f"    -> PDF opened successfully with {len(pdf.pages)} pages")
                    for page_num, page in enumerate(pdf.pages):
                        text = page.extract_text()
                        print(f"\n--- PAGE {page_num + 1} ---\n{text}\n")
            except Exception as e:
                print(f"    -> Error opening PDF: {e}")
else:
    print(f"Directory not found!")
