from rest_framework import serializers
from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = '__all__'
        read_only_fields = ['text']

    def create(self, validated_data):
        resume = Resume.objects.create(**validated_data)
        resume.text = resume.extract_text()  # Extract text after saving
        resume.save()
        return resume
