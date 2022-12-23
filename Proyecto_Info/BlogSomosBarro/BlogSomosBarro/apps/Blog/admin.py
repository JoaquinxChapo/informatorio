from django.contrib import admin
from .models import Categorias,Noticias, Comentarios, Tarjetas,Trabajos, InfoIndex
# Register your models here.
admin.site.register(Categorias,admin.ModelAdmin)
admin.site.register(Noticias,admin.ModelAdmin)
admin.site.register(Comentarios,admin.ModelAdmin)
admin.site.register(Tarjetas,admin.ModelAdmin)
admin.site.register(Trabajos,admin.ModelAdmin)
admin.site.register(InfoIndex,admin.ModelAdmin)
