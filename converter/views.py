import io
from django.shortcuts import render, redirect
from .forms import PDFUploadForm
from .models import PDFDocument
from pdfminer.high_level import extract_text

def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_doc = form.save()
            # PDF file convert to text
            pdf_path = pdf_doc.file.path
            text = extract_text(pdf_path)
            return render(request, 'converter/result.html', {'text': text})
    else:
        form = PDFUploadForm()
    return render(request, 'converter/upload.html', {'form': form})
