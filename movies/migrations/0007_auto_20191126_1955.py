# Generated by Django 2.2.6 on 2019-11-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20191122_2122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='linkmovie',
        ),
        migrations.AddField(
            model_name='movie',
            name='linkname',
            field=models.CharField(error_messages={'unique': 'Movie with this link already exists'}, max_length=100, null=True, unique=True, verbose_name='Name of movie for link'),
        ),
    ]
