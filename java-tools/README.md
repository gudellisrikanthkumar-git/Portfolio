# Java Resume Tools

This Maven utility replaces the resume text extraction step without changing the portfolio website or resume links.

## Requirements

- JDK 17 or newer
- Maven 3.9 or newer

## Run

From the repository root:

```powershell
mvn -f java-tools/pom.xml compile exec:java
```

The utility reads `assets/resume/Gudelli_Srikanth_Kumar_Resume.pdf` and writes extracted text to `data/resume_raw.txt`.
