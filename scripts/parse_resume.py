import pdfplumber
import os
import json
import re
from pathlib import Path

# Find the resume PDF in the organized asset directory.
portfolio_dir = Path(__file__).resolve().parents[1]
pdf_files = list((portfolio_dir / "assets" / "resume").glob("*.pdf"))

if not pdf_files:
    print("No PDF files found!")
    exit(1)

pdf_path = pdf_files[0]
print(f"Found PDF: {pdf_path}")

# Extract text from PDF
with pdfplumber.open(pdf_path) as pdf:
    full_text = ""
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            full_text += f"\n--- PAGE {i+1} ---\n"
            full_text += text

# Save raw text for reference
with open(portfolio_dir / "data" / "resume_raw.txt", "w", encoding="utf-8") as f:
    f.write(full_text)

print("\n" + "="*80)
print("RESUME CONTENT:")
print("="*80)
print(full_text)

# Now parse the content to extract certifications and work experience
print("\n\n" + "="*80)
print("PARSING CERTIFICATIONS AND WORK EXPERIENCE")
print("="*80)

# Split by sections - look for common headers
sections = {}
current_section = None
section_content = []

for line in full_text.split('\n'):
    line_stripped = line.strip()
    
    # Detect section headers (common patterns in resumes)
    if any(header in line_stripped.upper() for header in ['CERTIFICATIONS', 'CERTIFICATES', 'PROFESSIONAL CERTIFICATIONS']):
        if current_section:
            sections[current_section] = '\n'.join(section_content)
        current_section = 'CERTIFICATIONS'
        section_content = []
    elif any(header in line_stripped.upper() for header in ['WORK EXPERIENCE', 'PROFESSIONAL EXPERIENCE', 'EMPLOYMENT HISTORY', 'EXPERIENCE']):
        if current_section:
            sections[current_section] = '\n'.join(section_content)
        current_section = 'WORK_EXPERIENCE'
        section_content = []
    elif line_stripped and current_section:
        section_content.append(line)

# Don't forget the last section
if current_section:
    sections[current_section] = '\n'.join(section_content)

print("\nFound sections:", list(sections.keys()))
print("\n" + "-"*80)

if 'CERTIFICATIONS' in sections:
    print("\nCERTIFICATIONS SECTION:")
    print(sections['CERTIFICATIONS'])

print("\n" + "-"*80)

if 'WORK_EXPERIENCE' in sections:
    print("\nWORK EXPERIENCE SECTION:")
    print(sections['WORK_EXPERIENCE'])
