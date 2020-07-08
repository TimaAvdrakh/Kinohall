from django.contrib import admin

from .models import movie
from .models import Gender
from .models import Comment
from .models import series, seriesComment


class movieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'producer', 'time', 'published', 'gender')
    list_display_links = ('title', 'year')
    search_fields = ('title', 'year', 'producer')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('Movie', 'author', 'created_at')
    list_display_links = ('Movie', 'author')
    search_fields = ('Movie', 'author')

class seriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'producer', 'time', 'published', 'gender')
    list_display_links = ('title', 'year')
    search_fields = ('title', 'year', 'producer')

class seriesCommentAdmin(admin.ModelAdmin):
    list_display = ('Series', 'author', 'created_at')
    list_display_links = ('Series', 'author')
    search_fields = ('Series', 'author')

admin.site.register(movie, movieAdmin)
admin.site.register(Gender)
admin.site.register(Comment, CommentAdmin)
admin.site.register(series, seriesAdmin)
admin.site.register(seriesComment, seriesCommentAdmin)
