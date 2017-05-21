from rest_framework import serializers
from app.models import *

class ObjetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Objet
        fields = ('id_conteneur', 'id_image')

class renameSerializer(serializers.Serializer):
    id_conteneur = serializers.CharField(max_length=200)
    id_conteneur = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
