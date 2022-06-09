import PyPDF2

def reader():
    file = open("corev1/document/pdf_11_paginas.pdf","rb")
    reader = PyPDF2.PdfFileReader(file)
    text=''
    for i in range(0,reader.numPages):
        page = reader.getPage(i)
        text=text+page.extractText()
    return(text)

texto = reader()
print(texto)