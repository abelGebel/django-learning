from django.db import models

# Create your models here.

class Disco (models.Model):
    album = models.CharField(max_length=200)
    band = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(verbose_name="image",upload_to="discos")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "disco"
        verbose_name_plural = "discos"
        ordering = ["-created"]

    def __str__(self):
       return self.album 
    
    #superuser : abelg abelgebel@gmail.com abelg aaa