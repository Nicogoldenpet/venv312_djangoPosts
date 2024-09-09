from django.db import models

# Create your models here.
class Post(models.Model): #Creando la tabla Post para incluir nuestros textos
    message = models.TextField()
    
    def __str__(self): #Creando una función que nos permitirá ver los posts escritos
        return self.message[:50]