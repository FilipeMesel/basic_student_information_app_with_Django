from django.db import models

# Create your models here.
class StudentModel(models.Model):

    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    classe = models.CharField(max_length=100)
    marks = models.FloatField(default=0.0)
    
     
    def __str__(self):
        return self.nome