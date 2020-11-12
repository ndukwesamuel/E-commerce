from django.contrib.auth.models import  User
from django.db import models


class pppp(models.Model):
    name= models.CharField(max_length=100, null=True)
    price = models.IntegerField()
    description = models.TextField()
    product_pic = models.ImageField(upload_to = 'static/images/')

    def __str__(self):
        return self.name 