# Generated by Django 4.1.1 on 2022-10-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_alter_familiares_fechadenac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiares',
            name='fechaDeNac',
            field=models.DateField(verbose_name='fechaDeNac'),
        ),
    ]
