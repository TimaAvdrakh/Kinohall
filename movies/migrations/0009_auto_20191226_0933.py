# Generated by Django 2.2.6 on 2019-12-26 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='aboutthefilm',
            field=models.TextField(null=True, verbose_name='About the film'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='Movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.movie', verbose_name='Movie'),
        ),
        migrations.CreateModel(
            name='series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(error_messages={'unique': 'Movie with this title already exists'}, max_length=50, null=True, unique=True, verbose_name='Name of movie')),
                ('linkposter', models.TextField(null=True, verbose_name='link to poster')),
                ('year', models.IntegerField(null=True, verbose_name='Year')),
                ('abouttheseries', models.TextField(null=True, verbose_name='About the series')),
                ('rating', models.IntegerField(null=True, verbose_name='Rating')),
                ('country', models.CharField(max_length=30, null=True, verbose_name='Country')),
                ('time', models.CharField(max_length=20, null=True, verbose_name='Time of movie')),
                ('producer', models.CharField(max_length=40, null=True, verbose_name='Producer')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, null=True, verbose_name='Published')),
                ('linkname', models.CharField(error_messages={'unique': 'Movie with this link already exists'}, max_length=100, null=True, unique=True, verbose_name='Name of movie for link')),
                ('gender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='movies.Gender', verbose_name='Gender')),
            ],
            options={
                'verbose_name': 'Series',
                'verbose_name_plural': 'Serials',
                'ordering': ['-published'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='Series',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='movies.series', verbose_name='Series'),
        ),
    ]
