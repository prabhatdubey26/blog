from django.contrib import admin
from .models import Post
# Register your models here.


class PostDisplay(admin.ModelAdmin):
    list_display = ['sno','title','content','author', 'slug','timestamp']
    list_filter = ['sno', 'title','author']

admin.site.register(Post,PostDisplay)