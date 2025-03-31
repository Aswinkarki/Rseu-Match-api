from django.db import models
import fitz  # PyMuPDF
import docx

class Resume(models.Model):
    file = models.FileField(upload_to='resumes/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField(blank=True, null=True)  # Store extracted text

    def __str__(self):
        return self.file.name

    def extract_text(self):
        """Extract text from uploaded resume file."""
        file_path = self.file.path
        text = ""

        if file_path.endswith('.pdf'):
            with fitz.open(file_path) as pdf:
                text = "\n".join([page.get_text() for page in pdf])

        elif file_path.endswith('.docx'):
            doc = docx.Document(file_path)
            text = "\n".join([para.text for para in doc.paragraphs])

        return text
