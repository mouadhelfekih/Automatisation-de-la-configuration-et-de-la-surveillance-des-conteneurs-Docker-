from django.db import models
from django.contrib.auth.models import User



class Objet(models.Model):
    id_conteneur=models.CharField(max_length=300,null=True)
    id_image=models.CharField(max_length=300 ,null=False)
    username=models.ForeignKey(User ,null=True)
