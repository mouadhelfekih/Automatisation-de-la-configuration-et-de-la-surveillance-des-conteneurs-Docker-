from django.contrib import admin
from .models import Objet 

class Objetadmin(admin.ModelAdmin):
    list_display   = ('id_conteneur', 'id_image', 'username')

admin.site.register(Objet ,Objetadmin)
