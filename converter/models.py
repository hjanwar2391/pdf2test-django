from django.db import models

class PDFDocument(models.Model):
    file = models.FileField(upload_to='pdfs/')