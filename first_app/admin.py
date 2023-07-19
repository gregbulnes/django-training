from django.contrib import admin

from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'created_at')
    search_fields = ['title', 'content']
    ordering = ['-created_at']

admin.site.register(BlogPost, BlogPostAdmin)