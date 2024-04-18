from rest_framework import serializers
from drf.models import Student

class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    rollno = serializers.CharField(max_length=100)
    
    
    class Meta:
        model = Student
        fields = "__all__" 