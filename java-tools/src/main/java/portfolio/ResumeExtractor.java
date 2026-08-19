package portfolio;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import org.apache.pdfbox.Loader;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.text.PDFTextStripper;

public final class ResumeExtractor {
    private static final String RESUME_FILE = "Gudelli_Srikanth_Kumar_Resume.pdf";

    private ResumeExtractor() {
    }

    public static void main(String[] args) throws IOException {
        Path repositoryRoot = findRepositoryRoot();
        Path resumePath = repositoryRoot.resolve("assets").resolve("resume").resolve(RESUME_FILE);
        Path outputPath = repositoryRoot.resolve("data").resolve("resume_raw.txt");

        if (!Files.exists(resumePath)) {
            throw new IOException("Resume not found: " + resumePath);
        }

        Files.createDirectories(outputPath.getParent());

        String text;
        try (PDDocument document = Loader.loadPDF(resumePath.toFile())) {
            text = new PDFTextStripper().getText(document);
        }

        Files.writeString(outputPath, text, StandardCharsets.UTF_8);
        System.out.println("Resume extracted successfully.");
        System.out.println("Input:  " + resumePath);
        System.out.println("Output: " + outputPath);
    }

    private static Path findRepositoryRoot() {
        Path current = Paths.get(System.getProperty("user.dir")).toAbsolutePath().normalize();
        Path candidate = current;

        while (candidate != null) {
            if (Files.exists(candidate.resolve("index.html"))
                    && Files.isDirectory(candidate.resolve("assets"))) {
                return candidate;
            }
            candidate = candidate.getParent();
        }

        return current;
    }
}
