# Generated by Django 3.2.4 on 2021-06-15 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barbers', '0002_auto_20210615_0031'),
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='barber',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='barbeiro_agendado', to='barbers.barber'),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]