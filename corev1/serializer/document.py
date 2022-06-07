from rest_framework import serializers
from corev1.document.models import DocumentModel

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentModel
        exclude = ['active', 'deleted']