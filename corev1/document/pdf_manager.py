import PyPDF2
from corev1.document.models import DocumentModel

def read_using_path(caminho_arquivo):
    file = open(caminho_arquivo, 'rb')
    reader = PyPDF2.PdfFileReader(file)
    text=''
    for i in range(0,reader.numPages):
        page = reader.getPage(i)
        text=text+page.extractText()
    return(text)

def read_using_document_uuid(uuid):
    document = DocumentModel.objects.get(uuid=uuid)
    file = document.file.open('rb')
    reader = PyPDF2.PdfFileReader(file)
    text=''
    for i in range(0,reader.numPages):
        page = reader.getPage(i)
        text=text+page.extractText()
    return(text)