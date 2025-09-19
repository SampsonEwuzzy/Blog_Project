# blog/admin.py - Corrected
from django.contrib import admin
from .models import Post, Category

# Register the Post model using the decorator
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created_at']
    list_filter = ['status', 'created_at', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

# Register the Category model separately if not using a decorator
admin.site.register(Category)