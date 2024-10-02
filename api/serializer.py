from rest_framework import serializers
from .models import Livro

class LivroSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Livro
        fields = '__all__'

    class LivroSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField()
        titulo = serializers.IntegerField(max_Length=100)
        autor = serializers.CharField(max_Length=100)
        publicado_em = serializers.DateField()            