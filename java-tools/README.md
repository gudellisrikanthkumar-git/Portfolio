# Java Resume Tools

This Maven utility replaces the Python resume text extractor without changing the portfolio website or its links.

## Requirements

- Java 17+
- Maven 3.9+

## Run from the portfolio root

```powershell
mvn -f java-tools\pom.xml compile
mvn -f java-tools\pom.xml exec:java
```

The extractor reads:

`assets/resume/Gudelli_Srikanth_Kumar_Resume.pdf`

and writes:

`data/resume_raw.txt`
