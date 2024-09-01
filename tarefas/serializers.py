from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Tarefa


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class TarefaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'atribuicao',  ]
