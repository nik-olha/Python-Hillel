from django.contrib import admin
from .models import Post, Like


class LikeTabularInline(admin.TabularInline):
    model = Like


class PostAdmin(admin.ModelAdmin):
    inlines = [LikeTabularInline]
    model = Post
    list_display = ('user', 'title', 'content', 'image', 'created_at', 'update_at')


admin.site.register(Post, PostAdmin)
