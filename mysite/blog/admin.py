from django.contrib import admin
from .models import Post, BlogComment
# Register your models here.


class PostDisplay(admin.ModelAdmin):
    list_display = ['title','content','author', 'slug','timestamp']
    list_filter = [ 'title','author']

class CommentDisplay(admin.ModelAdmin):
    list_display = ['comment','user','post', 'parent','timestamp']
    list_filter = [ 'user','post']

admin.site.register(Post,PostDisplay)
admin.site.register(BlogComment,CommentDisplay)
