from django.contrib import admin
from .models import Post, Comment
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'author']
    list_filter = ['date']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
