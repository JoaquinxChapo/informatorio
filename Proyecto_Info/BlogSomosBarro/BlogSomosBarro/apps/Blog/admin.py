from django.contrib import admin
from .models import Categorias,Noticias, Comentarios, Somos
# Register your models here.
admin.site.register(Categorias,admin.ModelAdmin)
admin.site.register(Noticias,admin.ModelAdmin)
admin.site.register(Comentarios,admin.ModelAdmin)
admin.site.register(Somos,admin.ModelAdmin)
