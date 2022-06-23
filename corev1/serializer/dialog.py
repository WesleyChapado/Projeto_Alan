from rest_framework import serializers
from corev1.dialog.models import DialogModel

class DialogSerializer(serializers.ModelSerializer):
	class Meta:
		model = DialogModel
		fields = ['question', 'answer', 'file']