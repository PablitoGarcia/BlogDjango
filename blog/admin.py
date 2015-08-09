from django.contrib import admin
from django.utils.encoding import smart_unicode
from blog.models import Entrada , Categoria, Contacto, Mensajes
# Register your models here.
admin.site.register(Entrada)
admin.site.register(Categoria)
admin.site.register(Contacto)
admin.site.register(Mensajes)