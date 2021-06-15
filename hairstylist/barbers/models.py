from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

class Barber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="barber")
    email = models.EmailField(unique=True,null=True)
    name = models.CharField(max_length=255,null=True)
