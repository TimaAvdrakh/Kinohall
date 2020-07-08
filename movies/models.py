from django.db import models

class series(models.Model):
    title = models.CharField(max_length=50,null=True , verbose_name='Name of movie', unique=True,
                             error_messages={'unique': 'Movie with this title already exists'})
    linkposter = models.TextField(verbose_name='link to poster', null=True)
    year = models.IntegerField(verbose_name='Year', null=True)
    abouttheseries = models.TextField(verbose_name='About the series', null=True)
    rating = models.IntegerField(verbose_name='Rating', null=True,)
    country = models.CharField(max_length=30, verbose_name='Country', null=True)
    time = models.CharField(max_length=20, verbose_name='Time of movie', null=True)
    producer = models.CharField(max_length=40, verbose_name='Producer', null=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published', null=True)
    linkname = models.CharField(max_length=100, verbose_name='Kinopoisk id of series', null=True, unique=True,
                                error_messages={'unique': 'Movie with this link already exists'})
    gender = models.ForeignKey('Gender', null=True, on_delete=models.PROTECT, verbose_name='Gender')

    class Meta:
        verbose_name = 'Series'
        verbose_name_plural = 'Serials'
        ordering = ['-published']

class seriesComment(models.Model):
    Series = models.ForeignKey(series, on_delete=models.CASCADE,verbose_name='Movie', null=True)
    author = models.CharField(max_length=30, verbose_name='Author')
    content = models.TextField(verbose_name='Content')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Display on screen?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='Published')

    class Meta:
        verbose_name_plural = 'Series_Comments'
        verbose_name = "Series_Comment"
        ordering = ['created_at']

class movie(models.Model):
    title = models.CharField(max_length=50, verbose_name='Name of movie', unique=True,
                             error_messages={'unique': 'Movie with this title already exists'})
    linkslider = models.TextField(verbose_name='link to slider', null=True)
    linkposter = models.TextField(verbose_name='link to poster', null=True)
    year = models.IntegerField(verbose_name='Year')
    aboutthefilm = models.TextField(verbose_name='About the film', null=True)
    rating = models.IntegerField(verbose_name='Rating', null=True,)
    country = models.CharField(max_length=30, verbose_name='Country')
    time = models.CharField(max_length=20, verbose_name='Time of movie')
    producer = models.CharField(max_length=40, verbose_name='Producer')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')
    linkname = models.CharField(max_length=100, verbose_name='Kinopoisk id of series', null=True, unique=True,
                                error_messages={'unique': 'Movie with this link already exists'})
    gender = models.ForeignKey('Gender', null=True, on_delete=models.PROTECT, verbose_name='Gender')

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['-published']

class Gender(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Gender')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'
        ordering = ['name']

class Comment(models.Model):
    Movie = models.ForeignKey(movie, on_delete=models.CASCADE, verbose_name='Movie', null=True)
    author = models.CharField(max_length=30, verbose_name='Author')
    content = models.TextField(verbose_name='Content')
    is_active = models.BooleanField(default=True, db_index=True, verbose_name='Display on screen?')
    created_at = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='Published')

    class Meta:
        verbose_name_plural = 'Comments'
        verbose_name = "Comment"
        ordering = ['created_at']