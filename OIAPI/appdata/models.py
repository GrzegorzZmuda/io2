from django.db import models

# Create your models here.
class Appdata(models.Model):
    name = models.CharField(max_length=100)  #Nazwa Aplikacji z której pobieramy logi
    env = models.CharField(max_length=15, default='SOME STRING') #framework z którego korzysta aplikacja
    version = models.CharField(max_length=50, default='SOME STRING') #wersja
    build = models.CharField(max_length=50, default='SOME STRING')  #buildq
    created = models.DateTimeField(auto_now_add=True) #datetime utworzenia rekordu

class Refined(models.Model):
    name = models.CharField(max_length=100)  #Nazwa Aplikacji z której pobieramy logi
    rpm = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True) #datetime utworzenia rekordu