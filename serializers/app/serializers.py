from rest_framework import serializers
from app.models import *
from rest_framework.validators import UniqueValidator

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class TeacherSerializer(serializers.Serializer):
    Tname=serializers.CharField(max_length=100,validators=[UniqueValidator(queryset=Teacher.objects.all())])
    Sub=serializers.CharField(max_length=100)
    
    def create(self, validated_data):
        # Create a new Teacher object with the validated data
        teacher = Teacher.objects.create(**validated_data)
        return teacher
    
    def validate_Sub(self,value):
        if value not in ['Django','Python']:
            raise serializers.ValidationError('See the subjects Onceee...')
        return value
    
    def validate(self,data):
        if data['Tname'] != 'Harshad':
            raise serializers.ValidationError('it should be harshad')
        return data

