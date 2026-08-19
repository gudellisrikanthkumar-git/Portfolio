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
    private ResumeExtractor() {
    }

    public static void main(String[] args) throws IOException {
        Path portfolioDirectory = locatePortfolioDirectory();
        Path resumePath = portfolioDirectory.resolve(
                Paths.get("assets", "resume", "Gudelli_Srikanth_Kumar_Resume.pdf"));
        Path outputPath = portfolioDirectory.resolve(Paths.get("data", "resume_raw.txt"));

        if (!Files.isRegularFile(resumePath)) {
            throw new IOException("Resume PDF not found: " + resumePath);
        }

        String extractedText;
        try (PDDocument document = Loader.loadPDF(resumePath.toFile())) {
            PDFTextStripper stripper = new PDFTextStripper();
            StringBuilder text = new StringBuilder();
            for (int page = 1; page <= document.getNumberOfPages(); page++) {
                stripper.setStartPage(page);
                stripper.setEndPage(page);
                text.append("\n--- PAGE ").append(page).append(" ---\n");
                text.append(stripper.getText(document));
            }
            extractedText = text.toString();
        }

        Files.createDirectories(outputPath.getParent());
        Files.writeString(outputPath, extractedText, StandardCharsets.UTF_8);
        System.out.print(extractedText);
        System.out.println("\n[Raw text saved to " + outputPath + "]");
    }

    private static Path locatePortfolioDirectory() {
        Path current = Paths.get("").toAbsolutePath().normalize();
        if (Files.isRegularFile(current.resolve(Paths.get("assets", "resume", "Gudelli_Srikanth_Kumar_Resume.pdf")))) {
            return current;
        }

        Path parent = current.getParent();
        if (parent != null && Files.isRegularFile(parent.resolve(
                Paths.get("assets", "resume", "Gudelli_Srikanth_Kumar_Resume.pdf")))) {
            return parent;
        }

        throw new IllegalStateException("Run this tool from the portfolio root or java-tools directory.");
    }
}
