from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed']

    def validate_title(self, value):
        if not value.strip():
            raise serializers.ValidationError("Title must not be empty.")
        return value
