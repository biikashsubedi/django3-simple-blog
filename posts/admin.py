from django.contrib import admin
from .models import *


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'createdBy', 'created']
    list_display_links = ['title', 'created']
    search_fields = ['title']
    list_filter = ['created']
    list_per_page = 10


admin.site.register(Post, PostAdmin)
