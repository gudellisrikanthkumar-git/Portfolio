import pdfplumber
import json
from pathlib import Path
import re

# Find the PDF file
portfolio_dir = Path(__file__).resolve().parents[1]
pdf_files = list((portfolio_dir / "assets" / "resume").glob("*.pdf"))
pdf_path = pdf_files[0]

# Extract text from PDF
with pdfplumber.open(pdf_path) as pdf:
    full_text = ""
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            full_text += text + "\n"

# Parse the resume data
resume_data = {
    "personal_info": {
        "name": "Gudelli Srikanth Kumar",
        "phone": "+91-9177841357",
        "email": "gudellisrikanthkumar@gmail.com",
        "job_title": "QA Test Engineer",
        "total_experience": "5+ years"
    },
    "certifications": [],
    "work_experience": [],
    "projects": []
}

# Search for certifications section
certif_section = re.search(
    r'(?:CERTIFICATIONS?|PROFESSIONAL CERTIFICATIONS?)(.*?)(?:EDUCATION|TECHNICAL SKILLS|$)',
    full_text,
    re.IGNORECASE | re.DOTALL
)

if certif_section:
    certif_text = certif_section.group(1)
    # Parse individual certifications
    lines = [line.strip() for line in certif_text.split('\n') if line.strip()]
    for line in lines:
        if line and not line.startswith('---'):
            resume_data['certifications'].append({
                "name": line,
                "organization": "",
                "date": ""
            })

# Parse work experience from the main section
work_exp_matches = re.findall(
    r'Worked as (.*?) for (.*?) from (.*?) to (.*?)\.',
    full_text
)

for job_title, company, start_date, end_date in work_exp_matches:
    resume_data['work_experience'].append({
        "job_title": job_title.strip(),
        "company": company.strip(),
        "start_date": start_date.strip(),
        "end_date": end_date.strip(),
        "responsibilities": [],
        "achievements": []
    })

# Parse projects
project_pattern = r'Project #?\s*(\d+)\s*[-–]?\s*(.*?)(?:Client|Manual & Automation)'
projects = re.findall(project_pattern, full_text, re.IGNORECASE | re.DOTALL)

for proj_num, proj_name in projects:
    # Extract project details
    proj_section = re.search(
        f'Project #?\\s*{proj_num}.*?(?=Project #?|Education|Technical Skills|$)',
        full_text,
        re.IGNORECASE | re.DOTALL
    )
    
    if proj_section:
        proj_text = proj_section.group(0)
        
        client_match = re.search(r'Client\s*:?\s*(.*?)(?:\n|Manual)', proj_text, re.IGNORECASE)
        client = client_match.group(1).strip() if client_match else ""
        
        role_match = re.search(r'Role\s*:?\s*(.*?)(?:\n|Team)', proj_text, re.IGNORECASE)
        role = role_match.group(1).strip() if role_match else ""
        
        desc_match = re.search(r'Description\s*:?\s*(.*?)(?:Roles?|$)', proj_text, re.IGNORECASE | re.DOTALL)
        description = desc_match.group(1).strip() if desc_match else ""
        
        resp_match = re.search(r'Roles?[& ]*Responsibilities\s*:?\s*(.*?)(?:Declaration|Project|Education|$)', proj_text, re.IGNORECASE | re.DOTALL)
        responsibilities = []
        if resp_match:
            resp_text = resp_match.group(1)
            # Extract bullet points
            bullets = re.findall(r'●\s*(.*?)(?=●|$)', resp_text)
            responsibilities = [b.strip() for b in bullets if b.strip()]
        
        resume_data['projects'].append({
            "number": proj_num,
            "name": proj_name.strip(),
            "client": client,
            "role": role,
            "description": description,
            "responsibilities": responsibilities[:5]  # Limit to top 5
        })

# Save as JSON
with open(portfolio_dir / "data" / "resume_extracted.json", "w", encoding="utf-8") as f:
    json.dump(resume_data, f, indent=2, ensure_ascii=False)

print("="*80)
print("EXTRACTED RESUME DATA")
print("="*80)
print(json.dumps(resume_data, indent=2, ensure_ascii=False))

print("\n" + "="*80)
print("JSON saved to: resume_extracted.json")
print("="*80)
