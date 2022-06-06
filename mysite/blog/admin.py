from django.contrib import admin

from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'post', 'author',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
