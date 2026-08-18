import pdfplumber
import json
from pathlib import Path
import re

# Find the PDF file
portfolio_dir = Path(r"C:\Users\671893\OneDrive - Epiq Inc\Desktop\Portfolio")
pdf_files = list(portfolio_dir.glob("*.pdf"))
pdf_path = pdf_files[0]

# Extract text from PDF
with pdfplumber.open(pdf_path) as pdf:
    full_text = ""
    for i, page in enumerate(pdf.pages):
        text = page.extract_text()
        if text:
            full_text += text + "\n"

# Initialize comprehensive resume data
resume_data = {
    "personal_info": {
        "name": "Gudelli Srikanth Kumar",
        "phone": "+91-9177841357",
        "email": "gudellisrikanthkumar@gmail.com",
        "job_title": "QA Test Engineer",
        "total_experience": "5+ years"
    },
    "certifications": [],
    "work_experience": [
        {
            "job_title": "QA Test Engineer",
            "company": "Insurite Private Limited",
            "start_date": "June 2020",
            "end_date": "October 2024",
            "duration": "4 years 5 months",
            "key_responsibilities": [
                "Conducted manual and automated testing for multiple web and mobile applications",
                "Developed and executed test cases using Selenium WebDriver and TestNG frameworks",
                "Implemented data-driven and hybrid automation frameworks (Page Object Model, Page Factory)",
                "Worked on automated complex web flows (login, payments, search) using Playwright",
                "Collaborated with development team to integrate automated tests into CI/CD pipeline",
                "Attended sprint planning, daily standups, bug reviews, and retrospective meetings"
            ],
            "key_achievements": [
                "Reduced Regression bugs by 30% through comprehensive test automation",
                "Cut test execution time by 40% via parallel test runs",
                "Provided test deliverables on time as per client expectations including RTM, test case design, and training documentation"
            ]
        },
        {
            "job_title": "QA Test Engineer",
            "company": "Synergy Global Solutions",
            "start_date": "December 2024",
            "end_date": "November 2025",
            "duration": "12 months",
            "key_responsibilities": [
                "Performed Smoke, Functionality, Integration, System, and Regression testing",
                "Developed and maintained automated test scripts using Selenium WebDriver with Java",
                "Reviewed and documented requirements in BRD, FRD using Requirements Traceability Matrix (RTM)",
                "Collaborated with QA team to identify test scenarios and create test cases using Cucumber",
                "Performed Sanity testing before deploying releases to higher environments",
                "Implemented risk-based testing approaches when needed"
            ],
            "key_achievements": [
                "Improved test coverage and efficiency through data-driven testing approaches",
                "Successfully managed test data effectively across various scenarios",
                "Supported UAT testing and ensured smooth end-to-end testing lifecycle"
            ]
        }
    ],
    "projects": [
        {
            "number": 1,
            "name": "CSB (CIGNA SUPPLEMENTAL BENEFITS)",
            "client": "CIGNA - LIFE & HEALTH INSURANCE",
            "domain": "Insurance/Healthcare",
            "role": "QA Test Engineer",
            "team_size": 6,
            "tools_used": ["Selenium WebDriver", "Manual Testing", "TestNG"],
            "description": "Handled multiple insurance enrolling applications & Medicare Products including Cancer, Heart, Critical illness, and other enroll products (Dental) for aged 65 and older, people with disabilities and End-stage Renal Disease patients.",
            "key_responsibilities": [
                "Conducted manual and automated testing for multiple web and mobile applications, ensuring high-quality software releases",
                "Developed and executed test cases, test scenarios, and test scripts based on functional and non-functional requirements",
                "Utilized automation frameworks and tools (Selenium WebDriver, TestNG) to automate test cases, reducing testing time and improving efficiency",
                "Worked closely with development team to identify, troubleshoot, and resolve software defects",
                "Involved in Unit testing & Integration testing",
                "Attended sprint plan meetings, daily standups, bug reviews, and retrospective meetings",
                "Implemented data-driven testing approaches to increase test coverage and efficiency"
            ]
        },
        {
            "number": 2,
            "name": "FGI – AVO (Agent Virtual Office)",
            "client": "Future Generali India Insurance Company Ltd.",
            "domain": "Insurance",
            "role": "Test Engineer",
            "team_size": 7,
            "tools_used": ["Selenium WebDriver", "Manual Testing", "TestNG", "Cucumber", "SQL", "Maven"],
            "description": "Agent Virtual Office (AVO) Solutions - Portal for Intermediaries. One-stop solution enabling insurance companies to set up different privilege levels, generate quick quotes, issue policies, track business via dashboards, and provide self-service options for intermediaries.",
            "key_responsibilities": [
                "Reviewed and documented requirements in Business Requirements Document (BRD), Functional Requirements Documents (FRD), User Guidebook and established traceability using Requirements Traceability Matrix (RTM)",
                "Performed Smoke, Functionality, Integration, System, Regression tests based on analysis and understanding of requirements",
                "Developed and maintained automated test scripts using Selenium WebDriver with Java",
                "Collaborated with QA team to identify test scenarios and create test cases using Cucumber",
                "Performed Sanity testing before deploying any release to higher environment",
                "Tagged and Prioritized User stories for each sprint based on client requirements",
                "Utilized automation Frameworks and tools (Selenium WebDriver, TestNG, Cucumber, SQL, Maven) to automate test cases",
                "Identified, communicated and implemented risk-based testing approach when needed",
                "Involved in complete testing lifecycle including analysis, scenarios design, test case writing and execution"
            ]
        },
        {
            "number": 3,
            "name": "RECLS - Life Science (Provider Management)",
            "client": "Provider Management",
            "domain": "Healthcare/Pharmaceutical",
            "role": "QA Test Engineer",
            "team_size": 8,
            "tools_used": ["RTS2.0", "Manual Testing", "Automation Testing"],
            "description": "Healthcare provider management system for pharmaceutical and medtech manufacturers. Manages pricing agreements, pricing value drivers, and periodic backend rebates for different healthcare organizations (GPOs, IDNs, health systems, hospitals).",
            "key_responsibilities": [
                "Performed Smoke, Functionality, Integration, System, Regression tests based on analysis and understanding of requirements",
                "Worked closely with development team to identify, troubleshoot, and resolve software defects",
                "Involved in Unit testing & Integration testing",
                "Implemented data-driven testing approaches to increase test coverage and efficiency, managing test data effectively across various scenarios"
            ]
        }
    ],
    "technical_skills": {
        "automation": ["Selenium Java", "Selenium WebDriver", "Playwright", "Eclipse"],
        "testing_tools": ["SeleniumWebDriver", "IDE", "RC", "Grid", "TestNG", "RTS2.0", "Cucumber"],
        "database": ["Oracle SQL"],
        "version_control": ["GitHub"],
        "languages": ["Core Java"],
        "defect_tools": ["JIRA", "Confluence"],
        "packages": ["MS Office"]
    },
    "education": {
        "degree": "B.Tech in Computer Science Engineering (CSE)",
        "institution": "CMR College of Engineering and Technology",
        "location": "Hyderabad, Telangana",
        "year": 2015
    },
    "expertise_highlights": [
        "5+ years of Experience in IT Software Testing (Automation & Manual Testing)",
        "3+ years of experience in Selenium Web Driver with Java",
        "2+ years with Playwright for end-to-end automated complex web flows",
        "Expertise in Page Object Model and Data-driven framework design",
        "Proficient in Agile/Scrum methodology and SDLC/STLC",
        "Strong in API testing and mobile application testing",
        "Reduced Regression bugs by 30% and cut test execution time by 40% via Parallel runs",
        "Experience with CI/CD pipeline integration and test automation"
    ]
}

# Save as JSON
with open("resume_structured.json", "w", encoding="utf-8") as f:
    json.dump(resume_data, f, indent=2, ensure_ascii=False)

print("="*80)
print("COMPREHENSIVE RESUME EXTRACTION - JSON FORMAT")
print("="*80)
print(json.dumps(resume_data, indent=2, ensure_ascii=False))
print("\n✓ JSON file saved to: resume_structured.json")
