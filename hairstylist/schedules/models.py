from django.db import models

class Schedule(models.Model):
    barber = models.ForeignKey('barbers.Barber',on_delete=models.CASCADE,related_name="barbeiro_agendado",null=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    name = models.CharField(max_length=255, null=True)
    cpf = models.CharField(max_length=20,null=True)
    email = models.EmailField(null=True)
