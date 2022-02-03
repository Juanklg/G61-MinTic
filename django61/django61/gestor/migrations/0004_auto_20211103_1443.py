# Generated by Django 3.2.5 on 2021-11-03 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0003_seccion'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='password',
            field=models.CharField(default='nulo', max_length=15),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(default='nulo', max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email',
            field=models.EmailField(default='nulo', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(default='nulo', max_length=30),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(default='nulo', max_length=15),
        ),
    ]
