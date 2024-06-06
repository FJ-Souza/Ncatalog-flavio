from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Roupa(models.Model):
    titulo = models.CharField(max_length=15)
    path = models.ImageField(upload_to="imagens/")
    descricao = models.TextField()

class Curtida(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    roupa_id = models.ForeignKey(Roupa, on_delete=models.CASCADE)

class Comentario(models.Model):
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE)
    roupa_id = models.ForeignKey(Roupa, on_delete=models.CASCADE)
    conteudo = models.TextField()
