import os
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

portfolio_dir = Path(__file__).resolve().parents[1]
directory = portfolio_dir / "assets" / "resume"
print(f"Current directory: {directory}")
print(f"Directory exists: {directory.exists()}")
print("\nFiles in directory:")

if directory.exists():
    for item in os.listdir(directory):
        full_path = directory / item
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
