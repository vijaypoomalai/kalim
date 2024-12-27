from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    Sno = serializers.IntegerField()
    Sname=serializers.CharField()
    city=serializers.CharField()
    result=serializers.ChoiceField(choices=[('P','Pass'),('F','Fail')])
    passby=serializers.CharField()
    
    