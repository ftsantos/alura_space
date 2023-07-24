from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Fotografia(models.Model):
    
    
    OPCOES_CATEGORIA = [
        ("NEBULOSA", "Nebulosa"),
        ("ESTRELA", "Estrela"),
        ("GALÁXIA", "Galáxia"),
        ("PLANETA", "Planeta"),
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False, default='nome')
    legenda = models.CharField(max_length=150, null=False, blank=False, default='legenda22')
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False, default='descrição')
    #foto = models.CharField(max_length=100, null=False, blank=False)
    foto= models.ImageField(upload_to="fotos/%Y/%m/%d/", blank=True)
    publicada = models.BooleanField(default=True)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)
    #usuario = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    usuario = models.ForeignKey(
        to = User,
        on_delete=models.SET_NULL, #models.CASCADE
        null=True,
        blank=False,
        related_name='user',
    )
    
    def __str__(self):
        # return f"Fotografia [nome={self.nome}]"
        return self.nome
    
    