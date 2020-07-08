# Generated by Django 2.2.6 on 2019-11-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_auto_20191105_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='linkimage',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='poster',
        ),
        migrations.AddField(
            model_name='movie',
            name='linkposter',
            field=models.TextField(null=True, verbose_name='link to poster'),
        ),
        migrations.AddField(
            model_name='movie',
            name='linkslider',
            field=models.TextField(null=True, verbose_name='link to slider'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='linkmovie',
            field=models.TextField(null=True, verbose_name='link to movie'),
        ),
    ]