from django.db import models
from datetime import datetime
from django.utils import timezone

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    def __string__(self):
        print(self.nombre)
        return(self.nombre)


"""comentarios"""
class Comentarios(models.Model):
    noticia= models.ForeignKey('noticias', related_name='comentarios', on_delete=models.CASCADE)
    autor=models.ForeignKey('auth.User', on_delete=models.CASCADE)
    creado = models.DateTimeField(default=timezone.now)
    aprobado=models.BooleanField(default=False)

    def aprobarComentario(self):
        self.aprobado=True
        self.save()


"""area de noticias"""
class Noticias(models.Model):
    autor=models.ForeignKey('auth.User', on_delete=models.CASCADE)    
    titulo=models.CharField(max_length=255)
    contenido= models.TextField()
    img=models.ImageField(null=True, blank=True, upload_to='img/images')
    creado=models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    publicado=models.DateTimeField(blank=True, null=True)
    categorias= models.ManyToManyField('Categorias',related_name='noticias')

    def PublicarNoticia(self):
        self.publicado=datetime.now()
        self.save()

    def comentarioAprobados(self):
        return self.comentarios.filter(aprobado=True)


"""Clase para la creacion de las tarjetas"""
class Tarjetas(models.Model):
    titulo=models.CharField(max_length=255)
    contenido= models.TextField()
    img=models.ImageField(null=True, blank=True, upload_to='img/images')
    categorias= models.ManyToManyField('Categorias',related_name='tarjetas')
    creado=models.DateTimeField(default=timezone.now)
    def Publicartarjetas(self):
        self.publicado=datetime.now()
        self.save()


class Trabajos(models.Model):
    titulo=models.CharField(max_length=255)
    contenido= models.TextField()
    img=models.ImageField(null=True, blank=True, upload_to='img/images')
    categorias= models.ManyToManyField('Categorias',related_name='trabajos')
    creado=models.DateTimeField(default=timezone.now)
    def Publicartrabajo(self):
        self.publicado=datetime.now()
        self.save()

class InfoIndex(models.Model):
    contenido=models.TextField(max_length=5000)
    categorias=models.ManyToManyField('Categorias', related_name='NosotrosIndex')
    creado=models.ManyToManyField('Categorias', related_name='infoindex')
    def PublicarNos(self):
        self.publicado=datetime.now()
        self.save()

class Team(models.Model):
    contenido= models.TextField()
    img=img=models.ImageField(null=True, blank=True, upload_to='img/images')
    tipo=models.TextField