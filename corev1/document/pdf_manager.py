import PyPDF2
from corev1.document.models import DocumentModel
from corev1.folder.models import FolderModel
from user.models import UserModel
from elasticsearch import Elasticsearch
from polyglot.detect import Detector
from corev1.dialog.models import DialogModel
import nltk
import os
import uuid

class PdfManager():
    def __init__(self, document):
        self.es = Elasticsearch(["http://elasticsearch:9200"])
        self.document = document
        self.num_pages = self.num_of_pages()
        self.text = self.read_document()
        self.type = self.file_type()
        self.folder_name = self.folder_name()
        self.kb_uuid = self.folder_uuid()
        self.organization_name = self.organization_name()


    def read_document(self):
        '''
            Retorna o texto de um documento
        '''
        file = self.document.file.open('rb')
        reader = PyPDF2.PdfFileReader(file)
        text=''
        for i in range(0,reader.numPages):
            page = reader.getPage(i)
            text=text+page.extractText()
        return(text)

    def num_of_pages(self):
        '''
            Retorna o número de páginas de um documento
        '''
        file = self.document.file.open('rb')
        num_pages = PyPDF2.PdfFileReader(file).numPages
        return str(num_pages)

    def language_detector(self, text):
        '''
            Retorna a linguagem usada no texto
        '''
        try:
            detector = Detector(text)
            language = detector.language
            return language.name
        except:
            return 'Alguns caracteres impossibilitaram a verificação do idioma'

    def file_type(self):
        '''
            Retorna o tipo do arquivo
        '''
        file_name, file_ext = os.path.splitext(str(self.document.file))
        return file_ext

    def folder_name(self):
        '''
            Retorna o nome da pasta que o documento pertence
        '''
        try: 
            folder = FolderModel.objects.get(uuid=self.document.folder.uuid)
            return folder.name
        except:
            return 'Este documento não pertence a nenhuma pasta'

    def folder_uuid(self):
        '''
            Retorna o uuid da pasta que o documento pertence
        '''
        try: 
            folder = FolderModel.objects.get(uuid=self.document.folder.uuid)
            return folder.uuid
        except:
            return 'Este documento não pertence a nenhuma pasta'

    def organization_name(self):
        '''
            Retorna o nome da organização que o usuário proprietário do documento pertence
        '''
        try: 
            user = UserModel.objects.get(id=self.document.user_owner.id)
            return user.organization
        except:
            return 'Este documento não pertence a nenhum usuário/empresa'

    def save(self):
        '''
            Salva os dados e as sentenças de um documento no Elasticsearch
        '''
        sentencas = nltk.sent_tokenize(self.text)
        for sentenca in sentencas:
            doc = {
            'num_pages': self.num_pages,
            'language': self.language_detector(sentenca),
            'type': self.type,
            'text_length': len(sentenca),
            'folder_name': self.folder_name,
            'kb_uuid': self.kb_uuid,
            'file_uuid': self.document.uuid,
            'modification_date': self.document.updated,
            'text': sentenca,
            'organization_name': self.organization_name,
            'creation_date': self.document.created,
            'status': self.document.active
            }
            self.es.index(index=self.kb_uuid, body=doc)

    def search(question, kb_uuid, uuid_usuario):
        '''
            Retorna o id do dialog com todas as respostas  do usuário
        '''
        es = Elasticsearch(["http://elasticsearch:9200"])
        res = es.search(
            index=kb_uuid, 
            body={
                "query": {
                    "match": {
                        'text':question,
                    }
                }
            }
        )
        dialog_id = uuid.uuid4()
        user_owner = UserModel.objects.get(id=uuid_usuario)
        for hit in res['hits']['hits']:
            file = DocumentModel.objects.get(
                uuid = hit["_source"]['file_uuid']
            )
            dialog = DialogModel(
                question = question,
                answer = hit["_source"]['text'],
                file = file.file.name,
                user_owner = user_owner,
                dialog_id = dialog_id,
                answer_id = hit["_id"],
                folder_name = hit["_source"]['folder_name']
            )
            dialog.save()
        return dialog_id


