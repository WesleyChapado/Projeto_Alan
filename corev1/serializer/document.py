from rest_framework import serializers
from corev1.document.models import DocumentModel
import os

from corev1.folder.models import FolderModel

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        exclude = ['id', 'active', 'deleted']

    def validate(self, data):
        file_name, file_ext = os.path.splitext(data['file'].name)
        if file_ext != '.pdf':
            raise serializers.ValidationError({'file':'O arquivo enviado deve ser do tipo PDF'})
        return data
