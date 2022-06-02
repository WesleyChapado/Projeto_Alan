from rest_framework import serializers
from corev1.folder.models import FolderModel

class FolderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FolderModel
        fields = ('__all__')